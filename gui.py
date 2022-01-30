import tkinter as tk
import utility

def clicked():
    utility.organise(path.get())
    
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

btn = tk.Button(app, text = "Organise", command = clicked)
btn.pack(pady = 15)

app.mainloop()
