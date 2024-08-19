from tkinter import *
from PIL import ImageTk,Image
import pymysql
from tkinter import messagebox
from add import *
from delete import *
from view import *
from issue import *
from Return import *

cnx = pymysql.connect(host="localhost",user="root",password="12345",database="lib")
cur = cnx.cursor()

window = Tk()
window.title("LMS")
window.minsize(width=400,height=400)
window.geometry("600x500")

bg =Image.open("library.jpg")
[img_width, img_height] = bg.size
newImgwidth = int(img_width*2)
newImgheight = int(img_height*2) 

def Quit() : 
    quit()

bg2 = bg.resize((newImgwidth,newImgheight))
img = ImageTk.PhotoImage(bg2)

Canvas1 = Canvas(window)
Canvas1.create_image(300,340,image = img)      
Canvas1.config(bg="white",width = newImgwidth, height = newImgheight)
Canvas1.pack(expand=True,fill=BOTH)

hFrame1 = Frame(window,bg="#000000",bd=5)
hFrame1.place(relx=0.2,rely=0.1,relwidth=0.6,relheight=0.16)
hLabel = Label(hFrame1, text="Welcome to \n Nitte Library", bg='gray', fg='black', font=('Calibri',15))
hLabel.place(relx=0.001,rely=0, relwidth=1, relheight=1)

btn1 = Button(window,text="Add Book Details",bg='gray', fg='black', command=add)
btn1.place(relx=0.28,rely=0.3, relwidth=0.45,relheight=0.1)

btn2 = Button(window,text="Delete Book",bg='gray', fg='black', command=Delete)
btn2.place(relx=0.28,rely=0.4, relwidth=0.45,relheight=0.1)

btn3 = Button(window,text="View Book List",bg='gray', fg='black', command=View)
btn3.place(relx=0.28,rely=0.5, relwidth=0.45,relheight=0.1)

btn4 = Button(window,text="Issue Book to Student",bg='gray', fg='black', command = Issue)
btn4.place(relx=0.28,rely=0.6, relwidth=0.45,relheight=0.1)

btn5 = Button(window,text="Return Book",bg='gray', fg='black', command = returnBook)
btn5.place(relx=0.28,rely=0.7, relwidth=0.45,relheight=0.1)

btn6 = Button(window,text="Quit",bg='gray', fg='black', command = Quit)
btn6.place(relx=0.35,rely=0.9, relwidth=0.30,relheight=0.05)

#window.resizable(False,False)
window.mainloop()