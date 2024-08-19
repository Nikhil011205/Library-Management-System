from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import pymysql

cnx = pymysql.connect(host="localhost",user="root",password="12345",database="lib")
cur = cnx.cursor()
issueTable = "booklist" 
bookTable = "issue"

def delete():
    bid = bookInfo1.get()    
    deleteSql = "delete from "+bookTable+" where ID = '"+bid+"'"
    deleteIssue = "delete from "+issueTable+" where ID = '"+bid+"'"
    try:
        cur.execute(deleteSql)
        cnx.commit()
        cur.execute(deleteIssue)
        cnx.commit()
        messagebox.showinfo('Success',"Book Record Deleted")
    except:
        messagebox.showinfo("Please check Book ID")
    bookInfo1.delete(0, END)
    window.destroy()
def Delete(): 
    
    global bookInfo1,bookInfo2,bookInfo3,bookInfo4,Canvas1,cnx,cur,bookTable,window
    
    window = Tk()
    window.title("Library")
    window.minsize(width=400,height=400)
    window.geometry("600x500")
    Canvas1 = Canvas(window)
    
    Canvas1.config(bg="#006B38")
    Canvas1.pack(expand=True,fill=BOTH)
        
    hFrame1 = Frame(window,bg="#FFBB00",bd=5)
    hFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)
    
    hLabel = Label(hFrame1, text="Delete Book", bg='black', fg='white', font=('Courier',15))
    hLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
    
    lFrame = Frame(window,bg='black')
    lFrame.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.5)   
        
    lb2 = Label(lFrame,text="Book ID : ", bg='black', fg='white')
    lb2.place(relx=0.05,rely=0.5)
        
    bookInfo1 = Entry(lFrame)
    bookInfo1.place(relx=0.3,rely=0.5, relwidth=0.62)
    
    SubmitBtn = Button(window,text="SUBMIT",bg='#d1ccc0', fg='black',command=delete)
    SubmitBtn.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)
    
    quitBtn = Button(window,text="Quit",bg='#f7f1e3', fg='black', command=window.destroy)
    quitBtn.place(relx=0.53,rely=0.9, relwidth=0.18,relheight=0.08)
    #window.resizable(False,False)
    window.mainloop()