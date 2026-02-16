import csv
import os

def create():
    f=open("emp.csv","a",newline="")
    cw=csv.writer(f)
    eid=input("/n Enter New Employee Id: ")
    ename=input("Enter Employee Name: ")
    eno=input("Enter Employee's Mobile Number: ")
    sal=input("Enter Employee Salary: ")
    dept=input("Enter the department of the Employee: ")
    mn=input("Enter the Name of Employee's Manager: ")
    cno=input("Enter the Cabin Number of the Employee: ")
    add=input("Enter Employee's Address of Residence: ")
    bg=input("Enter Employee's Blood Group: ")
    rec=[eid,ename,eno,sal,dept,mn,cno,add,bg]
    cw.writerow(rec)
    print("Record successfully added in csv file")
    f.close()

def read():
    f=open("emp.csv","r")
    cr=csv.reader(f)
    for i in cr:
        print("Employee ID: ",i[0],end=" | ")
        print("Employee's Name: ",i[1],end=" | ")
        print("Employee's Mobile Number: ",i[2],end=" | ")
        print("Employee's Salary: ",i[3],end=" | ")
        print("Employee's Department: ",i[4],end=" | ")
        print("Employee's Manager Name: ",i[5],end=" | ")
        print("Employee's Cabin Number: ",i[6],end=" | ")
        print("Employee's Address of Residence: ",i[7],end=" | ")
        print("Employee's Blood Group: ",i[8])
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
            nno=input("Enter the new Mobile number of the Employee: ")
            nsal=input("Enter new Salary of the Employee: ")
            ndept=input("Enter new Department of the Employee: ")
            nmg=input("Enter the new Manager of the Employee: ")
            ncb=input("Enter the new Cabin Number of the Employee: ")
            nadd=input("Enter new Address of the Employee: ")
            nbg=input("Enter the new Blood Group of the Employee: ")
            t=[neid,nename,nno,nsal,ndept,nmg,ncb,nadd,nbg]
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
    neid=input("Enter Employee ID to delete the data: ")
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
            print("Employee ID: ",r[0])
            print("Employee's Name: ",r[1])
            print("Employee's Mobile Number: ",r[2])
            print("Employee's Salary: ",r[3])
            print("Employee's Department: ",r[4])
            print("Employee's Manager Name: ",r[5])
            print("Employee's Cabin Number: ",r[6])
            print("Employee's Address of Residence: ",r[7])
            print("Employee's Blood Group: ",r[8])
    if f==0:
        print("Sorry, Record of Employee not found")