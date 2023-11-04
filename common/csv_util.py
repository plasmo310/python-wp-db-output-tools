import csv


class CsvUtil:
    # CSV書き込み
    @staticmethod
    def writeCsvFile(file_path, output_rows):
        with open(file_path, 'w') as f:
            writer = csv.writer(f)
            writer.writerows(output_rows)

    # CSV読み込み
    @staticmethod
    def readCsvFile(file_path):
        read_rows = []
        with open(file_path) as f:
            reader = csv.reader(f)
            for row in reader:
                read_rows.append(row)
        return read_rows
