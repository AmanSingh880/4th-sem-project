from tkinter import *
import pickle
import os
from tkinter import messagebox
    
def main_call():
    os.system("main.py")

def reset_password(password):
    def validate_password_reset(password):
        Upper_case=Num=Spec_char=False
        if(len(password)<8):
            messagebox.showwarning("Sales Analytic","Password must have 8 characters")
            return False
        for i in password:
            if(i.isupper()):
                Upper_case=True
            elif(not(i.isalnum())):
                Spec_char=True
            elif(i.isdigit()):
                Num=True
        if(Upper_case and Num and Spec_char):
            return True
        else:
            if(Upper_case):
                if(Num):
                    messagebox.showwarning("Sales Analytic","Password must have special character")
                else:
                    messagebox.showwarning("Sales Analytic","Password must have digits(0-9)")
            elif(Num):
                if(Upper_case):
                    messagebox.showwarning("Sales Analytic","Password must have special character(@-#)")
                else:
                    messagebox.showwarning("Sales Analytic","Password must have Uppercase character(A-Z)")
            else:
                if(Num):
                    messagebox.showwarning("Sales Analytic","Password must have Uppercase character(A-Z)")
                else:
                    messagebox.showwarning("Sales Analytic","Password must have digits(0-9)")
            return False

    
    if(validate_password_reset(password)):
        file=open("binary.bin","wb")
        pickle.dump(password,file)
        file.close()
        messagebox.showwarning("Sales Analytic","Password Changed")
        return True
    else:
        messagebox.showwarning("Sales Analytic","Retry ")
        return False
root=Tk()
root.title("Sales analytic")
root.geometry('1200x800')
root.configure(bg="red")
l=Label(root,text="Welcome to Sales Analytics",font="Airtel 34",bg="blue", fg="white")
l.place(x=300,y=100)
def Validate_password(password):
    valid=False
    try:
        file=open("binary.bin","rb")
        original_password=pickle.load(file)
        if(original_password==password):
            valid=True
            file.close()
            return True
        else:
            messagebox.showwarning("Sales Analytic","Incorrect Password")
            file.close()
            return False
    except:
        messagebox.showwarning("Sales Analytic","Data not Found")
    finally:
        return valid
def f1():
    password=var.get()
    vali=Validate_password(password)
    print(vali)
    if(vali):
        print("Succesfull")
        root.destroy()
        main_call()
    else:
        print("Failed")
def f2():
    messagebox.showwarning("Sales Analytic","Enter New Password in Password feild then reclick on Reset Button\n if Already entered please ignore")
    password=var.get()
    reset_password(password)


l1=Label(root,text="Enter the password",font="Airtel 15",bg="white",fg="black")
l1.place(x=100,y=300)
var=StringVar()
l2=Entry(root,text=var,bg="sky blue",fg="dark blue",font="Airtel 15")
l2.place(x=300,y=300)
l3=Button(root,text="Submit" ,bg="blue",fg="white",font="Airtel 15",command=f1)
l3.place(x=200,y=400)
l4=Button(root,text="Reset" ,bg="blue",fg="white",font="Airtel 15",command=f2)
l4.place(x=200,y=500)
a=Button(root,text="Exit",bg="blue",fg="White",font="Arial 20",command=root.destroy)
a.place(x=20,y=700)
root.mainloop()
