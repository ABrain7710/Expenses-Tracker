import xlsxwriter

# Create a workbook and add a worksheet.
workbook = xlsxwriter.Workbook('budget_tracking.xlsx')

months = [ 'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

for month in months:
    worksheet = workbook.add_worksheet(month)
    row = 0
    col = 0

    inital_columns = ['Item', 'Cost', 'Main Category', 'Specific Category']

    for column in inital_columns:
        worksheet.write(row, col, column)
        col += 1

workbook.close()
