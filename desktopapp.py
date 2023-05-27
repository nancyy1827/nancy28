from tkinter import *
import mysql.connectro


def create_conn():
    return mysql.connector.connect(
        host="localhost",
        username="root",
        password="

root=Tk()
root.geometry("350x480")
root.title("employee Registration")
root.resizable(width=False,height=False)


l_empid=Label(root,text="EMP-ID",font=("Arial",10))
l_empid.place(x=50,y=50)

l_ename=Label(root,text="EMP NAME",font=("Arial",10))
l_ename.place(x=50,y=100)

l_job=Label(root,text="JOB",font=("Arial",10))
l_job.place(x=50,y=150)

l_email=Label(root,text="EMAIL",font=("Arial",10))
l_email.place(x=50,y=200)

l_hiredate=Label(root,text="HIREDATE",font=("Arial",10))
l_hiredate.place(x=50,y=250)

e_empid=Entry(root)
e_empid.place(x=150,y=50)

e_ename=Entry(root)
e_ename.place(x=150,y=100)


e_job=Entry(root)
e_job.place(x=150,y=150)

e_email=Entry(root)
e_email.place(x=150,y=200)


e_hiredate=Entry(root)
e_hiredate.place(x=150,y=250)

insert=Button(root,text="INSERT",bg="black",fg="white",font=("Cambria",12))
insert.place(x=80,y=320)

search=Button(root,text="SEARCH",bg="black",fg="white",font=("Cambria",12))
search.place(x=180,y=320)

update=Button(root,text="UPDATE",bg="black",fg="white",font=("Cambria",12))
update.place(x=80,y=390)

delete=Button(root,text="DELETE",bg="black",fg="white",font=("Cambria",12))
delete.place(x=180,y=390)

















