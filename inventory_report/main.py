import sys
from inventory_report.inventory.inventory_refactor import InventoryRefactor
from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.xml_importer import XmlImporter


importer_lib = {
    "csv": CsvImporter,
    "json": JsonImporter,
    "xml": XmlImporter
}


def validate_args(arguments):
    if len(arguments) != 3:
        sys.stderr.write('Verifique os argumentos\n')
        return False
    return True


def main():
    arguments = sys.argv
    if validate_args(arguments):
        _, file_path, report_type = arguments
        file_type = file_path.split('.')[-1]
        instance = InventoryRefactor(importer_lib[file_type])
        report = instance.import_data(file_path, report_type)
        print(report, end="")


if __name__ == "__main__":
    main()
