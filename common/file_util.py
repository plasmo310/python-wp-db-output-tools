class FileUtil:
    # テキストファイル書き込み
    @staticmethod
    def writeTextFile(file_path, output_rows):
        with open(file_path, 'w', encoding='UTF-8') as f:
            f.writelines(output_rows)
