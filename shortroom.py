from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk
import random
from time import strftime
from datetime import datetime
import mysql.connector
from tkinter import messagebox


class shortRoombooking_window:
    def __init__(self,root):
        self.root=root
        self.root.title("Hotel Management System     | Developed By Group 5 ")
        self.root.geometry("1125x550+230+220")

        self.var_contact=StringVar()
        self.var_checkin=StringVar()
        self.var_checkout=StringVar() 
        self.var_roomavailable=StringVar()
        self.var_roomtype=StringVar()
        self.var_noofdays=StringVar()
        self.var_paidtax=StringVar()
        self.var_actualtotal=StringVar()
        self.var_total=StringVar()
        self.shortime=StringVar()



           #======title===============
        lbl_title=Label(self.root,text="SHORT ROOM BOOKING  DETAILS",font=("times new roman",20,"bold"),bg="green",fg="gold",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1295,height=50)
         #=====logo==================
        img2=Image.open(r"C:\Hotel Management System\images\winhotel.png")
        img2=img2.resize((100,48),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        lblimg=Label(self.root,image=self.photoimg2,bd=0,relief=RIDGE)
        lblimg.place(x=5,y=2,width=100,height=48)

        #===========Room labelframe======================
        labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="Room Booking Details", font=("times new roman",12,"bold"),padx=2)
        labelframeleft.place(x=5,y=50,width=425,height=425)


        #=======labels and entry===========
        #==customer contact
        lbl_cust_contact=Label(labelframeleft,text="Customer contact",font=("times new roman",12,"bold"),padx=2,pady=6)
        lbl_cust_contact.grid(row=0,column=0,sticky=W)


        enty_contact=ttk.Entry(labelframeleft,textvariable=self.var_contact,font=("times new roman",13,"bold"),width=20)
        enty_contact.grid(row=0,column=1,sticky=W)

         #==fetch data button
        btn_fetchdata=Button(labelframeleft,command=self.fetch_contact,text="fetch data",font=("arial",11,"bold"),bg="green",fg="gold",width=8)
        btn_fetchdata.place(x=330,y=4)

        lbl_check_in_date=Label(labelframeleft,text="Check_in" ,font=("times new roman",12,"bold"),padx=2,pady=6)
        lbl_check_in_date.grid(row=1,column=0,sticky=W)

        txt_check_in_date=ttk.Entry(labelframeleft,textvariable=self.var_checkin,width=29,font=("times new roman",13,"bold"))
        txt_check_in_date.grid(row=1,column=1)

        #==check_out date
        lbl_check_out_date=Label(labelframeleft,text="Check_out",font=("times new roman",12,"bold"),padx=2,pady=6)
        lbl_check_out_date.grid(row=2,column=0,sticky=W)

        txt_check_out=ttk.Entry(labelframeleft,textvariable=self.var_checkout,width=29,font=("times new roman",13,"bold"))
        txt_check_out.grid(row=2,column=1)

        lbl_available_room=Label(labelframeleft,text="Room No.",font=("times new roman",12,"bold"),padx=2,pady=6)
        lbl_available_room.grid(row=4,column=0,sticky=W)

        txt_availableroom=ttk.Entry(labelframeleft,textvariable=self.var_roomavailable,width=29,font=("times new roman",13,"bold"))
        txt_availableroom.grid(row=4,column=1)

        lbl_roomtype=Label(labelframeleft,text="Room Type",font=("times new roman",12,"bold"),padx=2,pady=6)
        lbl_roomtype.grid(row=5,column=0,sticky=W)

        txt_roomtype=ttk.Entry(labelframeleft,textvariable=self.var_roomtype,width=29,font=("times new roman",13,"bold"))
        txt_roomtype.grid(row=5,column=1)

       


          # No of days
        lbl_no_days=Label(labelframeleft,text="No.of Hrs",font=("times new roman",12,"bold"),padx=2,pady=6)
        lbl_no_days.grid(row=6,column=0,sticky=W)

        txt_no_days=ttk.Entry(labelframeleft,textvariable=self.var_noofdays,width=29,font=("times new roman",13,"bold"))
        txt_no_days.grid(row=6,column=1)

        #==Paid tax===
        lbl_paid_tax=Label(labelframeleft,text="Paid tax",font=("times new roman",12,"bold"),padx=2,pady=6)
        lbl_paid_tax.grid(row=7,column=0,sticky=W)

        txt_paid_tax=ttk.Entry(labelframeleft,textvariable=self.var_paidtax,width=29,font=("times new roman",13,"bold"))
        txt_paid_tax.grid(row=7,column=1)

        #==sub total
        lbl_subtotal=Label(labelframeleft,text="Sub Total",font=("times new roman",12,"bold"),padx=2,pady=6)
        lbl_subtotal.grid(row=8,column=0,sticky=W)

        txt_subtotal=ttk.Entry(labelframeleft,textvariable=self.var_actualtotal,width=29,font=("times new roman",13,"bold"))
        txt_subtotal.grid(row=8,column=1)

        # total cost==
        lbl_totalcost=Label(labelframeleft,text="Total Cost",font=("times new roman",12,"bold"),padx=2,pady=6)
        lbl_totalcost.grid(row=9,column=0,sticky=W)

        txt_totalcost=ttk.Entry(labelframeleft,textvariable=self.var_total,width=29,font=("times new roman",13,"bold"))
        txt_totalcost.grid(row=9,column=1)

         #========buttons========
        btn_frame=Frame(labelframeleft,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=330,width=420,height=40)
        
        btnadd=Button(btn_frame,command=self.add_data,text="Add",font=("arial",11,"bold"),bg="green",fg="gold",width=8)
        btnadd.grid(row=0,column=0,padx=1)

        btnupdate=Button(btn_frame,command=self.update,text="Update",font=("arial",11,"bold"),bg="green",fg="gold",width=8)
        btnupdate.grid(row=0,column=1,padx=1)

        btndelete=Button(btn_frame,command=self.mdelete_data,text="Delete",font=("arial",11,"bold"),bg="green",fg="gold",width=8)
        btndelete.grid(row=0,column=2,padx=1)

        btnReset=Button(btn_frame,command=self.reset,text="Reset",font=("arial",11,"bold"),bg="green",fg="gold",width=8)
        btnReset.grid(row=0,column=3,padx=1)

        #===Bill Button==
        btnbill=Button(btn_frame,command=self.total,text="Bill",font=("arial",11,"bold"),bg="green",fg="gold",width=8)
        btnbill.grid(row=0,column=4,padx=1)

          #============rightside image===
        img3=Image.open(r"C:\Hotel Management System\images\bed2.jpg")
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


        btn_search=Button(table_frame,command=self.search_data,text="Search",font=("arial",11,"bold"),bg="green",fg="gold",width=5)
        btn_search.grid(row=0,column=3,padx=1)

        btn_show=Button(table_frame,command=self.fetch_data,text="Show All",font=("arial",11,"bold"),bg="green",fg="gold",width=8)
        btn_show.grid(row=0,column=4,padx=1)




         #======show data table======

        view_table=Frame(table_frame,bd=2,relief=RIDGE)
        view_table.place(x=0,y=50,width=680,height=120)

        scrollx=ttk.Scrollbar(view_table,orient=HORIZONTAL)
        scrolly=ttk.Scrollbar(view_table,orient=VERTICAL)

        self.room_details_table=ttk.Treeview(view_table,column=("contact","check_in","check_out","Room","no_of_hrs","roomtype"),xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)


        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)

        scrollx.config(command=self.room_details_table.xview)
        scrolly.config(command=self.room_details_table.yview)

        self.room_details_table.heading("contact",text="Contact")
        self.room_details_table.heading("check_in",text="Check_in")
        self.room_details_table.heading("check_out",text="Check_out")
        self.room_details_table.heading("Room",text="Room_No")   
        self.room_details_table.heading("no_of_hrs",text="No. of hrs")
        self.room_details_table.heading("roomtype",text="Roomtype")
        
        
        self.room_details_table["show"]="headings"

        self.room_details_table.column("contact",width=100)
        self.room_details_table.column("check_in",width=100)
        self.room_details_table.column("check_out",width=100)
        self.room_details_table.column("Room",width=100)
        self.room_details_table.column("no_of_hrs",width=100)
        self.room_details_table.column("roomtype",width=100)
        
        self.room_details_table.pack(fill=BOTH,expand=1)
        self.room_details_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()
        

          
        #==add data===
    def add_data(self):
        if self.var_contact.get()=="" or self.var_checkin.get()=="":
            messagebox.showerror("Error","All Fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",user="root",password="12345",database="db_customerss")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into short_time_room values(%s,%s,%s,%s,%s,%s)",(
                                                                            self.var_contact.get(),
                                                                            self.var_checkin.get(),
                                                                            self.var_checkout.get(),                                                                          
                                                                            self.var_roomavailable.get(),
                                                                            self.var_noofdays.get(),
                                                                             self.var_roomtype.get()
                                                                            
                                                                            
                                                                        ))
                                                        
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Room booked",parent=self.root)
            except Exception as es:
                messagebox.showwarning("Warning",f"Something went wrong:{str(es)}",parent=self.root)

      #show data in treeview====
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",user="root",password="12345",database="db_customerss")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from short_time_room")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.room_details_table.delete(*self.room_details_table.get_children())
            for i in rows:
                self.room_details_table.insert("",END,values=i)
            conn.commit()
        conn.close()

        #===get cursor data
    def get_cursor(self,event=""):
        cursor_rows=self.room_details_table.focus()
        content=self.room_details_table.item(cursor_rows)
        row=content["values"]

        self.var_contact.set(row[0])
        self.var_checkin.set(row[1])
        self.var_checkout.set(row[2])
        self.var_roomavailable.set(row[3])
        self.var_noofdays.set(row[4])
        self.var_roomtype.set(row[5])

        #update===
    
    def update(self):
        if self.var_contact.get()=="":
            messagebox.showerror("Error","Please Enter Mobile Number",parent=self.root)
        
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="12345",database="db_customerss")
            my_cursor=conn.cursor()
            my_cursor.execute("update short_time_room set check_in=%s,check_out=%s,Room=%s,no_of_hrs=%s,roomtype=%s where contact=%s",(

                                                                                                                    
                                                                                                                    self.var_checkin.get(),
                                                                                                                    self.var_checkout.get(),
                                                                                                                    self.var_roomavailable.get(),
                                                                                                                    self.var_noofdays.get(),
                                                                                                                    self.var_roomtype.get(),
                                                                                                                    self.var_contact.get(),
                                                                                                                  

                                                                                                                                                ))

            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Update","Room details has been updated successfully",parent=self.root)

    
   

    def mdelete_data(self):
        mdelete_data=messagebox.askyesno("Hotel Management System","Do you want to delete this room booked",parent=self.root)
        if mdelete_data>0:
            conn=mysql.connector.connect(host="localhost",username="root",password="12345",database="db_customerss")
            my_cursor=conn.cursor()
            query="delete from short_time_room  where contact=%s"
            value=(self.var_contact.get(),)
            my_cursor.execute(query,value)
        else:
            if not mdelete_data:
                return
        conn.commit()
        self.fetch_data()
        conn.close()







      #====All Data Fetch==================
    def fetch_contact(self):
          if self.var_contact.get()=="":
            messagebox.showerror("Error","please Enter Contact Number",parent=self.root)
          else:
            conn=mysql.connector.connect(host="localhost",username="root",password="12345",database="db_customerss")
            my_cursor=conn.cursor()
            query=("select Ref from tbl_customer where Mobile =%s")
            value=(self.var_contact.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            
            

            if row==None:
                messagebox.showerror("Error","This Number Not Found",parent=self.root)
            else:
               
                conn.commit()
                conn.close()


                showdataframe=Frame(self.root,bd=4,relief=RIDGE,padx=2)
                showdataframe.place(x=455,y=50,width=300,height=220)
                receipt_area=Label(showdataframe,text="Bill Area",font="arial 12 bold",bd=5,relief=GROOVE).pack(fill=X)
                scrol_y=Scrollbar(showdataframe,orient=VERTICAL)
                self.txtarea=Text(showdataframe,yscrollcommand=scrol_y.set)
                scrol_y.pack(side=RIGHT,fill=Y)
                scrol_y.config(command=self.txtarea.yview)
                self.txtarea.pack(fill=BOTH,expand=1)
                
               
                
               

                lblref=Label(showdataframe,text="Ref:",bg="white",font=("arial",12,"bold"))
                lblref.place(x=20,y=40)

                lbl=Label(showdataframe,text=row,bg="white",font=("arial",12,"bold"))
                lbl.place(x=90,y=40)

                #==database Name====
                conn=mysql.connector.connect(host="localhost",username="root",password="12345",database="db_customerss")
                my_cursor=conn.cursor()
                query=("select Lastname from tbl_customer where Mobile =%s")
                value=(self.var_contact.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()

                lblname=Label(showdataframe,bg="white",text="name:",font=("arial",12,"bold"))
                lblname.place(x=20,y=60)

                lbl2=Label(showdataframe,bg="white",text=row,font=("arial",12,"bold"))
                lbl2.place(x=90,y=60)
                




                #======databae Gender

                
                conn=mysql.connector.connect(host="localhost",username="root",password="12345",database="db_customerss")
                my_cursor=conn.cursor()
                query=("select Gender from tbl_customer where Mobile =%s")
                value=(self.var_contact.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()

                lblgender=Label(showdataframe,bg="white",text="Gender:",font=("arial",12,"bold"))
                lblgender.place(x=20,y=80)

                lbl3=Label(showdataframe,bg="white",text=row,font=("arial",12,"bold"))
                lbl3.place(x=90,y=80)
                self.txtarea.insert(END,f"\n\n\n\n\n=================================")
    def reset(self):
        self.var_contact.set("")
        self.var_checkin.set("")
        self.var_checkout.set("")
        self.var_roomavailable.set("")
        self.var_noofdays.set("")
        self.var_paidtax.set("")
        self.var_actualtotal.set("")
        self.var_total.set("")
        self.shortime.set("")
     
    def search_data(self):

        if self.txt_search.get()=="":
            messagebox.showerror("Error","Enter Contact or Room",parent=self.root)

        else:

        
                  
            conn=mysql.connector.connect(host="localhost",username="root",password="12345",database="db_customerss")
            my_cursor=conn.cursor()
            my_cursor.execute('select * from short_time_room where ' +str(self.serch_var.get())+" LIKE '%"+str(self.txt_search.get()+"%'"))
            rows=my_cursor.fetchall()
            if len (rows)!=0:
                self.room_details_table.delete(*self.room_details_table.get_children())
                for i in rows:
                    self.room_details_table.insert("",END,values=i)
               
                conn.commit()
            conn.close()
    def total(self):

            three_hrstime=float(120)
            in_date=self.var_checkin.get()
            out_date=self.var_checkout.get()
            shorttime=float(out_date)-float(in_date)

        

            formulaforthreehrs=float(shorttime*three_hrstime)
            Tax="₱ "+str("%.2f"%((formulaforthreehrs)*0.01))
            St="₱ "+str("%.2f"%((formulaforthreehrs)))
            Tt="₱ "+str("%.2f"%(formulaforthreehrs+((formulaforthreehrs)*0.01)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(St)
            self.var_total.set(Tt)
            self.var_noofdays.set(shorttime) 

        
       
    
            


               



            






       










if __name__=="__main__":
    root=Tk()
    obj=shortRoombooking_window(root)
    root.mainloop()

