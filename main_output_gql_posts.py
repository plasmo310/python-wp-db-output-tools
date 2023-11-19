from common.file_util import *
from db_settings import *
from gql import gql, Client
from gql.transport.aiohttp import AIOHTTPTransport
import urllib.parse

# 出力フォルダ
OUTPUT_DIR = 'output/posts_gql/'

# クエリ
QUERY_GET_POSTS = \
    """
        query AllPosts {
            posts(first: 1000) {
              edges {
                node {
                  title
                  slug
                  content
                }
              }
            }
        }
    """

QUERY_GET_PAGES = \
    """
        query AllPages {
            pages(first: 1000) {
              edges {
                node {
                  title
                  slug
                  content
                }
              }
            }
        }
    """


# 出力ファイル名生成
def create_output_file_path(file_name):
    return OUTPUT_DIR + file_name + '.txt'


# lowercaseのエンコード結果を返却
def encode_lowercase(value):
    return urllib.parse.quote(value).lower()


####################
# 記事データ出力
# WordPress内で変換後のデータが欲しいためWPGraphQLで実行
####################
if __name__ == "__main__":
    # WPGraphQLを実行
    transport = AIOHTTPTransport(url=WP_GRAPH_QL_URL)
    client = Client(transport=transport)

    # 投稿記事
    query = gql(QUERY_GET_POSTS)
    result = client.execute(query)
    posts = result["posts"]["edges"]
    for post in posts:
        slug = post["node"]["slug"]
        content = post["node"]["content"]
        if slug is not None and content is not None:
            FileUtil.writeTextFile(create_output_file_path(encode_lowercase(slug)), content)

    # 固定ページ
    query = gql(QUERY_GET_PAGES)
    result = client.execute(query)
    pages = result["pages"]["edges"]
    for page in pages:
        slug = page["node"]["slug"]
        content = page["node"]["content"]
        if slug is not None and content is not None:
            FileUtil.writeTextFile(create_output_file_path(encode_lowercase(slug)), content)
