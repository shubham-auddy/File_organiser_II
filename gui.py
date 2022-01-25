import tkinter as tk
import os
import shutil

# FUNCTIONS
def check_dir(input_path):
    try:
        for directory in directories:
            path = os.path.join(input_path, directory)
            os.makedirs(path)
    except FileExistsError as err:
        pass

def folders(name,file,input_path):
    if os.path.exists(input_path + '/' + name):
            shutil.move(input_path + '/' + file, input_path + '/' + name + '/' + file)
    else:
        os.makedirs(input_path + '/' + name)
        shutil.move(input_path + '/' + file, input_path + '/' + name + '/' + file)

def oragnise():
    input_path = path.get()
    try:
        files = os.listdir(input_path)
        check_dir(input_path)
        for file in files:

            if os.path.isfile(input_path+'/'+file):
                file_name, extension = os.path.splitext(file)
                extension = extension[1:]

                if extension in images:
                    folders("Images",file,input_path)
                elif extension in audio:
                    folders("Audio",file,input_path)
                elif extension in video:
                    folders("Videos",file,input_path)
                elif extension in archives:
                    folders("Archives",file,input_path)
                elif extension in programs:
                    folders("Programs",file,input_path)
                elif extension in docs:
                    folders("Documents",file,input_path)
                else:
                    folders("Others",file,input_path)

    except Exception as err:
        pass

#GUI
app = tk.Tk()
app.geometry('400x100')
app.minsize(400,130)
app.maxsize(400,130)
app.resizable(0,0)
app.title("File Organizer II")

label1 = tk.Label(app, text = "Enter the path below :", width=20, height=3)
label1.pack()

path  = tk.Entry(app, width = 50 )
path.pack()

btn = tk.Button(app, text = "Organise", command = oragnise)
btn.pack(pady = 15)

# DATA

directories = ["Images", "Audio", "Videos", "Documents", "Archives", "Programs", "Others"]

images = ["jpg", "jpeg", "png", "pjp", "pjpeg", "avif", "gif", "svg", "webp", "apng", "bmp", "ico", "cur", "tiff", "tif"]
programs = ["exe","apk","msi"]
archives = ["rar", "zip", "iso"]
docs = ["doc", "txt", "xls", "ppt", "ppt", "pdf", "pptx", "xlsx", "docx"]
audio = ["mp3", "wav", "aac"]
video = ["mp4", "mkv"]

app.mainloop()
