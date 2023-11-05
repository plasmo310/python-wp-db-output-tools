# python-wp-db-output-tools
- wordpressのDB情報をファイル出力するツール
  - マスタデータのCSV出力
  - 記事データのtext出力

## 使い方
* <code>db_settings.py.template</code>にDB情報を設定し、<code>db_settings.py</code>にリネームする
* <code>output/db</code>、<code>output/posts</code>フォルダを作成する
* <code>main_output_mst_data.py</code>、<code>main_output_post_content.py</code>をそれぞれ実行する