from common.csv_util import *
from common.mysql_db_manager import *
from db_settings import *

# 出力フォルダ
OUTPUT_DIR = 'output/db/'

# SQL
SQL_MST_POSTS = \
    f'''
SELECT
    wp_posts_A.id,
    wp_posts_A.post_type,
    wp_posts_A.post_title,
    wp_posts_A.post_name,
    wp_posts_B.guid as featured_image,
    wp_posts_A.post_date,
    wp_posts_A.post_modified
FROM
    wp_posts as wp_posts_A
    LEFT JOIN
        wp_postmeta
    ON  wp_posts_A.id = wp_postmeta.post_id
    AND wp_postmeta.meta_key = '_thumbnail_id'
    LEFT JOIN
        wp_posts as wp_posts_B
    ON  wp_posts_B.id = wp_postmeta.meta_value
WHERE
    wp_posts_A.post_type IN('post', 'page')
AND wp_posts_A.post_status = 'publish'
    '''

SQL_MST_TERMS = \
    f'''
SELECT
    wp_terms.term_id as id,
    wp_term_taxonomy.taxonomy,
    wp_terms.name,
    wp_terms.slug,
    wp_term_taxonomy.parent
FROM
    wp_terms
    INNER JOIN
        wp_term_taxonomy
    ON  wp_terms.term_id = wp_term_taxonomy.term_id
WHERE
    taxonomy IN('category', 'post_tag')
    '''

SQL_MST_TERM_RELATIONSHIPS = \
    f'''
SELECT
    object_id as post_id,
    term_taxonomy_id as term_id
FROM
    wp_term_relationships
    '''

# 出力定義
OUTPUT_MST_DATA_INFOS = [
    ['mst_posts', SQL_MST_POSTS],
    ['mst_terms', SQL_MST_TERMS],
    ['mst_term_relationships', SQL_MST_TERM_RELATIONSHIPS],
]


# 出力ファイル名生成
def create_output_file_path(file_name):
    return OUTPUT_DIR + file_name + '.csv'


# SQL実行結果をCSV書き出し
def output_sql_result_to_csv(output_path, sql):
    # SQL実行
    db_manager = MySqlDbManager(WORDPRESS_DB_USER, WORDPRESS_DB_PASSWORD, WORDPRESS_DB_HOST, WORDPRESS_DB_NAME)
    rows = db_manager.executeSqlWithColumnName(sql)
    # CSV書き込み
    CsvUtil.writeCsvFile(output_path, rows)


####################
# マスタデータ出力
####################
if __name__ == "__main__":
    for output_mst_data_info in OUTPUT_MST_DATA_INFOS:
        # 出力定義を取得
        output_file_name = output_mst_data_info[0]
        output_sql = output_mst_data_info[1]
        # SQLを実行してファイル出力
        output_path = create_output_file_path(output_file_name)
        output_sql_result_to_csv(output_path, output_sql)
