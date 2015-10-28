import os, shutil, datetime

desktop_path = os.path.expanduser('~') + '/Desktop/'
folder_path = os.path.join(desktop_path, str(datetime.datetime.now().strftime('%Y-%m-%d')))
os.makedirs(folder_path)
files_on_desktop = os.listdir(desktop_path)

for file in files_on_desktop:
    if file.endswith('jpg') is True:
	shutil.move(desktop_path + file, folder_path)
