from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import pymysql

cnx = pymysql.connect(host="localhost",user="root",password="12345",database="lib")
cur = cnx.cursor()

bookTable = "booklist" 
    
def View(): 
    
    window = Tk()
    window.title("Library")
    window.minsize(width=400,height=400)
    window.geometry("600x500")


    Canvas1 = Canvas(window) 
    Canvas1.config(bg="#6a6277")
    Canvas1.pack(expand=True,fill=BOTH)
        
        
    hFrame1 = Frame(window,bg="#502adb",bd=5)
    hFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)
        
    hLabel = Label(hFrame1, text="View Books", bg='black', fg='white', font=('Courier',15))
    hLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
    
    lFrame = Frame(window,bg='black')
    lFrame.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.5)
    y = 0.25
    
    Label(lFrame, text="%-10s%-40s%-30s%-20s"%('BID','Title','Author','Status'),bg='black',fg='white').place(relx=0.07,rely=0.1)
    Label(lFrame, text="----------------------------------------------------------------------------",bg='black',fg='white').place(relx=0.05,rely=0.2)
    getBooks = "select * from "+bookTable
    try:
        cur.execute(getBooks)
        cnx.commit()
        for i in cur:
            Label(lFrame, text="%-10s%-30s%-30s%-20s"%(i[0],i[1],i[2],i[3]),bg='black',fg='white').place(relx=0.07,rely=y)
            y += 0.1
    except:
        messagebox.showinfo("Failed to fetch files from database")
    
    quitBtn = Button(window,text="Quit",bg='#f7f1e3', fg='black', command=window.destroy)
    quitBtn.place(relx=0.4,rely=0.9, relwidth=0.18,relheight=0.08)
    #window.resizable(False,False)
    window.mainloop()