import os
import shutil

def check_dir(input_path):
    try:
        for directory in directories:
            path = os.path.join(input_path, directory)
            os.makedirs(path)
    except FileExistsError as err:
        pass

def folders(name):
    if os.path.exists(input_path + '/' + name):
            shutil.move(input_path + '/' + file, input_path + '/' + name + '/' + file)
    else:
        os.makedirs(input_path + '/' + name)
        shutil.move(input_path + '/' + file, input_path + '/' + name + '/' + file)

input_path = input("Enter path : ")

directories = ["Images", "Audio", "Videos", "Documents", "Archives", "Programs", "Others"]

images = ["jpg", "jpeg", "png", "pjp", "pjpeg", "avif", "gif", "svg", "webp", "apng", "bmp", "ico", "cur", "tiff", "tif"]
programs = ["exe","apk","msi"]
archives = ["rar", "zip", "iso"]
docs = ["doc", "txt", "xls", "ppt", "ppt", "pdf", "pptx", "xlsx", "docx"]
audio = ["mp3", "wav", "aac"]
video = ["mp4", "mkv"]

files = os.listdir(input_path)

check_dir(input_path)

try:
    for file in files:

        if os.path.isfile(input_path+'/'+file):
            file_name, extension = os.path.splitext(file)
            extension = extension[1:]

            if extension in images:
                folders("Images")
            elif extension in audio:
                folders("Audio")
            elif extension in video:
                folders("Videos")
            elif extension in archives:
                folders("Archives")
            elif extension in programs:
                folders("Programs")
            elif extension in docs:
                folders("Documents")
            else:
                folders("Others")

except Exception as err:
    print(err)

