from distutils import extension
import os
import shutil

start = "F://"
send = "Document_Files" 

listOfFiles = os.listdir(start)
print(listOfFiles)

for file_name in listOfFiles:
    name, extension = os.path.splitext(file_name)

    if extension == '':
        continue
    if extension in [ '.txt', '.doc', '.docx', '.pdf']:
        path1 = start+'/'+file_name
        path2 = send + '/' + "Document_Files"
        path3 = send + '/' + "Document_Files" + '/' + file_name

        if os.path.exists(path2):
            print("Moving " + file_name + ".....")
            shutil.move(path1,path3)

        else:
            os.makedirs(path2)
            print("Moving " + file_name + ".....")
            shutil.move(path1,path3)

