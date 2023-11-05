from common.file_util import *
from common.mysql_db_manager import *
from db_settings import *

# 出力フォルダ
OUTPUT_DIR = 'output/posts/'

# SQL
SQL_POST_CONTENTS = \
    f'''
SELECT
    post_name,
    post_content
FROM
    wp_posts
WHERE
    post_type IN('post', 'page')
AND post_status = 'publish'
    '''


# 出力ファイル名生成
def create_output_file_path(file_name):
    return OUTPUT_DIR + file_name + '.txt'


####################
# 記事データ出力
####################
if __name__ == "__main__":
    db_manager = MySqlDbManager(WORDPRESS_DB_USER, WORDPRESS_DB_PASSWORD, WORDPRESS_DB_HOST, WORDPRESS_DB_NAME)
    rows = db_manager.executeSql(SQL_POST_CONTENTS)
    for row in rows:
        post_name = row[0]
        post_content = row[1]
        FileUtil.writeTextFile(create_output_file_path(post_name), post_content)
