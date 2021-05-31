from inventory_report.main import importer_lib
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.simple_report import SimpleReport


class Inventory:
    @staticmethod
    def _call_importer(file_path):
        extension = file_path.split('.')[-1]
        try:
            return importer_lib[extension].import_data(file_path)
        except Exception:
            raise ValueError('formato de arquivo inválido')

    @staticmethod
    def _generate_report(content_list, report_type):
        if report_type == "simples":
            return SimpleReport.generate(content_list)
        elif report_type == "completo":
            return CompleteReport.generate(content_list)

    @classmethod
    def import_data(cls, file_path, report_type):
        content_list = cls._call_importer(file_path)
        return cls._generate_report(content_list, report_type)
