import openpyxl
wb = openpyxl.load_workbook(r"C:\Users\Admin\Desktop\1\和平社区.xlsx")
ws = wb["支部数据"]
for each_rows in ws.rows:
    for each_row in each_rows:
        print(each_row.value)
        # each_row.number_format = "NUMBER"
        if "%" in each_row.value and not isinstance(each_row,float):
            each_row.value = float(each_row.value.split("%")[0])/100
        elif each_row.value.isdigit():
            each_row.value = int(each_row.value)
        elif "." in each_row.value and not isinstance(each_row,float):
            each_row.value = float(each_row.value)

        # each_row.number_format = "FORMAT_GENERAL"
        # print(each_row.value)
wb.save(r"C:\Users\Admin\Desktop\1\和平社区.xlsx")