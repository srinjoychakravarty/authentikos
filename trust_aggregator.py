# Reading an excel file using Python
from decimal import Decimal
from statistics import mean
import os, psycopg2, xlrd

def insertMediaSources(mediaSourceList):
    """ insert multiple vendors into the vendors table  """
    sql = "INSERT INTO trust_ratings(mediaSource) VALUES(%s)"
    conn = None
    try:
        connect_str = "dbname='crowdsourced_judgement' user='postgres' host='localhost' " + "password='postgres'"
        # use our connection values to establish a connection
        conn = psycopg2.connect(connect_str)
        # create a psycopg2 cursor that can execute queries
        cur = conn.cursor()
        # execute the INSERT statement
        cur.executemany(sql, mediaSourceList)
        # commit the changes to the database
        conn.commit()
        # close communication with the database
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print("Uh oh, can't connect. Invalid dbname, user or password?")
        print(error)
    finally:
        if conn is not None:
            conn.close()




# def insert_into_table():
#     try:
#         connect_str = "dbname='crowdsourced_judgement' user='postgres' host='localhost' " + "password='postgres'"
#         # use our connection values to establish a connection
#         conn = psycopg2.connect(connect_str)
#         # create a psycopg2 cursor that can execute queries
#         cursor = conn.cursor()
#         # run a SELECT statement - no data in there, but we can try it
#         cursor.execute("""SELECT * from trust_ratings""")
#         # conn.commit() # <--- makes sure the change is shown in the database
#         rows = cursor.fetchall()
#         print(rows)
#         cursor.close()
#         conn.close()
#     except Exception as e:
#         print("Uh oh, can't connect. Invalid dbname, user or password?")
#         print(e)

if __name__ == "__main__":
    # Give the location of the file
    location = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
    file_path = location + "/trust.xlsx"
    print(file_path)

    # To open Workbook
    wb = xlrd.open_workbook(file_path)
    sheet = wb.sheet_by_index(0)

    # total number of rows
    total_rows = sheet.nrows

    media_trust_list = []

    for i in range(0, total_rows):
        new_score_array = []
        combined_string = sheet.cell_value(i, 0)
        data_array = combined_string.split()
        string_score_list = data_array[1:]
        decimal_score_list = [Decimal(x.strip(' "')) for x in string_score_list]
        temp_dict = {'mediaSource': data_array[0], 'averageTrust': (sum(decimal_score_list) / len(decimal_score_list))}
        media_trust_list.append(temp_dict)

    # print(media_trust_list)
    # most_trusted_media_sources = sorted(media_trust_list, key = lambda i: i['averageTrust'], reverse = True)
    most_trusted_media_sources = sorted(media_trust_list, key = lambda i: i['mediaSource'], reverse = False)
    print(most_trusted_media_sources)
    mediaSourceList = [item['mediaSource'] for item in most_trusted_media_sources]
    # print(mediaSourceList)
    #insertMediaSources(mediaSourceList)
