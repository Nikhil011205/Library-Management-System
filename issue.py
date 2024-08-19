from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import pymysql
cnx = pymysql.connect(host="localhost",user="root",password="12345",database="lib")
cur = cnx.cursor()
issueTable = "issue" 
bookTable = "booklist"
allBid = [] 
def issue():
    global issueBtn,lFrame,lb1,inf1,inf2,quitBtn,root,Canvas1,status
    bid = inf1.get()
    issueto = inf2.get()
    issueBtn.destroy()
    lFrame.destroy()
    lb1.destroy()
    inf1.destroy()
    inf2.destroy()
    extractBid = "select ID from "+bookTable
    try:
        cur.execute(extractBid)
        cnx.commit()
        for i in cur:
            allBid.append(i[0])
        if bid in allBid:
            checkAvail = "select status from "+bookTable+" where ID = '"+bid+"'"
            cur.execute(checkAvail)
            cnx.commit()
            for i in cur:
                check = i[0]
            if check == 'avail':
                status = True
            else:
                status = False
        else:
            messagebox.showinfo("Error","Book ID not present")
    except:
        messagebox.showinfo("Error","Can't fetch Book IDs")
    issueSql = "insert into "+issueTable+" values ('"+bid+"','"+issueto+"')"
    show = "select * from "+issueTable
    updateStatus = "update "+bookTable+" set status = 'issued' where ID = '"+bid+"'"
    try:
        if bid in allBid and status == True:
            cur.execute(issueSql)
            cnx.commit()
            cur.execute(updateStatus)
            cnx.commit()
            messagebox.showinfo('Success',"Book Issued")
            window.destroy()
        else:
            allBid.clear()
            messagebox.showinfo('Message',"Book Already Issued")
            window.destroy()
            return
    except:
        messagebox.showinfo("Search Error","value error")
    
    allBid.clear()
    
def Issue(): 
    
    global issueBtn,lFrame,lb1,inf1,inf2,quitBtn,window,Canvas1,status
    
    window = Tk()
    window.title("Library")
    window.minsize(width=400,height=400)
    window.geometry("600x500")
    
    Canvas1 = Canvas(window)
    Canvas1.config(bg="#5dd09b")
    Canvas1.pack(expand=True,fill=BOTH)

    hFrame1 = Frame(window,bg="#FFBB00",bd=5)
    hFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)
        
    hLabel = Label(hFrame1, text="Issue Book", bg='black', fg='white', font=('Courier',15))
    hLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
    
    lFrame = Frame(window,bg='black')
    lFrame.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.5)  
        
    lb1 = Label(lFrame,text="Book ID : ", bg='black', fg='white')
    lb1.place(relx=0.05,rely=0.2)
        
    inf1 = Entry(lFrame)
    inf1.place(relx=0.3,rely=0.2, relwidth=0.62)
    
    lb2 = Label(lFrame,text="Issued To : ", bg='black', fg='white')
    lb2.place(relx=0.05,rely=0.4)
        
    inf2 = Entry(lFrame)
    inf2.place(relx=0.3,rely=0.4, relwidth=0.62)
    
    issueBtn = Button(window,text="Issue",bg='#d1ccc0', fg='black',command=issue)
    issueBtn.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)
    
    quitBtn = Button(window,text="Quit",bg='#aaa69d', fg='black', command=window.destroy)
    quitBtn.place(relx=0.53,rely=0.9, relwidth=0.18,relheight=0.08)
    #window.resizable(False,False)
    window.mainloop()