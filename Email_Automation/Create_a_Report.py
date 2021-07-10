#!/usr/bin/env python3

import os
import datetime
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, Image
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
from reportlab.graphics.shapes import Drawing
from reportlab.graphics.charts.piecharts import Pie

"""Test python report pdf functionality"""

def main():
    source = os.path.join(os.path.expanduser("~"), "data") #USer home plus path
    #source = os.path.join(os.path.expanduser("~"), "data") #absolute path linux beginning with root
    dat_now = datetime.datetime.now().strftime("%B_%d_%Y-%H-%M-%S")
    report_name= f"Report_{dat_now}.pdf"
    pdf_path=(os.path.join(source, report_name))
    print(pdf_path)
    dict_with_data = {
        "elderberries": 1,
        "figs": 1,
        "apples": 2,
        "durians": 3,
        "bananas": 5,
        "cherries": 8,
        "grapes": 13        
    }
    report = SimpleDocTemplate(pdf_path)
    styles = getSampleStyleSheet()
    report_title = Paragraph("A Complete Inventory of My Fruit", styles["h1"])
    table_data = []
    for k, v in dict_with_data.items():
        table_data.append([k, v])
    table_style = [('GRID', (0,0), (-1,-1), 1, colors.black)]
    report_table = Table(data=table_data, style=table_style, hAlign="LEFT")
    report_pie = Pie(width=3, height=3)
    report_pie.data = []
    report_pie.labels = []
    for data_name in sorted(dict_with_data):
        report_pie.data.append(dict_with_data[data_name])
        report_pie.labels.append(data_name)
    report_chart = Drawing()
    report_chart.add(report_pie)
    report.build([report_title, report_table, report_chart])
    

if __name__ == "__main__":
    main()