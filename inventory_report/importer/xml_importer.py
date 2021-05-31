from lxml import etree
from inventory_report.importer.importer import Importer


class XmlImporter(Importer):
    @staticmethod
    def import_data(file_path):
        if file_path.endswith('xml') is False:
            raise ValueError('Arquivo inválido')

        content_list = []
        with open(file_path, newline='') as xmlfile:
            content = etree.parse(xmlfile)
            root = content.getroot()
            get_records = root.findall('record')
            for record in get_records:
                content = {child.tag: child.text for child in record}
                content_list.append(content)

        return content_list
