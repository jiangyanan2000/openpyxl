import openpyxl
import os
import os.path
import win32com.client as win32
import openpyxl
rootdir = input("输入文件夹路径：")
for parent,dirnames,filenames in os.walk(rootdir):
    # print(parent,dirnames,filenames)
    for fn in filenames:
        # print(parent,dirnames,filenames)
        filedir = os.path.join(parent,fn)
        # print(filedir)
        if filedir.split(".")[1] == "xls":
            excel = win32.gencache.EnsureDispatch("Excel.Application")
            # print(type(excel))
            wb = excel.Workbooks.Open(filedir)
            wb.SaveAs(filedir.replace("xls","xlsx"),FileFormat=51)
            wb.Close()
            excel.Application.Quit()
            os.remove(filedir)
            # print(wb)

for parent_new,dirnames_new,filenames_new in os.walk(rootdir):
    for fn_new in filenames_new:

        filedir_new = os.path.join(parent_new,fn_new)
        wb = openpyxl.load_workbook(filedir_new)
        ws = wb["支部数据"]
        ws["K1"] = "激活学员"
        maxrow = ws.max_row
        for each_rows in ws.rows:
            for each_row in each_rows:
                # print(each_row.value)
                # each_row.number_format = "NUMBER"
                if "%" in str(each_row.value) :
                    each_row.value = float(each_row.value.split("%")[0])/100
                elif str(each_row.value).isdigit():
                    each_row.value = int(each_row.value)
                elif "." in str(each_row.value) and not isinstance(each_row,float):
                    each_row.value = float(each_row.value)
            for rows in ws.iter_rows(min_col=3,min_row=2,max_col=11,max_row= maxrow):
                ws[rows[8].coordinate] = f"=SUM({rows[1].coordinate}:{rows[2].coordinate})"
            for cols in ws.iter_cols(min_col=3,min_row=2,max_col=11,max_row = (maxrow+1)):
                # print(cols)
                ws[cols[(maxrow-1)].coordinate] = f"=SUM({cols[0].coordinate}:{cols[(maxrow-2)].coordinate})"


            # each_row.number_format = "FORMAT_GENERAL"
            # print(each_row.value)

        wb.save(filedir_new)