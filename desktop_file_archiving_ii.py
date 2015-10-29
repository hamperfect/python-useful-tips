import os, shutil, datetime

desktop_path = os.path.expanduser('~') + '/Desktop/'
doc_folder_path = os.path.join(desktop_path + 'Doc/')
pic_folder_path = os.path.join(desktop_path + 'Pic/')
if not os.path.exists(doc_folder_path):
	os.makedirs(doc_folder_path)
if not os.path.exists(pic_folder_path):
	os.makedirs(pic_folder_path)
files_on_desktop = os.listdir(desktop_path)

for file in files_on_desktop:
    if file.endswith('jpg') is True or file.endswith('jpeg') is True or file.endswith('png') is True or file.endswith('bmp') is True:
    	shutil.move(desktop_path + file, pic_folder_path)

    if file.endswith('doc') is True or file.endswith('docx') is True or file.endswith('xls') is True or file.endswith('xlsx') is True or file.endswith('pdf') is True:
    	shutil.move(desktop_path + file, doc_folder_path)
    	
  # 这段代码的功能是能把桌面上，或者是os里面任何地方的图片类文件和文档类文件分别放到Doc文件夹和Pic文件夹中
  # 加了一个判断os.path.exists(path)，可以在已有目录的情况下不报错，同时没有目录的时候新创建目录
