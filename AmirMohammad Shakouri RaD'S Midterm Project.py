
#Amir Mohammad Shakouri Rad

# MESSAGE TO OSTAD:
    
    # Ostad azunja ke ye shop e farzie in
    # va shoma tu class ta jayi az projecto ke kamel kardim 
    # Harfi az optione BUY nazadin o tuye surat masaleye soale
    # mianterm ham nagoftin ke option buy ro ezafe konim pas
    # man hadsam ine ke mikhastin in shope farzio bezanim o
    # bebinin ke mitunim chizayi ke goftino amali konim ta karbar
    # masaln shoma bebine outcome esho ya na,
    # option buy ro ezafe nkrdm
    # ke omidvarm hadsam dorost bude bashe :(
    # chon alan ke daram projecto tamum mikonam jomasto 
    # rahi nist azatun beporsam
    # va tahe project sare ezafe kardane date yade buy oftdm ke age ezafe mikrdm
    # bayad kheyli chizaro avaz mikrdm ke dg time eii ta saat 12 e shb nmunde
    # ke mirim tu shanbe o ta qablesh byd projecto upload konm







import tkinter
import sqlite3



cnt=sqlite3.connect("myshop.db")
print("connect to database")

#------------------------ create users table -------------


# query='''CREATE TABLE products
# ( ID INTEGER PRIMARY KEY,
# name CHAR(20) NOT NULL,
# price int NOT NULL,
# qnt int NOT NULL,
# comment TEXT)'''

# cnt.execute(query)
# cnt.close()

#-------- int products table -------------------
#query='''INSERT INTO products (name,price,qnt)
#VALUES ('Microphones','55000','0') '''

#cnt.execute(query)
#cnt.commit()
#cnt.close()
#----------------- int users table -----------
# query='''INSERT INTO users (user,pw,addr)
# VALUES ('admin','123456789','rasht') '''

# cnt.execute(query)
# cnt.commit()
# cnt.close()

#-----------------Adding a column--------------

#cnt.execute("ALTER TABLE products ADD COLUMN dates TEXT")

#----------------- FUNCTIONS --------------

def login():
    user=user_txt.get()
    pw=pw_txt.get()
    
    if user=="" or pw=="":    #if len(user)==0 or len(pw)==0:
        msg_lbl.configure(text="Fill in the info !!!",fg="red")
        return
    if user=="admin" and pw=="123456789":
        msg_lbl.configure(text="Welcome ADMN <3",fg="orange")
        adminpanel_btn.configure(state="active")
    
    
    query=''' SELECT user,pw FROM users WHERE user=? AND pw=? '''
    result=cnt.execute(query,(user,pw))
    rows=result.fetchall()
    if len(rows)==0:
        msg_lbl.configure(text="wrong info!",fg="red")
        return

    else:
        msg_lbl.configure(text="welcome to ur account <3",fg="green")
        user_txt.delete(0,"end")
        pw_txt.delete(0,"end")
        login_btn.configure(state="disabled")
        submit_btn.configure(state="disabled")
        logout_btn.configure(state="active")
        shop_btn.configure(state="active")
        
        
def logout():
    login_btn.configure(state="active")
    logout_btn.configure(state="disabled")
    adminpanel_btn.configure(state="disabled")
    shop_btn.configure(state="disabled")
    msg_lbl.configure(text="you are logged out!",fg="green")
    
    
    
    
def final_submit():
    user=user1_txt.get()
    pw=pw1_txt.get()
    addr=addr1_txt.get()
    
        
    
    #------ Validation ------
    
    if user=="" or pw=="" or addr=="":
        msg1_lbl.configure(text="fill all the blanks!",fg="red")
        
    if len(pw)<8:
        msg1_lbl.configure(text="password is too short!!",fg="red")
        
    query='''SELECT id FROM users WHERE user=? '''
    result=cnt.execute(query,(user,))
    rows=result.fetchall()
    if len(rows)!=0:
        msg1_lbl.configure(text="username already exists!!",fg="red")
        return
    
    
    query='''INSERT INTO users (user,pw,addr)
          VALUES (?,?,?)'''
    
    cnt.execute(query,(user,pw,addr))
    cnt.commit()
    msg1_lbl.configure(text="SUBMIT is done <3",fg="green")
    
    user1_txt.delete(0,"end")
    pw1_txt.delete(0,"end")
    addr1_txt.delete(0,"end")                    
    
    
    
