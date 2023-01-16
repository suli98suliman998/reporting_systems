from Report_Manager.Report import Report


class Table:
    def __init__(self):
        self.__columnTitles = []
        self.__rowTitles = []
        self.__tableContent = []
        self.currentRow = 0

    def set_column_titles(self, titles: [str]):
        self.__columnTitles = titles

    def set_row_titles(self, titles: [str]):
        self.__rowTitles = titles

    def set_table_content(self, content: [[str]]):
        self.__tableContent = content

    def get_column_titles(self):
        return self.__columnTitles

    def get_row_titles(self):
        return self.__rowTitles

    def get_table_content(self):
        return self.__tableContent

    def fillRow(self):
        pass

    def build_table(self, report: Report):
        pass
