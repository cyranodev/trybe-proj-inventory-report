import csv
from inventory_report.importer.importer import Importer


class CsvImporter(Importer):
    @staticmethod
    def import_data(file_path):
        if not file_path.endswith('csv'):
            raise ValueError('Arquivo inválido')
        content_list = []
        with open(file_path, newline='') as csvfile:
            content_csv = csv.DictReader(csvfile, delimiter=",")
            [content_list.append(row) for row in content_csv]

        return content_list