def submit():
    global user1_txt,pw1_txt,addr1_txt,msg1_lbl
    
    win_submit=tkinter.Toplevel(win)
    win_submit.title("Submit")
    win_submit.geometry("200x200")
    
    #-------------------widgets--------------
    user1_lbl=tkinter.Label(win_submit,text="username: ")
    user1_lbl.pack()
    user1_txt=tkinter.Entry(win_submit,width=20)
    user1_txt.pack()

    pw1_lbl=tkinter.Label(win_submit,text="password: ")
    pw1_lbl.pack()
    pw1_txt=tkinter.Entry(win_submit,width=20)
    pw1_txt.pack()
    
    addr1_lbl=tkinter.Label(win_submit,text="address: ")
    addr1_lbl.pack()
    addr1_txt=tkinter.Entry(win_submit,width=20)
    addr1_txt.pack()


    msg1_lbl=tkinter.Label(win_submit,text="")
    msg1_lbl.pack()

    login1_btn=tkinter.Button(win_submit,text="submit now!",command=final_submit)
    login1_btn.pack()
    
    
    #------------------------------------------
    win_submit.mainloop()
    


def admin_panel():
   win_panel=tkinter.Toplevel(win)
   win_panel.title("Panel")
   win_panel.geometry("400x400")
  
   
    
#------------------ ADMIN PANEL widgets----------------------

   Susers1_btn=tkinter.Button(win_panel,text="Submitted Users",command=submitted_panel)
   Susers1_btn.pack()
   
   storage1_btn=tkinter.Button(win_panel,text="Products available in storage",command=storage)
   storage1_btn.pack()
   
   storage0_btn=tkinter.Button(win_panel,text="Products that we ran out of !",command=storage0)
   storage0_btn.pack()
   
   sold_btn=tkinter.Button(win_panel,text="Most & Least sold products !",command=sold)
   sold_btn.pack()
   
   datelog_btn=tkinter.Button(win_panel,text="Time log of sold stuff",command=datelog)
   datelog_btn.pack()
   
   # MESSAGE TO OSTAD:
       
       # Ostad azunja ke ye shop e farzie in
       # va shoma tu class ta jayi az projecto ke kamel kardim 
       # Harfi az optione BUY nazadin o tuye surat masaleye soale
       # mianterm ham nagoftin ke option buy ro ezafe konim pas
       # man hadsam ine ke mikhastin in shope farzio bezanim o
       # bebinin ke mitunim chizayi ke goftino amali konim ta karbar
       # masaln shoma bebine outcome esho ya na,
       # option buy ro ezafe nkrdm
       # ke omidvarm hadsam dorost bude bashe :(
       # chon alan ke daram projecto tamum mikonam jomasto 
       # rahi nist azatun beporsam
       # va tahe project sare ezafe kardane date yade buy oftdm ke age ezafe mikrdm
       # bayad kheyli chizaro avaz mikrdm ke dg time eii ta saat 12 e shb nmunde
       # ke mirim tu shanbe o ta qablesh byd projecto upload konm


#-----------------------------------------------
   win_panel.mainloop()


def submitted_panel():
    win_submitted_panel=tkinter.Toplevel(win)
    win_submitted_panel.title("Submitted Users")
    win_submitted_panel.geometry("400x400")
    
    lstbox=tkinter.Listbox(win_submitted_panel,width=40)
    lstbox.pack()
    
    query='''SELECT ID,user FROM users'''
    result=cnt.execute(query)
    rows=result.fetchall()
    for user in rows:
        mystr=f"id: {user[0]}  name: {user[1]} "
        lstbox.insert(0, mystr)
    
    
    win.mainloop()
    
    
def storage():
    win_storage=tkinter.Toplevel(win)
    win_storage.title("Available Products in storage")
    win_storage.geometry("400x400")
    
    lstbox=tkinter.Listbox(win_storage,width=40)
    lstbox.pack()
    
    query='''SELECT name,qnt FROM products'''
    result=cnt.execute(query)
    rows=result.fetchall()
    for availables in rows:
        mystr=f"name: {availables[0]}  available qnt: {availables[1]} "
        lstbox.insert(0, mystr)
    
    
    win.mainloop()
    
    
    
def storage0():
    win_storage0=tkinter.Toplevel(win)
    win_storage0.title("Not Available in storage")
    win_storage0.geometry("400x400")
    
    lstbox=tkinter.Listbox(win_storage0,width=40)
    lstbox.pack()
    
    query='''SELECT name FROM products WHERE qnt==0'''
    result=cnt.execute(query)
    rows=result.fetchall()
    for not_available in rows:
        mystr=f"name: {not_available[0]} "
        lstbox.insert(0, mystr)
    
    
    win.mainloop()
    
    
