import os
import os.path
import win32com.client as win32
import openpyxl
rootdir = r"C:\Users\Admin\Desktop\1"
for parent,dirnames,filenames in os.walk(rootdir):
    # print(parent,dirnames,filenames)
    for fn in filenames:
        # print(parent,dirnames,filenames)
        filedir = os.path.join(parent,fn)
        print(filedir)
        if filedir.split(".")[1] == "xls":
            excel = win32.gencache.EnsureDispatch("Excel.Application")
            # print(type(excel))
            wb = excel.Workbooks.Open(filedir)
            wb.SaveAs(filedir.replace("xls","xlsx"),FileFormat=51)
            wb.Close()
            excel.Application.Quit()
            os.remove(filedir)
os.chdir(rootdir)
for file in os.listdir(rootdir):
    # print(os.getcwd())

    # print(file)
    open_file = openpyxl.load_workbook(file)
    print(open_file.sheetnames)
    one = open_file["支部数据"]
    print(len(list(one.rows)))
    for each in one.rows:
        for each_v in each:
            eachlist = []
            eachlist.append(each_v)
            one.append(eachlist)
    # new = open_file.copy_worksheet(one)
    open_file.save("heping2.xlsx")


