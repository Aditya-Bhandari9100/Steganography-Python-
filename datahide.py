from tkinter import *
from tkinter import filedialog
import tkinter as tk 
from PIL import Image, ImageTk 
import os
from stegano import lsb 

root = Tk()
root.title("Steganography - Hide a Secret Message in an Image")
root.geometry("800x600+150+100")
root.resizable(False, False)
root.configure(bg="#1e1e1e")

def showimage():
    global filename
    filename = filedialog.askopenfilename(initialdir=os.getcwd(),
                                          title="Select Image File",
                                          filetype=(("PNG File","*.png"),("JPG File","*.jpg"),("All File","*.txt"))
                                          )
    
    img = Image.open(filename)
    img = ImageTk.PhotoImage(img)
    lbl.configure(image=img, width=300, height=300)
    lbl.image = img

def Hide():
    global secret 
    message = text1.get(1.0, END)
    secret = lsb.hide(str(filename), message)

def Show():
    clear_message = lsb.reveal(filename)
    text1.delete(1.0, END)
    text1.insert(END, clear_message)

def save():
    secret.save("hidden.png")

image_icon = PhotoImage(file="logo.jpg")
root.iconphoto(False, image_icon)

# 1st Frame 
f = Frame(root, bd=3, bg="#4e4e4e", width=360, height=320, relief=GROOVE)
f.place(x=20, y=80)

lbl = Label(f, bg="#4e4e4e")
lbl.place(x=30, y=10)

# 2nd Frame 
frame2 = Frame(root, bd=3, width=360, height=320, bg="white", relief=GROOVE)
frame2.place(x=400, y=80)

text1 = Text(frame2, font=("Helvetica", 16), bg="#f5f5f5", fg="#333333", relief=GROOVE, wrap=WORD)
text1.place(x=0, y=0, width=340, height=295)

scrollbar1 = Scrollbar(frame2)
scrollbar1.place(x=340, y=0, height=300)
scrollbar1.configure(command=text1.yview)
text1.configure(yscrollcommand=scrollbar1.set)

# 3rd Frame - Buttons for Image Operations
frame3 = Frame(root, bd=3, bg="#333333", width=360, height=100, relief=GROOVE)
frame3.place(x=20, y=420)

Button(frame3, text="Open Image", width=12, height=2, font=("Helvetica", 12, "bold"), bg="#ffcc00", fg="black", command=showimage).place(x=20, y=30)
Button(frame3, text="Save Image", width=12, height=2, font=("Helvetica", 12, "bold"), bg="#ffcc00", fg="black", command=save).place(x=200, y=30)
Label(frame3, text="Image Operations", bg="#333333", fg="white", font=("Helvetica", 10, "bold")).place(x=120, y=5)

# 4th Frame - Buttons for Data Operations
frame4 = Frame(root, bd=3, bg="#333333", width=360, height=100, relief=GROOVE)
frame4.place(x=400, y=420)

Button(frame4, text="Hide Data", width=12, height=2, font=("Helvetica", 12, "bold"), bg="#ff6600", fg="white", command=Hide).place(x=20, y=30)
Button(frame4, text="Show Data", width=12, height=2, font=("Helvetica", 12, "bold"), bg="#ff6600", fg="white", command=Show).place(x=200, y=30)
Label(frame4, text="Data Operations", bg="#333333", fg="white", font=("Helvetica", 10, "bold")).place(x=120, y=5)

# Title Label
title_label = Label(root, text="Steganography - Hide a Secret Message in an Image", bg="#1e1e1e", fg="white", font=("Helvetica", 18, "bold"))
title_label.pack(pady=20)

root.mainloop()
