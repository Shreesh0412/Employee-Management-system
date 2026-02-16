import csv
import os

def create():
    f=open("emp.csv","a",newline="")
    cw=csv.writer(f)
    eid=input("Enter New Employee Id: ")
    ename=input("Enter Employee Name: ")
    sal=input("Enter Employee Salary: ")
    rec=[eid,ename,sal]
    cw.writerow(rec)
    print("Record successfully added in csv file")
    f.close()

def read():
    f=open("emp.csv","r")
    cr=csv.reader(f)
    for x in cr:
        print(x)
    f.close()

def update():
    f1=open("emp.csv","r")
    f2=open("temp.csv","w",newline="")
    cr=csv.reader(f1)
    cw=csv.writer(f2)
    neid=input("Enter Employee id to update : ")
    f=0
    for r in cr:
        if r[0]==neid:
            nename=input("Enter new name of the Employee: ")
            nsal=input("Enter new Salary of the Employee: ")
            t=[neid,nename,nsal]
            cw.writerow(t)
            f=1
        else:
            cw.writerow(r)
    f1.close()
    f2.close()
    os.remove("emp.csv")
    os.rename("temp.csv","emp.csv")
    if f==1:
        print("Record successfully Updated")
    else:
        print("Sorry, Record of Employee not found")

def delete():
    f1=open("emp.csv","r")
    f2=open("temp.csv","w",newline="")
    cr=csv.reader(f1)
    cw=csv.writer(f2)
    neid=input("Enter Employee for delete in csv")
    f=0
    for r in cr:
        if r[0]==neid:
            f=1
        else:
            cw.writerow(r)
    f1.close()
    f2.close()
    os.remove("emp.csv")
    os.rename("temp.csv","emp.csv")
    if f==1:
        print("Record successfully Deleted")
    else:
        print("Sorry, Record of Employee not found")

def search():
    f1=open("emp.csv","r")
    cr=csv.reader(f1)
    neid=input("Enter Employee ID for SEARCH : ")
    f=0
    for r in cr:
        if r[0]==neid:
            f=1
            print(r)
        if f==0:
            print("Sorry, Record of Employee not found")