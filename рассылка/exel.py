import os
import pandas as pd
from openpyxl import load_workbook
from openpyxl.utils.dataframe import dataframe_to_rows


def exel(file):
    workbook = load_workbook(file)
    sheet =workbook .active

    data = sheet.values
    row = next(data)[1:]
    data = list(data)
    return data

if __name__ =='__main__':
    print(exel('test.xlsx'))


