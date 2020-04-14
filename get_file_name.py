import os
def get_file_name(rootdir):

    file_list = []
    for parent_new, dirnames_new, filenames_new in os.walk(rootdir):
        for fn_new in filenames_new:
            filedir_new = os.path.join(parent_new, fn_new)
            file_list.append(filedir_new)
    return file_list

rootdir = input("输入文件夹地址：")
get_file_name(rootdir)
print(get_file_name(rootdir))
