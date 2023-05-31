from tkinter import*
from PIL import Image,ImageTk
from customer import customer_window
from report import report_window
from room import Roombooking_window
from details import Detailsroom_window
from shortroom import shortRoombooking_window





class HotelManagementSystem:
    def __init__(self,root):
        self.root=root
        self.root.title("Hotel Management System     | Developed By Group 5 ")
        self.root.geometry("1550x800+0+0")
        
        #=======1st image========
        img1=Image.open(r"C:\Hotel Management System\images\HOTELMOTOS.jpg")
        img1=img1.resize((1150,150),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        lblimg=Label(self.root,image=self.photoimg1,bd=4,relief=RIDGE)
        lblimg.place(x=220,y=0,width=1150,height=150)

        #=====logo==================
        img2=Image.open(r"C:\Hotel Management System\images\winwin.jpg")
        img2=img2.resize((230,150),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        lblimg=Label(self.root,image=self.photoimg2,bd=4,relief=RIDGE)
        lblimg.place(x=0,y=0,width=230,height=150)


         #============right side image================
        img3=Image.open(r"C:\Hotel Management System\images\bghotel1.jpg")
        img3=img3.resize((1500,590),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        lblimg11=Label(self.root,image=self.photoimg3,bd=4,relief=RIDGE)
        lblimg11.place(x=0,y=150,width=1500,height=590)

        

       
        #==========menu==============

      

        #=========button frame=========
        btn_frame=Frame(self.root,bd=4,relief=RIDGE)
        btn_frame.place(x=0,y=150,width=1400,height=45)

        custom_btn=Button(btn_frame,text="CUSTOMER",command=self.customer_details,width=20,font=("times new roman",15,"bold"),bg="green",fg="gold",bd=0,cursor="hand1")
        custom_btn.grid(row=0,column=0,pady=1)

        lroom_btn=Button(btn_frame,text="ROOM",command=self.booking,width=20,font=("times new roman",15,"bold"),bg="green",fg="gold",bd=0,cursor="hand1")
        lroom_btn.grid(row=0,column=1,pady=1)

       

        details_btn=Button(btn_frame,text="DETAILS",command=self.newroomdetails,width=20,font=("times new roman",15,"bold"),bg="green",fg="gold",bd=0,cursor="hand1")
        details_btn.grid(row=0,column=2,pady=1)

        report_btn=Button(btn_frame,text="REPORT",width=20,command=self.report,font=("times new roman",15,"bold"),bg="green",fg="gold",bd=0,cursor="hand1")
        report_btn.grid(row=0,column=3,pady=1)
        
        LOGOUT_btn=Button(btn_frame,text="LOGOUT",width=30,command=self.logout,font=("times new roman",15,"bold"),bg="green",fg="gold",bd=0,cursor="hand1")
        LOGOUT_btn.grid(row=0,column=4,pady=1)


        

      

       

        #==========downside iamge=========

        #img4=Image.open(r"C:\Hotel Management System\images\diamond.jpg")
        #img4=img4.resize((230,250),Image.ANTIALIAS)
        #self.photoimg4=ImageTk.PhotoImage(img4)

        #lblimg11=Label(main_frame,image=self.photoimg4,bd=4,relief=RIDGE)
        #lblimg11.place(x=0,y=220,width=230,height=250)


        #img5=Image.open(r"C:\Hotel Management System\images\food.jpg")
        #img5=img5.resize((230,80),Image.ANTIALIAS)
        #self.photoimg5=ImageTk.PhotoImage(img5)

        #lblimg12=Label(main_frame,image=self.photoimg5,bd=4,relief=RIDGE)
        #lblimg12.place(x=0,y=420,width=230,height=80)


    def customer_details(self):
        self.new_window=Toplevel(self.root)
        self.app=customer_window(self.new_window)

        
        

    def booking(self):
        self.new_window=Toplevel(self.root)
        self.app=Roombooking_window(self.new_window)

    def newroomdetails(self):
        self.new_window=Toplevel(self.root)
        self.app=Detailsroom_window(self.new_window)

  

    def report(self):
        self.new_window=Toplevel(self.root)
        self.app=report_window(self.new_window)


    def logout(self):
        self.root.destroy()
        
        

        


        













        







if __name__== "__main__":
    root=Tk()
    obj=HotelManagementSystem(root)
    root.mainloop()



