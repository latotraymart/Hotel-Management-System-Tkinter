from os import name
from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk
import random
import mysql.connector
from tkinter import messagebox

import numpy as np


from tkinter import filedialog, messagebox
import pandas as pd
import tkinter as tk







class report_window:
    def __init__(self,root):
        self.root=root
        self.root.title("Hotel Management System     | Developed By Group 5 ")
        self.root.geometry("1400x1400+0+225")

        
        
       


         #======title===============
        lbl_title=Label(self.root,text="MONTHLY REPORT",font=("times new roman",20,"bold"),bg="green",fg="gold",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1400,height=50)
         #=====logo==================
        img2=Image.open(r"C:\Hotel Management System\images\winhotel.png")
        img2=img2.resize((100,48),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        lblimg=Label(self.root,image=self.photoimg2,bd=0,relief=RIDGE)
        lblimg.place(x=5,y=2,width=100,height=48)

        #===========Room labelframe======================
        labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="Open File", font=("times new roman",12,"bold"),padx=2)
        labelframeleft.place(x=5,y=50,width=540,height=350)
        
        

        
        
       
        #=buttons
        btn_frame=Frame(labelframeleft,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=200,width=300,height=40)
        
        btnbrowse=Button(btn_frame,text="Browse File",command=lambda:file_dialog(),font=("arial",11,"bold"),bg="green",fg="gold",width=15)
        btnbrowse.grid(row=0,column=0,padx=1)

        btnreset=Button(btn_frame,text="Load File",command=lambda:load_exceldata(),font=("arial",11,"bold"),bg="green",fg="gold",width=15)
        btnreset.grid(row=0,column=1,padx=1)
        lbl_fileselected=Label(labelframeleft,text="No File Selected",font=("times new roman",12,"bold"),padx=2,pady=6)
        lbl_fileselected.place(rely=0.20,relx=0.25)

       

        #tree view frame
        table_frame=LabelFrame(self.root,bd=2,relief=RIDGE,text="Excel Data", font=("arial",12,"bold"),padx=2)
        table_frame.place(x=435,y=55,width=600,height=350)
        
        tv1=ttk.Treeview(table_frame)
        tv1.place(relheight=1,relwidth=1)

        treescrolly=tk.Scrollbar(table_frame,orient="vertical",command=tv1.yview)
        treescrollx=tk.Scrollbar(table_frame,orient="horizontal",command=tv1.xview)
        tv1.configure(xscrollcommand=treescrollx.set,yscrollcommand=treescrolly.set)
        treescrollx.pack(side="bottom",fill="x")
        treescrolly.pack(side="right",fill="y")

        def file_dialog():
            filename=filedialog.askopenfilename(initialdir="/",
                                title="Select A File", 
                                 filetype=(("xlsx files", "*.xlsx"),("All files","*.*")))
            lbl_fileselected["text"]=filename
            return None


      

        
        
        def load_exceldata():
            file_path=lbl_fileselected["text"]
            try:
                excel_filename= r"{}".format(file_path)
                df = pd.read_excel(excel_filename)
            except ValueError:
                tk.messagebox.showerror("Information", "The file you have choosen is invalid")
                return None

            except FileNotFoundError:
                tk.messagebox.showerror("Information", f"No such file as {file_path}")
                return None

            clear_data()
            tv1["column"]=list(df.columns)
            tv1["show"]="headings"
            for column in tv1["columns"]:
                tv1.heading(column, text=column)
            df_rows=df.to_numpy().tolist()
            for row in df_rows:
                tv1.insert("","end", values=row)
            return None
        def clear_data():
                tv1.delete(*tv1.get_children())
        

        
        
        
  
    
      



       







if __name__=="__main__":
    root=Tk()
    obj=report_window(root)
    root.mainloop()
