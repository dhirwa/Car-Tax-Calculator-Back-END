from xlrd import open_workbook
from flask import jsonify,request
import sqlite3 as sql
from flask import Flask
import psycopg2



app=Flask(__name__)



class Arm(object):
    def __init__(self, cr_id,cr_brand,cr_mark,cr_engine,cr_drive,cr_year,cr_newprice,cr_body,cr_category):
        self.cr_id = cr_id
        self.cr_brand = cr_brand
        self.cr_mark = cr_mark
        self.cr_engine = cr_engine
        self.cr_drive = cr_drive
        self.cr_year = cr_year
        self.cr_newprice = cr_newprice
        self.cr_body = cr_body
        self.cr_category = cr_category

    def __str__(self):
        return("  car_id = {0}\n"
               "  car_brand = {1}\n"
               "  car_mark = {2}\n"
               "  car_engine = {3}\n"
               "  car_drive = {4}\n"
               "  car_year = {5}\n"
               "  car_newprice = {6}\n"
               "  car_body = {7}\n"
               "  car_category = {8}\n"
               .format(self.cr_id,self.cr_brand,self.cr_mark,self.cr_engine,self.cr_drive,self.cr_year,self.cr_newprice,self.cr_body,self.cr_category))

wb = open_workbook('toyota.xls')
for sheet in wb.sheets():
    number_of_rows = sheet.nrows
    number_of_columns = sheet.ncols

    items = []

    rows = []
    for row in range(1, number_of_rows):
        values = []
        for col in range(number_of_columns):
            value  = (sheet.cell(row,col).value)
            try:
                value = str(int(value))

            except ValueError:
                pass
            finally:
                values.append(value)


        item = Arm(*values)
        items.append(item)
    con = psycopg2.connect(database="cars", user="postgres", password="password", host="127.0.0.1", port="5432")
    cur=con.cursor()
    for item in items:
        q='INSERT INTO cars(cr_id,cr_brand,cr_mark,cr_engine,cr_drive,cr_year,cr_newprice,cr_body,cr_category) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s);'
        data=(item.cr_id,item.cr_brand,item.cr_mark,item.cr_engine,item.cr_drive,item.cr_year,item.cr_newprice,item.cr_body,item.cr_category)
        cur.execute(q,data)
        con.commit()

for item in items:
    print item