def sold():
    win_sold=tkinter.Toplevel(win)
    win_sold.title("Most & Least sold products")
    win_sold.geometry("500x500")
    
    lstbox=tkinter.Listbox(win_sold,width=40)
    lstbox.pack()
    
    lstbox1=tkinter.Listbox(win_sold,width=40)
    lstbox1.pack()
    
    query='''SELECT name FROM products WHERE qnt==0'''
    result=cnt.execute(query)
    rows=result.fetchall()
    for most_bought in rows:
        mystr=f"Most Bought item: {most_bought[0]} "
        lstbox.insert(0, mystr)
    
    query='''SELECT name FROM products WHERE qnt>=15'''
    result=cnt.execute(query)
    rows=result.fetchall()
    for least_bought in rows:
        mystr=f"Least Bought item: {least_bought[0]} "
        lstbox1.insert(0, mystr)
    
    win.mainloop()
    
    
    
def datelog():
    
    # MESSAGE TO OSTAD:
        
        # Ostad azunja ke ye shop e farzie in
        # va shoma tu class ta jayi az projecto ke kamel kardim 
        # Harfi az optione BUY nazadin o tuye surat masaleye soale
        # mianterm ham nagoftin ke option buy ro ezafe konim pas
        # man hadsam ine ke mikhastin in shope farzio bezanim o
        # bebinin ke mitunim chizayi ke goftino amali konim ta karbar
        # masaln shoma bebine outcome esho ya na,
        # option buy ro ezafe nkrdm
        # ke omidvarm hadsam dorost bude bashe :(
        # chon alan ke daram projecto tamum mikonam jomasto 
        # rahi nist azatun beporsam
        # va tahe project sare ezafe kardane date yade buy oftdm ke age ezafe mikrdm
        # bayad kheyli chizaro avaz mikrdm ke dg time eii ta saat 12 e shb nmunde
        # ke mirim tu shanbe o ta qablesh byd projecto upload konm
        
    global datelog_lbl 
    global datelog_txt
    global enter_date
    win_datelog=tkinter.Toplevel(win)
    win_datelog.title("date:" )
    win_datelog.geometry("400x400")
    
    datelog_txt=tkinter.Entry(win_datelog,width=20)
    datelog_txt.pack()
    
    datelog_lbl=tkinter.Label(win_datelog,text="date :")
    datelog_lbl.pack()
    
    enter_date=datelog_txt.get()
    
    datelog1_btn=tkinter.Button(win_datelog,text=" Show Me! ",command=product_dates)
    datelog1_btn.pack()
    
    
    win_datelog.mainloop()

    
    
    
    
def product_dates():
    
    win_datelog1=tkinter.Toplevel(win)
    win_datelog1.title("Products bought in specific dates: " )
    win_datelog1.geometry("400x400")
    
    
    query = '''SELECT name FROM products WHERE dates= ? '''
    result=cnt.execute(query,(enter_date,))
    rows=result.fetchall()
    
    lstbox=tkinter.Listbox(win_datelog1,width=100,height=50)
    lstbox.pack()
    
    for product in rows :
         lstbox.insert(0,product)
         
         
         
    win_datelog1.mainloop()
    
    
    
    
    
def shop():
    win_shop=tkinter.Toplevel(win)
    win_shop.title("Shop")
    win_shop.geometry("400x400")
   
    lstbox=tkinter.Listbox(win_shop,width=40)
    lstbox.pack()
    
    query='''SELECT * FROM products'''
    result=cnt.execute(query)
    rows=result.fetchall()
    for product in rows:
        mystr=f"id: {product[0]}  name: {product[1]}  price: {product[2]}  qnt: {product[3]} "
        lstbox.insert(0, mystr)
    
    
    win.mainloop()

#---------------------- widgets ---------------------------------------------------

win=tkinter.Tk()
win.title("main")
win.geometry("300x300")


user_lbl=tkinter.Label(text="username: ")
user_lbl.pack()
user_txt=tkinter.Entry(width=20)
user_txt.pack()

pw_lbl=tkinter.Label(text="password: ")
pw_lbl.pack()
pw_txt=tkinter.Entry(width=20)
pw_txt.pack()


msg_lbl=tkinter.Label(text="")
msg_lbl.pack()

login_btn=tkinter.Button(text="Login",command=login)
login_btn.pack()

logout_btn=tkinter.Button(text="Logout",state="disabled",command=logout)
logout_btn.pack()


submit_btn=tkinter.Button(text="submit",command=submit)
submit_btn.pack()


shop_btn=tkinter.Button(text="shop",state="disabled",command=shop)
shop_btn.pack()


adminpanel_btn=tkinter.Button(text="Admin Panel",state="disabled",command=admin_panel)
adminpanel_btn.pack()



win.mainloop()