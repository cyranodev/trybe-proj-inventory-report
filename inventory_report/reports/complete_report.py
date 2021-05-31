from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.utils import ReportsUtils


class CompleteReport(SimpleReport):
    @classmethod
    def generate(cls, report_list):
        simple_report = super().generate(report_list)
        stock = ReportsUtils.get_stock(report_list)
        stock_report = ""
        for key in stock:
            stock_report += f"- {key}: {stock[key]}\n"
        complete_report = (
            f"{simple_report}"
            "\nProdutos estocados por empresa: \n"
            f"{stock_report}"
        )
        return complete_report
