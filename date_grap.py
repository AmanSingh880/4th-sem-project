from tkinter import *
import os
from tkinter import messagebox
import mysql.connector
from datetime import datetime as z
from matplotlib.figure import Figure 
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, 
NavigationToolbar2Tk) 


mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="12345",
    database="sales_report"
)
mycursor = mydb.cursor()
class data_entry_class():
    def __init__(self):
        self.Product_ID = None
        self.Date = None
        self.Product_Name = None
        self.Product_Model = None
        self.Category = None
        self.MRP = None
        self.Product_sold = None

def show_dates():
    mycursor.execute("Select date_of_sale from boat")
    d=[]
    for x in mycursor:
        d.append(x[0])
    dates = [date.day for date in d]
    return list(set(dates))

def show_categories():
    mycursor.execute("Select Distinct category from boat")
    cat=[]
    for x in mycursor:
        cat.append(x[0])
    return cat
root=Tk()
root.title("Sales analytic")
root.geometry('1200x750')
root.config(bg="red")
l=Label(root,text="Sales Analytics",font="Airtel 34",bg="blue", fg="white")
l.place(x=300,y=100)

root.mainloop()
