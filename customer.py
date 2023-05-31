from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk
import random
import mysql.connector
from tkinter import messagebox



class customer_window:
    def __init__(self,root):
        self.root=root
        self.root.title("Hotel Management System     | Developed By Group 5 ")
        self.root.geometry("1400x1400+0+225")


        #===========variables=====================
        self.var_ref=StringVar()
        x=random.randint(1000,9999)
        self.var_ref.set(str(x))


        self.var_cust_name=StringVar()
        self.var_last_name=StringVar()
        self.var_address=StringVar()
        self.var_gender=StringVar()
        self.var_mobile=StringVar()
        self.var_email=StringVar()
        self.var_nationality=StringVar()
        self.var_idproof=StringVar()
        self.var_id_num=StringVar()


        




        #======title===============
        lbl_title=Label(self.root,text="ADD CUSTOMER DETAILS",font=("times new roman",20,"bold"),bg="green",fg="gold",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1400,height=50)
         #=====logo==================
        img2=Image.open(r"C:\Hotel Management System\images\winhotel.png")
        img2=img2.resize((100,48),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        lblimg=Label(self.root,image=self.photoimg2,bd=0,relief=RIDGE)
        lblimg.place(x=5,y=2,width=100,height=48)

        #===========labelframe======================
        labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="customer Details", font=("times new roman",12,"bold"),padx=2)
        labelframeleft.place(x=5,y=50,width=425,height=425)

        #===customer label and entry========
        lbl_cust_ref=Label(labelframeleft,text="customer Ref",font=("times new roman",12,"bold"),padx=2,pady=6)
        lbl_cust_ref.grid(row=0,column=0,sticky=W)


        enty_ref=ttk.Entry(labelframeleft,textvariable=self.var_ref,font=("times new roman",13,"bold"),width=29,state="readonly")
        enty_ref.grid(row=0,column=1)


        #===customer name==========
        lbl_cust_name=Label(labelframeleft,text="First Name",font=("times new roman",12,"bold"),padx=2,pady=6)
        lbl_cust_name.grid(row=1,column=0,sticky=W)

        txt_cname=ttk.Entry(labelframeleft,textvariable=self.var_cust_name,width=29,font=("times new roman",13,"bold"))
        txt_cname.grid(row=1,column=1)

        #lastname=====
        lbl_last_name=Label(labelframeleft,text="Last Name",font=("times new roman",12,"bold"),padx=2,pady=6)
        lbl_last_name.grid(row=2,column=0,sticky=W)

        txt_lname=ttk.Entry(labelframeleft,textvariable=self.var_last_name,width=29,font=("times new roman",13,"bold"))
        txt_lname.grid(row=2,column=1)

        #====== address=========
        lbl_cust_address=Label(labelframeleft,text="Address",font=("times new roman",12,"bold"),padx=2,pady=6)
        lbl_cust_address.grid(row=3,column=0,sticky=W)

        txt_add=ttk.Entry(labelframeleft,textvariable=self.var_address,width=29,font=("times new roman",13,"bold"))
        txt_add.grid(row=3,column=1)

        #===gender=====

        lbl_gender=Label(labelframeleft,font=("arial",12,"bold"),text="Gender:",padx=2,pady=6)
        lbl_gender.grid(row=4,column=0,sticky=W)

        combo_gender=ttk.Combobox(labelframeleft,textvariable=self.var_gender,font=("arial",12,"bold"),width=27,state="readonly")
        combo_gender["value"]=("Male","Female","other")
        combo_gender.current(0)
        combo_gender.grid(row=4,column=1)
        


        #======mobile=========
        lbl_mobile=Label(labelframeleft,text="Mobile Number",font=("times new roman",12,"bold"),padx=2,pady=6)
        lbl_mobile.grid(row=5,column=0,sticky=W)

        txt_Mnum=ttk.Entry(labelframeleft,textvariable=self.var_mobile,width=29,font=("times new roman",13,"bold"))
        txt_Mnum.grid(row=5,column=1)

        #======email======
        lbl_email=Label(labelframeleft,text="Email",font=("times new roman",12,"bold"),padx=2,pady=6)
        lbl_email.grid(row=6,column=0,sticky=W)

        txt_email=ttk.Entry(labelframeleft,textvariable=self.var_email,width=29,font=("times new roman",13,"bold"))
        txt_email.grid(row=6,column=1)

        #=====nationality====

        lbl_nationality=Label(labelframeleft,text="Nationality",font=("times new roman",12,"bold"),padx=2,pady=6)
        lbl_nationality.grid(row=7,column=0,sticky=W)

        combo_nationality=ttk.Combobox(labelframeleft,textvariable=self.var_nationality,font=("arial",12,"bold"),width=27,state="readonly")
        combo_nationality["value"]=("Filipino","American","korean","british","Swedish","Indian")
        combo_nationality.current(0)
        combo_nationality.grid(row=7,column=1)
        
        #=======id proof type===========
        lbl_idproof=Label(labelframeleft,text="ID Proof Type",font=("times new roman",12,"bold"),padx=2,pady=6)
        lbl_idproof.grid(row=8,column=0,sticky=W)

        combo_idproof=ttk.Combobox(labelframeleft,textvariable=self.var_idproof,font=("arial",12,"bold"),width=27,state="readonly")
        combo_idproof["value"]=("Government ID","Driver License","Passport")
        combo_idproof.current(0)
        combo_idproof.grid(row=8,column=1)

        #====id number=====
        lbl_id_no=Label(labelframeleft,text="ID No.",font=("times new roman",12,"bold"),padx=2,pady=6)
        lbl_id_no.grid(row=9,column=0,sticky=W)

        txt_id_no=ttk.Entry(labelframeleft,textvariable=self.var_id_num,width=29,font=("times new roman",13,"bold"))
        txt_id_no.grid(row=9,column=1)


        #========buttons========
        btn_frame=Frame(labelframeleft,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=350,width=412,height=40)
        
        btnadd=Button(btn_frame,text="Add",command=self.add_data,font=("arial",11,"bold"),bg="green",fg="gold",width=10)
        btnadd.grid(row=0,column=0,padx=1)

        btnupdate=Button(btn_frame,text="Update",command=self.update,font=("arial",11,"bold"),bg="green",fg="gold",width=10)
        btnupdate.grid(row=0,column=1,padx=1)

        btndelete=Button(btn_frame,text="Delete",command=self.mdelete_data,font=("arial",11,"bold"),bg="green",fg="gold",width=10)
        btndelete.grid(row=0,column=2,padx=1)

        btnReset=Button(btn_frame,text="Reset",command=self.reset,font=("arial",11,"bold"),bg="green",fg="gold",width=10)
        btnReset.grid(row=0,column=3,padx=1)


        #=======search table frame system============
        table_frame=LabelFrame(self.root,bd=2,relief=RIDGE,text="View Details and  Search", font=("arial",12,"bold"),padx=2)
        table_frame.place(x=435,y=50,width=690,height=490)

        lbl_searchby=Label(table_frame,text="Search By: ",font=("times new roman",12,"bold"),bg="green",fg="white")
        lbl_searchby.grid(row=0,column=0,sticky=W,padx=2)


        self.serch_var=StringVar()
        combo_search=ttk.Combobox(table_frame,textvariable=self.serch_var,font=("arial",12,"bold"),width=27,state="readonly")
        combo_search["value"]=("Mobile","Ref")
        combo_search.current(0)
        combo_search.grid(row=0,column=1,padx=2)

        self.txt_search=StringVar()
        txt_search=ttk.Entry(table_frame,textvariable=self.txt_search,font=("times new roman",13,"bold"),width=20)
        txt_search.grid(row=0,column=2,padx=2)


        btn_search=Button(table_frame,text="Search",command=self.search,font=("arial",11,"bold"),bg="green",fg="gold",width=5)
        btn_search.grid(row=0,column=3,padx=1)

        btn_show=Button(table_frame,text="Show All",command=self.fetch_data,font=("arial",11,"bold"),bg="green",fg="gold",width=8)
        btn_show.grid(row=0,column=4,padx=1)

        #======show data table======

        view_table=Frame(table_frame,bd=2,relief=RIDGE)
        view_table.place(x=0,y=50,width=680,height=350)

        scrollx=ttk.Scrollbar(view_table,orient=HORIZONTAL)
        scrolly=ttk.Scrollbar(view_table,orient=VERTICAL)

        self.cust_details_table=ttk.Treeview(view_table,column=("Ref","FName","LName","Address","Gender","Mobile","Email","Nationality",
        "Id_proof","Id_number"),xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)


        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)

        scrollx.config(command=self.cust_details_table.xview)
        scrolly.config(command=self.cust_details_table.yview)

        self.cust_details_table.heading("Ref",text="Refer_no")
        self.cust_details_table.heading("FName",text="First_Name")
        self.cust_details_table.heading("LName",text="Last_Name")
        self.cust_details_table.heading("Address",text="Address")
        self.cust_details_table.heading("Gender",text="Gender")
        self.cust_details_table.heading("Mobile",text="Mobile")
        self.cust_details_table.heading("Email",text="Email")
        self.cust_details_table.heading("Nationality",text="Nationality")
        self.cust_details_table.heading("Id_proof",text="Id_proof")
        self.cust_details_table.heading("Id_number",text="Id_number")

        self.cust_details_table["show"]="headings"

        self.cust_details_table.column("Ref",width=100)
        self.cust_details_table.column("FName",width=100)
        self.cust_details_table.column("LName",width=100)
        self.cust_details_table.column("Address",width=100)
        self.cust_details_table.column("Gender",width=100)
        self.cust_details_table.column("Mobile",width=100)
        self.cust_details_table.column("Email",width=100)
        self.cust_details_table.column("Nationality",width=100)
        self.cust_details_table.column("Id_proof",width=100)
        self.cust_details_table.column("Id_number",width=100)


        self.cust_details_table.pack(fill=BOTH,expand=1)
        self.cust_details_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()


    def add_data(self):
        if self.var_mobile.get()=="" or self.var_email.get()=="":
            messagebox.showerror("Error","All Fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",user="root",password="12345",database="dbcustomer")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into tblcustomer values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                            self.var_ref.get(),
                                                                            self.var_cust_name.get(),
                                                                            self.var_last_name.get(),
                                                                            self.var_address.get(),
                                                                            self.var_gender.get(),
                                                                            self.var_mobile.get(),
                                                                            self.var_email.get(),
                                                                            self.var_nationality.get(),
                                                                            self.var_idproof.get(),
                                                                            self.var_id_num.get()
                                                                        ))
                                                        
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Customer Has been added",parent=self.root)
            except Exception as es:
                messagebox.showwarning("Warning",f"Something went wrong:{str(es)}",parent=self.root)

    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",user="root",password="12345",database="dbcustomer")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from tblcustomer")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.cust_details_table.delete(*self.cust_details_table.get_children())
            for i in rows:
                self.cust_details_table.insert("",END,values=i)
            conn.commit()
        conn.close()

    def get_cursor(self,events=""):
        cursor_rows=self.cust_details_table.focus()
        content=self.cust_details_table.item(cursor_rows)
        row=content["values"]

        self.var_ref.set(row[0])
        self.var_cust_name.set(row[1])
        self.var_last_name.set(row[2])
        self.var_address.set(row[3])
        self.var_gender.set(row[4])
        self.var_mobile.set(row[5])
        self.var_email.set(row[6])
        self.var_nationality.set(row[7])
        self.var_idproof.set(row[8])
        self.var_id_num.set(row[9])


    def update(self):
        if self.var_mobile.get()=="":
            messagebox.showerror("Error","Please Enter Mobile Number",parent=self.root)
        
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="12345",database="dbcustomer")
            my_cursor=conn.cursor()
            my_cursor.execute("update tblcustomer set FName=%s,LName=%s,Address=%s,Gender=%s,Mobile=%s,Email=%s,Nationality=%s,Id_proof=%s,Id_number=%s where Ref=%s",(

                                                                                                                    
                                                                                                                    self.var_cust_name.get(),
                                                                                                                    self.var_last_name.get(),
                                                                                                                    self.var_address.get(),
                                                                                                                    self.var_gender.get(),
                                                                                                                    self.var_mobile.get(),
                                                                                                                    self.var_email.get(),
                                                                                                                    self.var_nationality.get(),
                                                                                                                    self.var_idproof.get(),
                                                                                                                    self.var_id_num.get(),
                                                                                                                    self.var_ref.get()

                                                                                                                                                ))

            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Update","Customer details has been updated successfully",parent=self.root)


    def mdelete_data(self):
        mdelete_data=messagebox.askyesno("Hotel Management System","Do you want to delete this Customer",parent=self.root)
        if mdelete_data>0:
            conn=mysql.connector.connect(host="localhost",user="root",password="12345",database="dbcustomer")
            my_cursor=conn.cursor()
            query="delete from tblcustomer  where Ref=%s"
            value=(self.var_ref.get(),)
            my_cursor.execute(query,value)
        else:
            if not mdelete_data:
                return
        conn.commit()
        self.fetch_data()
        conn.close()

    def reset(self):
        #self.var_ref.set("")
        self.var_cust_name.set("")
        self.var_last_name.set("")
        self.var_address.set("")
        #self.var_gender.set("")
        self.var_mobile.set("")
        self.var_email.set("")
        #self.var_nationality.set("")
        #self.var_idproof.set("")
        self.var_id_num.set("")
        x=random.randint(1000,9999)
        self.var_ref.set(str(x))


    def search(self):

        if self.txt_search.get()=="":
            messagebox.showerror("Error","Fields are Required",parent=self.root)
        
        

        
        
        else:
    
            conn=mysql.connector.connect(host="localhost",user="root",password="12345",database="dbcustomer")
            my_cursor=conn.cursor()
            my_cursor.execute('select * from tblcustomer where ' +str(self.serch_var.get())+" LIKE '%"+str(self.txt_search.get()+"%'"))
            rows=my_cursor.fetchall()
            if len (rows)!=0:
                self.cust_details_table.delete(*self.cust_details_table.get_children())
                for i in rows:
                    self.cust_details_table.insert("",END,values=i)
               
                conn.commit()
                conn.close()
            else:
                messagebox.showerror("Error","Customer Not Found")
        
            



if __name__=="__main__":
    root=Tk()
    obj=customer_window(root)
    root.mainloop()

        
