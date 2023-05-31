from logging import info
from tkinter import*

from PIL import Image,ImageTk
from tkinter import ttk
import random
from time import strftime
from datetime import datetime
import mysql.connector
from tkinter import messagebox
import tempfile
import os

class Roombooking_window:
    def __init__(self,root):
        self.root=root
        self.root.title("Hotel Management System     | Developed By Group 5 ")
        self.root.geometry("1400x1400+0+225")

        #======variabless=====
        self.var_contact=StringVar()
        self.var_checkin=StringVar()
        self.var_checkout=StringVar()
        self.var_roomtype=StringVar()
        self.var_roomavailable=StringVar()
        self.var_meal=StringVar()
        self.var_noofdays=StringVar()
        self.var_noofhrs=IntVar()
        self.var_paidtax=StringVar()
        self.var_actualtotal=StringVar()
        self.var_total=StringVar()
        self.shortime=StringVar()






         #======title===============
        lbl_title=Label(self.root,text="ROOM BOOKING  DETAILS",font=("times new roman",20,"bold"),bg="green",fg="gold",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1400,height=40)
         #=====logo==================
        img2=Image.open(r"C:\Hotel Management System\images\winhotel.png")
        img2=img2.resize((100,48),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        lblimg=Label(self.root,image=self.photoimg2,bd=0,relief=RIDGE)
        lblimg.place(x=5,y=2,width=100,height=38)

        #===========Room labelframe======================
        labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="Room Booking Details", font=("times new roman",10,"bold"),padx=2)
        labelframeleft.place(x=0,y=50,width=425,height=430)

        #=======labels and entry===========
        #==customer contact
        lbl_cust_contact=Label(labelframeleft,text="Customer contact",font=("times new roman",12,"bold"),padx=2,pady=6)
        lbl_cust_contact.grid(row=0,column=0,sticky=W)


        enty_contact=ttk.Entry(labelframeleft,textvariable=self.var_contact,font=("times new roman",13,"bold"),width=20)
        enty_contact.grid(row=0,column=1,sticky=W)

        


        #==fetch data button
        btn_fetchdata=Button(labelframeleft,command=self.fetch_contact,text="fetch data",font=("arial",11,"bold"),bg="green",fg="gold",width=8)
        btn_fetchdata.place(x=330,y=4)





        #==check_in date
        lbl_check_in_date=Label(labelframeleft,text="Check_in_Date" ,font=("times new roman",12,"bold"),padx=2,pady=6)
        lbl_check_in_date.grid(row=1,column=0,sticky=W)

        txt_check_in_date=ttk.Entry(labelframeleft,textvariable=self.var_checkin,width=29,font=("times new roman",13,"bold"))
        txt_check_in_date.grid(row=1,column=1)

        #==check_out date
        lbl_check_out_date=Label(labelframeleft,text="Check_out_Date",font=("times new roman",12,"bold"),padx=2,pady=6)
        lbl_check_out_date.grid(row=2,column=0,sticky=W)

        txt_check_out=ttk.Entry(labelframeleft,textvariable=self.var_checkout,width=29,font=("times new roman",13,"bold"))
        txt_check_out.grid(row=2,column=1)

        #===Room Type
        lbl_roomtype=Label(labelframeleft,font=("arial",12,"bold"),text="Room Type:",padx=2,pady=6)
        lbl_roomtype.grid(row=3,column=0,sticky=W)
        
        conn=mysql.connector.connect(host="localhost",user="root",password="12345",database="dbcustomer")
        my_cursor=conn.cursor()
        my_cursor.execute("select Roomtype from rdetails")
        ide=my_cursor.fetchall()
        
        
        combo_roomtype=ttk.Combobox(labelframeleft,textvariable=self.var_roomtype,font=("arial",12,"bold"),width=27,state="readonly")
        combo_roomtype["values"]=ide
        combo_roomtype.current(0)
        combo_roomtype.grid(row=3,column=1)

        #available room
        lbl_available_room=Label(labelframeleft,text="Room No.",font=("times new roman",12,"bold"),padx=2,pady=6)
        lbl_available_room.grid(row=4,column=0,sticky=W)

        #txt_availableroom=ttk.Entry(labelframeleft,textvariable=self.var_roomavailable,width=29,font=("times new roman",13,"bold"))
        #txt_availableroom.grid(row=4,column=1)

        conn=mysql.connector.connect(host="localhost",user="root",password="12345",database="dbcustomer")
        my_cursor=conn.cursor()
        my_cursor.execute("select Roomno from rdetails")
        rows=my_cursor.fetchall()

        

        

        combo_roomno=ttk.Combobox(labelframeleft,textvariable=self.var_roomavailable,font=("arial",12,"bold"),width=27,state="readonly")
        combo_roomno["value"]=rows
        combo_roomno.current(0)
        combo_roomno.grid(row=4,column=1)

        
        
        


        



        #==Meal===
        
        lbl_meal=Label(labelframeleft,text="Meal",font=("times new roman",12,"bold"),padx=2,pady=6)
        lbl_meal.grid(row=5,column=0,sticky=W)
        
        
        combo_roomtype=ttk.Combobox(labelframeleft,textvariable=self.var_meal,font=("arial",12,"bold"),width=27,state="readonly")
        combo_roomtype["value"]=("Breakfast","Lunch","Dinner","None")
        combo_roomtype.current(0)
        combo_roomtype.grid(row=5,column=1)
        
        
        
        
        
        
        
      

        # No of days
        lbl_no_days=Label(labelframeleft,text="No.of Days",font=("times new roman",12,"bold"),padx=2,pady=6)
        lbl_no_days.grid(row=6,column=0,sticky=W)

        txt_no_days=ttk.Entry(labelframeleft,textvariable=self.var_noofdays,width=29,font=("times new roman",13,"bold"))
        txt_no_days.grid(row=6,column=1)


        # No of hrs
        lbl_no_hrs=Label(labelframeleft,text="No.of hours",font=("times new roman",12,"bold"),padx=2,pady=6)
        lbl_no_hrs.grid(row=7,column=0,sticky=W)

        txt_no_hrs=ttk.Entry(labelframeleft,textvariable=self.var_noofhrs,width=29,font=("times new roman",13,"bold"))
        txt_no_hrs.grid(row=7,column=1)

        #==Paid tax===
        lbl_paid_tax=Label(labelframeleft,text="Paid tax",font=("times new roman",12,"bold"),padx=2,pady=6)
        lbl_paid_tax.grid(row=8,column=0,sticky=W)

        txt_paid_tax=ttk.Entry(labelframeleft,textvariable=self.var_paidtax,width=29,font=("times new roman",13,"bold"))
        txt_paid_tax.grid(row=8,column=1)

        #==sub total
        lbl_subtotal=Label(labelframeleft,text="Sub Total",font=("times new roman",12,"bold"),padx=2,pady=6)
        lbl_subtotal.grid(row=9,column=0,sticky=W)

        txt_subtotal=ttk.Entry(labelframeleft,textvariable=self.var_actualtotal,width=29,font=("times new roman",13,"bold"))
        txt_subtotal.grid(row=9,column=1)

        # total cost==
        lbl_totalcost=Label(labelframeleft,text="Total Cost",font=("times new roman",12,"bold"),padx=2,pady=6)
        lbl_totalcost.grid(row=10,column=0,sticky=W)

        txt_totalcost=ttk.Entry(labelframeleft,textvariable=self.var_total,width=29,font=("times new roman",13,"bold"))
        txt_totalcost.grid(row=10,column=1)

   
        
        #========buttons========
        btn_frame=Frame(labelframeleft,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=380,width=420,height=27)
        
        btnadd=Button(btn_frame,text="Add",command=self.add_data,font=("arial",10,"bold"),bg="green",fg="gold",width=9)
        btnadd.grid(row=0,column=0,padx=1)

        btnupdate=Button(btn_frame,text="Update",command=self.update,font=("arial",10,"bold"),bg="green",fg="gold",width=9)
        btnupdate.grid(row=0,column=1,padx=1)

        btndelete=Button(btn_frame,text="Delete",command=self.mdelete_data,font=("arial",10,"bold"),bg="green",fg="gold",width=9)
        btndelete.grid(row=0,column=2,padx=1)

        btnReset=Button(btn_frame,text="Reset",command=self.reset,font=("arial",10,"bold"),bg="green",fg="gold",width=9)
        btnReset.grid(row=0,column=3,padx=1)

        #===Bill Button==
        btnbill=Button(btn_frame,text="Bill",command=self.total,font=("arial",10,"bold"),bg="green",fg="gold",width=9)
        btnbill.grid(row=0,column=4,padx=1)

        btnprint=Button(self.root,command=self.printb,text="Print",font=("arial",10,"bold"),bg="green",fg="gold",width=9)
        btnprint.place(x=700,y=255)

        
        #============rightside image===
        img3=Image.open(r"C:\Hotel Management System\images\bed.jpg")
        img3=img3.resize((325,300),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        lblimg=Label(self.root,image=self.photoimg3,bd=0,relief=RIDGE)
        lblimg.place(x=800,y=55,width=325,height=250)



         #=======search table frame system============
        table_frame=LabelFrame(self.root,bd=2,relief=RIDGE,text="View Details and  Search", font=("arial",12,"bold"),padx=2)
        table_frame.place(x=435,y=280,width=690,height=200)

        lbl_searchby=Label(table_frame,text="Search By: ",font=("times new roman",12,"bold"),bg="green",fg="white")
        lbl_searchby.grid(row=0,column=0,sticky=W,padx=2)


        self.serch_var=StringVar()
        combo_search=ttk.Combobox(table_frame,textvariable=self.serch_var,font=("arial",12,"bold"),width=27,state="readonly")
        combo_search["value"]=("Contact","Room")
        combo_search.current(0)
        combo_search.grid(row=0,column=1,padx=2)

        self.txt_search=StringVar()
        txt_search=ttk.Entry(table_frame,textvariable=self.txt_search,font=("times new roman",13,"bold"),width=20)
        txt_search.grid(row=0,column=2,padx=2)


        btn_search=Button(table_frame,text="Search",command=self.search_data,font=("arial",11,"bold"),bg="green",fg="gold",width=5)
        btn_search.grid(row=0,column=3,padx=1)

        btn_show=Button(table_frame,text="Show All",command=self.fetch_data,font=("arial",11,"bold"),bg="green",fg="gold",width=8)
        btn_show.grid(row=0,column=4,padx=1)

       

         #======show data table======

        view_table=Frame(table_frame,bd=2,relief=RIDGE)
        view_table.place(x=0,y=50,width=680,height=120)

        scrollx=ttk.Scrollbar(view_table,orient=HORIZONTAL)
        scrolly=ttk.Scrollbar(view_table,orient=VERTICAL)

        self.room_details_table=ttk.Treeview(view_table,column=("Contact","Checkindate","Checkoutdate","Roomtype","Room","Meal","NoOfdays","noofhrs"),xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)


        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)

        scrollx.config(command=self.room_details_table.xview)
        scrolly.config(command=self.room_details_table.yview)

        self.room_details_table.heading("Contact",text="Contact")
        self.room_details_table.heading("Checkindate",text="Check_in")
        self.room_details_table.heading("Checkoutdate",text="check_out")
        self.room_details_table.heading("Roomtype",text="Room_type")
        self.room_details_table.heading("Room",text="Room_No")
        self.room_details_table.heading("Meal",text="Meal")
        self.room_details_table.heading("NoOfdays",text="No_of_Days")
        self.room_details_table.heading("noofhrs",text="No_of_Hrs")
        
        self.room_details_table["show"]="headings"

        self.room_details_table.column("Contact",width=100)
        self.room_details_table.column("Checkindate",width=100)
        self.room_details_table.column("Checkoutdate",width=100)
        self.room_details_table.column("Roomtype",width=100)
        self.room_details_table.column("Room",width=100)
        self.room_details_table.column("Meal",width=100)
        self.room_details_table.column("NoOfdays",width=100)
        self.room_details_table.column("noofhrs",width=100)
        
        self.room_details_table.pack(fill=BOTH,expand=1)
        self.room_details_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()

        
        #==add data===
    def add_data(self):
        if self.var_contact.get()=="":
            messagebox.showerror("Error","All Fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",user="root",password="12345",database="dbcustomer")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into room values(%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                            self.var_contact.get(),
                                                                            self.var_checkin.get(),
                                                                            self.var_checkout.get(),
                                                                            self.var_roomtype.get(),
                                                                            self.var_roomavailable.get(),
                                                                            self.var_meal.get(),
                                                                            self.var_noofdays.get(),
                                                                            self.var_noofhrs.get()
                                                                            
                                                                        ))
                                                        
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Room booked",parent=self.root)
            except Exception as es:
                messagebox.showwarning("Warning",f"Room is Not Available:{str(es)}",parent=self.root)


        
        #=============room AVAILABILITY========
        

            #===fetch data=====
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",user="root",password="12345",database="dbcustomer")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from room order by Checkindate asc")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.room_details_table.delete(*self.room_details_table.get_children())
            for i in rows:
                self.room_details_table.insert("",END,values=i)
            conn.commit()
        conn.close()

        #===get cursor data
    def get_cursor(self,events=""):
        cursor_rows=self.room_details_table.focus()
        content=self.room_details_table.item(cursor_rows)
        row=content["values"]

        self.var_contact.set(row[0])
        self.var_checkin.set(row[1])
        self.var_checkout.set(row[2])
        self.var_roomtype.set(row[3])
        self.var_roomavailable.set(row[4])
        self.var_meal.set(row[5])
        self.var_noofdays.set(row[6])
        self.var_noofhrs.set(row[7])

        #update===
    
    def update(self):
        if self.var_contact.get()=="":
            messagebox.showerror("Error","Please Enter Mobile Number",parent=self.root)
        
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="12345",database="dbcustomer")
            my_cursor=conn.cursor()
            my_cursor.execute("update room set Checkin=%s,Checkout=%s,Roomtype=%s,Room=%s,Meal=%s,noOfdays=%s,noofhrs=%s where Contact=%s",(

                                                                                                                    
                                                                                                                    self.var_checkin.get(),
                                                                                                                    self.var_checkout.get(),
                                                                                                                    self.var_roomtype.get(),
                                                                                                                    self.var_roomavailable.get(),
                                                                                                                    self.var_meal.get(),
                                                                                                                    self.var_noofdays.get(),
                                                                                                                    self.var_noofhrs.get(),
                                                                                                                    self.var_contact.get(),
                                                                                                                   

                                                                                                                                                ))

            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Update","Room details has been updated successfully",parent=self.root)


            #==delete data
    def mdelete_data(self):
        mdelete_data=messagebox.askyesno("Hotel Management System","Do you want to delete this Room Booked",parent=self.root)
        if mdelete_data>0:
            conn=mysql.connector.connect(host="localhost",user="root",password="12345",database="dbcustomer")
            my_cursor=conn.cursor()
            query="delete from room  where Contact=%s"
            value=(self.var_contact.get(),)
            my_cursor.execute(query,value)
        else:
            if not mdelete_data:
                return
        conn.commit()
        self.fetch_data()
        conn.close()


    def reset(self):
        self.var_contact.set("")
        self.var_checkin.set("")
        self.var_checkout.set("")
        self.var_roomtype.set("")
        self.var_roomavailable.set("")
        self.var_meal.set("")
        self.var_noofdays.set("")
        self.var_noofhrs.set("")
        self.var_paidtax.set("")
        self.var_actualtotal.set("")
        self.var_total.set("")
        
        self.total()
        






    
    def fetch_contact(self):
        if self.var_contact.get()=="":
             messagebox.showerror("Error","please Enter Contact Number",parent=self.root)

        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="12345",database="dbcustomer")
            my_cursor=conn.cursor()
            query=("select Ref from tblcustomer where Mobile =%s")
            value=(self.var_contact.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            
            

            if row==None:
                messagebox.showerror("Error","This Number Not Found",parent=self.root)
            else:
               
                conn.commit()
                conn.close()




                
                
                showdataframe=Frame(self.root,bd=4,relief=RIDGE,padx=2)
                showdataframe.place(x=455,y=50,width=300,height=200)
               
               

                receipt_area=Label(showdataframe,text="Bill Area",font="arial 12 bold",bd=5,relief=GROOVE).pack(fill=X)
                scrol_y=Scrollbar(showdataframe,orient=VERTICAL)
                self.txtarea=Text(showdataframe,yscrollcommand=scrol_y.set)
                scrol_y.pack(side=RIGHT,fill=Y)
                scrol_y.config(command=self.txtarea.yview)
                self.txtarea.pack(fill=BOTH,expand=1)

                result=row[0]
                
                self.txtarea.insert(END,f"Ref: {result}")
                
                
               
                
               

                
                #==database Name====
                conn=mysql.connector.connect(host="localhost",user="root",password="12345",database="dbcustomer")
                my_cursor=conn.cursor()
                query=("select Lastname from tbl_customer where Mobile =%s")
                value=(self.var_contact.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()

                result=row[0]
                
                self.txtarea.insert(END,f"\nName: {result}")
                

                



                #======database Gender

                
                conn=mysql.connector.connect(host="localhost",user="root",password="12345",database="dbcustomer")
                my_cursor=conn.cursor()
                query=("select Gender from tbl_customer where Mobile =%s")
                value=(self.var_contact.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()

                result=row[0]
              
                self.txtarea.insert(END,f"\nGender: {result}")

                
                self.txtarea.insert(END,f"\n\n=================================")
               
                
    
            #searh system==========

    def search_data(self):

        if self.txt_search.get()=="":
            messagebox.showerror("Error","Enter Contact or Room",parent=self.root)

        else:

        
                  
            conn=mysql.connector.connect(host="localhost",user="root",password="12345",database="dbcustomer")
            my_cursor=conn.cursor()
            my_cursor.execute('select * from room where ' +str(self.serch_var.get())+" LIKE '%"+str(self.txt_search.get()+"%'"))
            rows=my_cursor.fetchall()
            if len (rows)!=0:
                self.room_details_table.delete(*self.room_details_table.get_children())
                for i in rows:
                    self.room_details_table.insert("",END,values=i)
               
                conn.commit()
                conn.close()

            else:
                messagebox.showerror("Error","Room booked Not Found")

   





    def total(self):
       
    
    
        in_date=self.var_checkin.get()
        out_date=self.var_checkout.get() 
        in_date=datetime.strptime(in_date,"%m/%d/%Y")
        out_date=datetime.strptime(out_date,"%m/%d/%Y")
        self.var_noofdays.set(abs(out_date-in_date).days)
  

        if (self.var_meal.get()=="Breakfast" and self.var_roomtype.get()=="Standard_Room"):
            mealprice=float(300)
            Standardroomprice=float(800)
            numdays=float(self.var_noofdays.get())
            
            formula1=float(mealprice+Standardroomprice)
            formula2=float(numdays*formula1)
            Tax="₱ "+str("%.2f"%((formula2)*0.01))
            St="₱ "+str("%.2f"%((formula2)))
            Tt="₱ "+str("%.2f"%(formula2+((formula2)*0.01)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(St)
            self.var_total.set(Tt)
            self.var_noofhrs.set(0)
            
            self.txtarea.insert(END,f"\n Number of days:{self.var_noofdays.get()}")
            self.txtarea.insert(END,f"\n Paid tax:{self.var_paidtax.get()}")
            self.txtarea.insert(END,f"\n Sub total:{self.var_actualtotal.get()}")
            self.txtarea.insert(END,f"\n Total Cost:{self.var_total.get()}")
            
        
        elif(self.var_meal.get()=="Lunch" and self.var_roomtype.get()=="Standard_Room"):
            mealprice=float(500)
            Standardroomprice=float(800)
            numdays=float(self.var_noofdays.get())
            
            formula1=float(mealprice+Standardroomprice)
            formula2=float(numdays*formula1)
            Tax="₱ "+str("%.2f"%((formula2)*0.01))
            St="₱ "+str("%.2f"%((formula2)))
            Tt="₱ "+str("%.2f"%(formula2+((formula2)*0.01)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(St)
            self.var_total.set(Tt)
            self.var_noofhrs.set(0)
            
            self.txtarea.insert(END,f"\n Number of days:{self.var_noofdays.get()}")
            self.txtarea.insert(END,f"\n Paid tax:{self.var_paidtax.get()}")
            self.txtarea.insert(END,f"\n Sub total:{self.var_actualtotal.get()}")
            self.txtarea.insert(END,f"\n Total Cost:{self.var_total.get()}")
        
        elif(self.var_meal.get()=="Dinner" and self.var_roomtype.get()=="Standard_Room"):
            mealprice=float(500)
            Standardroomprice=float(800)
            numdays=float(self.var_noofdays.get())
            
            formula1=float(mealprice+Standardroomprice)
            formula2=float(numdays*formula1)
            Tax="₱ "+str("%.2f"%((formula2)*0.01))
            St="₱ "+str("%.2f"%((formula2)))
            Tt="₱ "+str("%.2f"%(formula2+((formula2)*0.01)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(St)
            self.var_total.set(Tt)
            self.var_noofhrs.set(0)
            
            self.txtarea.insert(END,f" Number of days:{self.var_noofdays.get()}")
            self.txtarea.insert(END,f"\n Paid tax:{self.var_paidtax.get()}")
            self.txtarea.insert(END,f"\n Sub total:{self.var_actualtotal.get()}")
            self.txtarea.insert(END,f"\n Total Cost:{self.var_total.get()}")

        
        elif(self.var_meal.get()=="Breakfast" and self.var_roomtype.get()=="Family_Room"):
            mealprice=float(300)
            Standardroomprice=float(1100)
            numdays=float(self.var_noofdays.get())
            
            formula1=float(mealprice+Standardroomprice)
            formula2=float(numdays*formula1)
            Tax="₱ "+str("%.2f"%((formula2)*0.01))
            St="₱ "+str("%.2f"%((formula2)))
            Tt="₱ "+str("%.2f"%(formula2+((formula2)*0.01)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(St)
            self.var_total.set(Tt)
            self.var_noofhrs.set(0)
            
            self.txtarea.insert(END,f"\n Number of days:{self.var_noofdays.get()}")
            self.txtarea.insert(END,f"\n Paid tax:{self.var_paidtax.get()}")
            self.txtarea.insert(END,f"\n Sub total:{self.var_actualtotal.get()}")
            self.txtarea.insert(END,f"\n Total Cost:{self.var_total.get()}")


        elif(self.var_meal.get()=="Lunch" and self.var_roomtype.get()=="Family_Room"):
            mealprice=float(500)
            Standardroomprice=float(1100)
            numdays=float(self.var_noofdays.get())
            
            formula1=float(mealprice+Standardroomprice)
            formula2=float(numdays*formula1)
            Tax="₱ "+str("%.2f"%((formula2)*0.01))
            St="₱ "+str("%.2f"%((formula2)))
            Tt="₱ "+str("%.2f"%(formula2+((formula2)*0.01)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(St)
            self.var_total.set(Tt)

            self.var_noofhrs.set(0)
            
            self.txtarea.insert(END,f"\nNumber of days:{self.var_noofdays.get()}")
            self.txtarea.insert(END,f"\n Paid tax:{self.var_paidtax.get()}")
            self.txtarea.insert(END,f"\n Sub total:{self.var_actualtotal.get()}")
            self.txtarea.insert(END,f"\n Total Cost:{self.var_total.get()}")

        elif(self.var_meal.get()=="Dinner" and self.var_roomtype.get()=="Family_Room"):
            mealprice=float(500)
            Standardroomprice=float(1100)
            numdays=float(self.var_noofdays.get())
            
            formula1=float(mealprice+Standardroomprice)
            formula2=float(numdays*formula1)
            Tax="₱ "+str("%.2f"%((formula2)*0.01))
            St="₱ "+str("%.2f"%((formula2)))
            Tt="₱ "+str("%.2f"%(formula2+((formula2)*0.01)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(St)
            self.var_total.set(Tt)
            self.var_noofhrs.set(0)
            
            self.txtarea.insert(END,f"\n Number of days:{self.var_noofdays.get()}")
            self.txtarea.insert(END,f"\n Paid tax:{self.var_paidtax.get()}")
            self.txtarea.insert(END,f"\n Sub total:{self.var_actualtotal.get()}")
            self.txtarea.insert(END,f"\n Total Cost:{self.var_total.get()}")

        
            
                


        
   

        elif (self.var_meal.get()=="None" and self.var_roomtype.get()=="Standard_Room"):
            threehours=float(90)
            numofhours=int(self.var_noofhrs.get())
          
            
            formula1=float(numofhours*threehours)
            Tax="₱ "+str("%.2f"%((formula1)*0.01))
            St="₱ "+str("%.2f"%((formula1)))
            Tt="₱ "+str("%.2f"%(formula1+((formula1)*0.01)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(St)
            self.var_total.set(Tt)
            
            self.txtarea.insert(END,f"\n Number of hrs:{self.var_noofhrs.get()}")
            self.txtarea.insert(END,f"\n Paid tax:{self.var_paidtax.get()}")
            self.txtarea.insert(END,f"\n Sub total:{self.var_actualtotal.get()}")
            self.txtarea.insert(END,f"\n Total Cost:{self.var_total.get()}")
            
        elif (self.var_meal.get()=="None" and self.var_roomtype.get()=="Family_Room"):
            messagebox.showerror("Error","None of the choices",parent=self.root)

        elif self.var_noofhrs.get()==3:
            messagebox.showerror("Error","None of the choices",parent=self.root)

    def printb(self):
        q=self.txtarea.get('1.0','end-1c')
        filename=tempfile.mktemp('.txt')
        open(filename,'w', encoding='utf-8').write(q)
        os.startfile(filename,'Print')

       
    
        

            

            


        
           
           
            
    
        



            


       

        
        
        
      
        
       

        
            
            


        
        
       
       
       




if __name__=="__main__":
    root=Tk()
    obj=Roombooking_window(root)
    root.mainloop()

