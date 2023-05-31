from tkinter import*

from PIL import Image,ImageTk
from tkinter import ttk
import random
from time import strftime
from datetime import datetime
import mysql.connector
from tkinter import messagebox


class Detailsroom_window:
    def __init__(self,root):
        self.root=root
        self.root.title("Hotel Management System     | Developed By Group 5 ")
        self.root.geometry("1400x1400+0+225")
         #======title===============
        lbl_title=Label(self.root,text="NEW ROOM  DETAILS",font=("times new roman",20,"bold"),bg="green",fg="gold",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1400,height=50)
         #=====logo==================
        img2=Image.open(r"C:\Hotel Management System\images\winhotel.png")
        img2=img2.resize((100,48),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        lblimg=Label(self.root,image=self.photoimg2,bd=0,relief=RIDGE)
        lblimg.place(x=5,y=2,width=100,height=48)

        #===========Room labelframe======================
        labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="New Room Add", font=("times new roman",12,"bold"),padx=2)
        labelframeleft.place(x=5,y=50,width=540,height=350)

         #==floor===
        lbl_floor=Label(labelframeleft,text="Floor",font=("times new roman",12,"bold"),padx=2,pady=6)
        lbl_floor.grid(row=0,column=0,sticky=W)

        self.var_floor=StringVar()
        enty_floor=ttk.Entry(labelframeleft,textvariable=self.var_floor,font=("times new roman",13,"bold"),width=20)
        enty_floor.grid(row=0,column=1,sticky=W)


        #==Room no
        lbl_room=Label(labelframeleft,text="Room no.",font=("times new roman",12,"bold"),padx=2,pady=6)
        lbl_room.grid(row=1,column=0,sticky=W)

        self.var_roomno=StringVar()
        enty_room=ttk.Entry(labelframeleft,textvariable=self.var_roomno,font=("times new roman",13,"bold"),width=20)
        enty_room.grid(row=1,column=1,sticky=W)

        #==Room type
        lbl_roomtype=Label(labelframeleft,text="Room type",font=("times new roman",12,"bold"),padx=2,pady=6)
        lbl_roomtype.grid(row=2,column=0,sticky=W)

        self.var_roomtype=StringVar()
        enty_roomtype=ttk.Entry(labelframeleft,textvariable=self.var_roomtype,font=("times new roman",13,"bold"),width=20)
        enty_roomtype.grid(row=2,column=1,sticky=W)

       

         #========buttons========
        btn_frame=Frame(labelframeleft,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=200,width=448,height=40)
        
        btnadd=Button(btn_frame,text="Add",command=self.add_data,font=("arial",11,"bold"),bg="green",fg="gold",width=11)
        btnadd.grid(row=0,column=0,padx=1)

        btnupdate=Button(btn_frame,text="Update",command=self.update,font=("arial",11,"bold"),bg="green",fg="gold",width=11)
        btnupdate.grid(row=0,column=1,padx=1)

        btndelete=Button(btn_frame,text="Delete",command=self.mdelete_data,font=("arial",11,"bold"),bg="green",fg="gold",width=11)
        btndelete.grid(row=0,column=2,padx=1)

        btnrReset=Button(btn_frame,text="Reset",command=self.reset,font=("arial",11,"bold"),bg="green",fg="gold",width=11)
        btnrReset.grid(row=0,column=3,padx=1)

        table_frame=LabelFrame(self.root,bd=2,relief=RIDGE,text="View Details and  Search", font=("arial",12,"bold"),padx=2)
        table_frame.place(x=435,y=55,width=600,height=350)

        scrollx=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scrolly=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.room_details_table=ttk.Treeview(table_frame,column=("Floor","Roomno","Roomtype"),xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)


        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)

        scrollx.config(command=self.room_details_table.xview)
        scrolly.config(command=self.room_details_table.yview)

        self.room_details_table.heading("Floor",text="Floor")
        self.room_details_table.heading("Roomno",text="Room_no")
        self.room_details_table.heading("Roomtype",text="Roomtype")
       
        
        self.room_details_table["show"]="headings"

        self.room_details_table.column("Floor",width=100)
        self.room_details_table.column("Roomno",width=100)
        self.room_details_table.column("Roomtype",width=100)
        
       
        self.room_details_table.pack(fill=BOTH,expand=1)
        self.room_details_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()

         #==add data=== 
    def add_data(self):
        if self.var_floor.get()=="" or self.var_roomtype.get()=="":
            messagebox.showerror("Error","All Fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",user="root",password="12345",database="dbcustomer")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into rdetails values(%s,%s,%s)",(
                                                                            self.var_floor.get(),
                                                                            self.var_roomno.get(),
                                                                            self.var_roomtype.get()
                                                                            
                                                                            
                                                                        ))
                                                        
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","New room Added Successfully",parent=self.root)
            except Exception as es:
                messagebox.showwarning("Warning",f"Something went wrong:{str(es)}",parent=self.root)




    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="12345",database="dbcustomer")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from rdetails")
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

        self.var_floor.set(row[0])
        self.var_roomno.set(row[1])
        self.var_roomtype.set(row[2])


        #update===
    
    def update(self):
        if self.var_floor.get()=="":
            messagebox.showerror("Error","Please Enter floor number",parent=self.root)
        
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="12345",database="dbcustomer")
            my_cursor=conn.cursor()
            my_cursor.execute("update rdetails set Floor=%s,Roomtype=%s where Roomno=%s",(

                                                                                                                    
                                                                                                                    self.var_floor.get(),
                                                                                                                    self.var_roomtype.get(),
                                                                                                                    self.var_roomno.get()
                                                                                                                   

                                                                                                                                                ))

            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Update","New Room has been updated successfully",parent=self.root)


    #==delete data
    def mdelete_data(self):
        mdelete_data=messagebox.askyesno("Hotel Management System","Do you want to delete this New Room Details",parent=self.root)
        if mdelete_data>0:
            conn=mysql.connector.connect(host="localhost",user="root",password="12345",database="dbcustomer")
            my_cursor=conn.cursor()
            query="delete from rdetails  where Roomno=%s"
            value=(self.var_roomno.get(),)
            my_cursor.execute(query,value)
        else:
            if not mdelete_data:
                return
        conn.commit()
        self.fetch_data()
        conn.close()

    def reset(self):
        self.var_floor.set("")
        self.var_roomno.set("")
        self.var_roomtype.set("")


        

        

       

        





if __name__=="__main__":
    root=Tk()
    obj=Detailsroom_window(root)
    root.mainloop()


