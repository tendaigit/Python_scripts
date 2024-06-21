#!/usr/bin/env python3
# ReportLab module
# Using SimpleDocTemplate class to build a pdf
# using the high-level classes and methods in the Page Layout and
# Typography Using Scripts (PLATYPUS) part of the ReportLab module.

#Data
fruit = {
  "elderberries": 1,
  "figs": 1,
  "apples": 2,
  "durians": 3,
  "bananas": 5,
  "cherries": 8,
  "grapes": 13
}

from reportlab.platypus import SimpleDocTemplate
report = SimpleDocTemplate("/tmp/report.pdf")
#Using Flowables to create titles, Paragraphs and charts
from reportlab.platypus import Paragraph, Spacer, Table, Image

#(Paragraph, Spacer, Table, and Image) are classes that build individual
#elements in the final document.

#tell reportlab what style we want each part of the document to have
from reportlab.lib.styles import getSampleStyleSheet
styles = getSampleStyleSheet()
report_title = Paragraph("A Complete Inventory of My Fruits", styles["h1"])

#build the PDF now by using the build() method of our report
report.build([report_title])

#adding a Table
#convert Data from a dic to list-of-lists (two-dimensional array)
table_data = []
for k, v in fruit.items():
   table_data.append([k, v])

print(table_data)

#add list-of-lists to our report and then generate the PDF file
report_table = Table(data=table_data)
report.build([report_title, report_table])

#styling the table
from reportlab.lib import colors

table_style = [('GRID', (0,0), (-1,-1), 1, colors.black)]
report_table = Table(data=table_data, style=table_style, hAlign="LEFT")
report.build([report_title, report_table])

# use the Drawing Flowable class to create a Pie chart.
from reportlab.graphics.shapes import Drawing
from reportlab.graphics.charts.piecharts import Pie

report_pie = Pie(width=3, height=3)

#two separate lists to add data to the piechat:One for data, and one for labels.
report_pie.data = []
report_pie.labels = []

#sort fruits in alphabetical order
for fruit_name in sorted(fruit):
    #append to the two lists
    report_pie.data.append(fruit[fruit_name])
    report_pie.labels.append(fruit_name)

print(report_pie.data)
print(report_pie.labels)

#Place Pie object inside of a Flowable Drawing.
report_chart = Drawing()
report_chart.add(report_pie)

#add the new Drawing to the report
report.build([report_title, report_table, report_chart])
