import json
from inventory_report.importer.importer import Importer


class JsonImporter(Importer):
    @staticmethod
    def import_data(file_path):
        if not file_path.endswith('json'):
            raise ValueError('Arquivo inválido')

        content_list = []
        with open(file_path, newline='') as jsonfile:
            content_list = json.load(jsonfile)

        return content_list
