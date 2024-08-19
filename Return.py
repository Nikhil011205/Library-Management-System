from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import pymysql

cnx = pymysql.connect(host="localhost",user="root",password="12345",database="lib")
cur = cnx.cursor()

issueTable = "issue" 
bookTable = "booklist" 

allbid = [] 

def Return():
    
    global SubmitBtn,labelFrame,lb1,bookInfo1,quitBtn,root,Canvas1,status
    
    bid = bookInfo1.get()
    extractBid = "select ID from "+issueTable
    try:
        cur.execute(extractBid)
        cnx.commit()
        for i in cur:
            allbid.append(i[0])
        if bid in allbid:
            checkAvail = "select status from "+bookTable+" where ID = '"+bid+"'"
            cur.execute(checkAvail)
            cnx.commit()
            for i in cur:
                check = i[0]
            if check == 'issued':
                status = True
            else:
                status = False

        else:
            messagebox.showinfo("Error","Book ID not present")
    except:
        messagebox.showinfo("Error","Can't fetch Book IDs")
    
    issueSql = "delete from "+issueTable+" where ID = '"+bid+"'"

    updateStatus = "update "+bookTable+" set status = 'avail' where ID = '"+bid+"'"
    try:
        if bid in allbid and status == True:
            cur.execute(issueSql)
            cnx.commit()
            cur.execute(updateStatus)
            cnx.commit()
            messagebox.showinfo('Success',"Book Returned Successfully")
        else:
            allbid.clear()
            messagebox.showinfo('Message',"Please check the book ID")
            window.destroy()
            return
    except:
        messagebox.showinfo("Search Error","The value entered is wrong, Try again")
        
    allbid.clear()
    window.destroy()
def returnBook(): 
    
    global bookInfo1,SubmitBtn,quitBtn,Canvas1,cnx,cur,window,labelFrame, lb1
    
    window = Tk()
    window.title("Library")
    window.minsize(width=400,height=400)
    window.geometry("600x500")

    
    Canvas1 = Canvas(window)
    
    Canvas1.config(bg="#b0335a")
    Canvas1.pack(expand=True,fill=BOTH)
        
    hFrame1 = Frame(window,bg="#d34524",bd=5)
    hFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)
        
    headingLabel = Label(hFrame1, text="Return Book", bg='black', fg='white', font=('Courier',15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
    
    labelFrame = Frame(window,bg='black')
    labelFrame.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.5)   
    
    lb1 = Label(labelFrame,text="Book ID : ", bg='black', fg='white')
    lb1.place(relx=0.05,rely=0.5)
        
    bookInfo1 = Entry(labelFrame)
    bookInfo1.place(relx=0.3,rely=0.5, relwidth=0.62)
    
    SubmitBtn = Button(window,text="Return",bg='#d1ccc0', fg='black',command=Return)
    SubmitBtn.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)
    
    quitBtn = Button(window,text="Quit",bg='#f7f1e3', fg='black', command=window.destroy)
    quitBtn.place(relx=0.53,rely=0.9, relwidth=0.18,relheight=0.08)
    #window.resizable(False,False)
    window.mainloop()