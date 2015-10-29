import os, shutil, datetime

desktop_path = os.path.expanduser('~') + '/Desktop/'
folder_path = os.path.join(desktop_path, str(datetime.datetime.now().strftime('%Y-%m-%d')))
os.makedirs(folder_path)
files_on_desktop = os.listdir(desktop_path)

for file in files_on_desktop:
    if file.endswith('jpg') is True:
	shutil.move(desktop_path + file, folder_path)
	
 # 这段代码的功能是把所有桌面或指定目录下所有的的.jpg文件存到一个以当前日期为名字的文件夹里
 # 当然，由于没加判断，这里要是已经有那个文件夹的话就会报错，加完判断的代码在desktop_file_archiving_ii.py里
