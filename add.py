from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import pymysql

def Register():
    
    bid = bookInfo1.get()
    title = bookInfo2.get()
    author = bookInfo3.get()
    status = bookInfo4.get()
    status = status.lower()
    
    insertBooks = "insert into "+bookTable+" values('"+bid+"','"+title+"','"+author+"','"+status+"')"
    try:
        cur.execute(insertBooks)
        cnx.commit()
        messagebox.showinfo('Success',"Book added")
    except:
        messagebox.showinfo("Error","Error")
    window.destroy()
def add(): 
    global bookInfo1,bookInfo2,bookInfo3,bookInfo4,Canvas1,cnx,cur,bookTable,window
    window = Tk()
    window.title("Library")
    window.minsize(width=400,height=400)
    window.geometry("600x500")
    cnx = pymysql.connect(host="localhost",user="root",password="12345",database="lib")
    cur = cnx.cursor()
    bookTable = "booklist"

    Canvas1 = Canvas(window)
    Canvas1.config(bg="#5dd02d")
    Canvas1.pack(expand=True,fill=BOTH)
        
    headingFrame1 = Frame(window,bg="#ff7b2d",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)

    headingLabel = Label(headingFrame1, text="Add Books", bg='black', fg='white', font=('Courier',15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)


    labelFrame = Frame(window,bg='black')
    labelFrame.place(relx=0.1,rely=0.4,relwidth=0.8,relheight=0.4)
    
    lb1 = Label(labelFrame,text="Book ID : ", bg='black', fg='white')
    lb1.place(relx=0.05,rely=0.2, relheight=0.08)
        
    bookInfo1 = Entry(labelFrame)
    bookInfo1.place(relx=0.3,rely=0.2, relwidth=0.62, relheight=0.08)
        
    lb2 = Label(labelFrame,text="Title : ", bg='black', fg='white')
    lb2.place(relx=0.05,rely=0.35, relheight=0.08)
        
    bookInfo2 = Entry(labelFrame)
    bookInfo2.place(relx=0.3,rely=0.35, relwidth=0.62, relheight=0.08)
    
    lb3 = Label(labelFrame,text="Author : ", bg='black', fg='white')
    lb3.place(relx=0.05,rely=0.50, relheight=0.08)
        
    bookInfo3 = Entry(labelFrame)
    bookInfo3.place(relx=0.3,rely=0.50, relwidth=0.62, relheight=0.08)

    lb4 = Label(labelFrame,text="Status(Avail/issued) : ", bg='black', fg='white')
    lb4.place(relx=0.05,rely=0.65, relheight=0.08)
        
    bookInfo4 = Entry(labelFrame)
    bookInfo4.place(relx=0.3,rely=0.65, relwidth=0.62, relheight=0.08)
        
    SubmitBtn = Button(window,text="SUBMIT",bg='#d1ccc0', fg='black',command=Register)
    SubmitBtn.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)
    
    quitBtn = Button(window,text="Quit",bg='#f7f1e3', fg='black', command=window.destroy)
    quitBtn.place(relx=0.53,rely=0.9, relwidth=0.18,relheight=0.08)
    #window.resizable(False,False)
    window.mainloop()