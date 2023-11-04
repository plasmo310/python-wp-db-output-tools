import mysql.connector


# MySQL操作クラス
class MySqlDbManager:
    def __init__(self, user, password, host, database):
        # connector初期化
        connector = mysql.connector.connect(
            user=user,
            password=password,
            host=host,
            database=database
        )
        # 接続チェック
        if not connector.is_connected():
            print('db is not connected!!')
            return
        self.connector = connector

    # パラメータチェック
    def checkParameter(self):
        is_ok_parameter = True
        if self.connector is None:
            print('connector is not initialized!!')
            is_ok_parameter = False
        if not self.connector.is_connected():
            print('connector is not connected!!')
            is_ok_parameter = False
        return is_ok_parameter

    # 指定されたSQL実行
    def executeSqlWithColumnName(self, sql):
        if not self.checkParameter():
            return

        # dictionaryをTrue指定することで項目名をキーとした辞書型で返ってくる
        cursor = self.connector.cursor(dictionary=True)
        cursor.execute(sql)

        result = []
        # 一行目に項目名を追加
        column_names = []
        for row in cursor:
            for column_name in row:
                column_names.append(column_name)
            break
        result.append(column_names)
        # 後ろに値を追加
        for row in cursor:
            columns = []
            for column_name in row:
                columns.append(row[column_name])
            result.append(columns)
        return result

    def executeSql(self, sql):
        if not self.checkParameter():
            return
        cursor = self.connector.cursor()
        cursor.execute(sql)
        return cursor
