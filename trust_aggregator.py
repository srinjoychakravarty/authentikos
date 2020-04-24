# Reading an excel file using Python
from decimal import Decimal
from statistics import mean
from tinydb import TinyDB, Query
import hashlib, os, xlrd

def populate_crowdsource_trust(dbname):
        # Give the location of the file
        location = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
        file_path = location + "/data/crowdsourced_study.xlsx"
        db = TinyDB(location + "/" + dbname + ".json")

        # To open workbook
        wb = xlrd.open_workbook(file_path)
        sheet = wb.sheet_by_index(0)

        # total number of rows
        total_rows = sheet.nrows

        trust_ratings_list = []
        for i in range(1, total_rows):
            temp_dict = {'checksum': hashlib.md5(bytes(sheet.cell_value(i, 0), 'utf-8')).hexdigest(), sheet.cell_value(0, 0): sheet.cell_value(i, 0), sheet.cell_value(0, 1): sheet.cell_value(i, 1), sheet.cell_value(0, 2): sheet.cell_value(i, 2), sheet.cell_value(0, 3): sheet.cell_value(i, 3), sheet.cell_value(0, 4): sheet.cell_value(i, 4), sheet.cell_value(0, 5): sheet.cell_value(i, 5), sheet.cell_value(0, 6): sheet.cell_value(i, 6)}
            trust_ratings_list.append(temp_dict)
            db.insert(temp_dict)

        return trust_ratings_list

if __name__ == "__main__":
    print(populate_crowdsource_trust("trustdb"))
