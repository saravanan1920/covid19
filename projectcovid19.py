from unittest import result
import mysql.connector

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="9976876621",
    database="covid_db"

)
mycursor=mydb.cursor()
#*******************************************************************************************************************
print("-----------------------------------------------------------------")
print("*****************************************************************")
print("COVID19 VECCINATION RECORD")
print("-----------------------------------------------------------------")


print("-------------------------------------")
print("SELECT YOUR CHOOSE")
print("-------------------------------------")
print("press 1|Add a New Member")
print("press 2|add vaccination dose record")
print("press 3|state covid status record")
print("press 4|view member")
print("press 5|view vaccination dose record")
print("press 6|show state covid status record ")
print("--------------------------------------")
print("--------------------------------------")

#Add a New Member
#****************

def insert_data(atharcard_no,name,address,phone_number,Email,age):
    sql="insert into add_member(atharcard_no,name,address,phone_number,Email,age) values(%s,%s,%s,%s,%s,%s)"
    val=(atharcard_no,name,address,phone_number,Email,age)

    mycursor.execute(sql,val)
    mydb.commit()
    print("member added successfully")

#add vaccination dose record
#***************************

def insert_dose(atharcard_number,vaccination_name,dose,vaccination_date):
    sql="insert into vaccination_dose(atharcard_number,vaccination_name,dose,vaccination_date) values(%s,%s,%s,%s)"
    val=(atharcard_number,vaccination_name,dose,vaccination_date)
    mycursor.execute(sql,val)
    mydb.commit()
    print("vaccination record added successfully")

#state covid status record
#*************************

def covid_status(state_name,total_case,new_case,new_death,total_death,new_recovery,total_recovery,date):
    sql="insert into covid_status(state_name,total_case,new_case,new_death,total_death,new_recovery,total_recovery,date) values(%s,%s,%s,%s,%s,%s,%s,%s)"
    val=(state_name,total_case,new_case,new_death,total_death,new_recovery,total_recovery,date)
    mycursor.execute(sql,val)
    mydb.commit()
    print("covid status added successfully")

#view member
#************

def view_member():
    mycursor.execute("select * from add_member")
    result=mycursor.fetchall()
    for i in result:
        print(i)

#view dose
#*********

def view_dose():
    mycursor.execute("select * from vaccination_dose")
    result=mycursor.fetchall()
    for i in result:
        print(i)

#show covid status
#*****************

def show_covid_status():
    mycursor.execute("SELECT * FROM covid_db.vaccination_dose")
    result=mycursor.fetchall()
    for i in result:
        print(i)      
    

user=int(input("enter your choice:"))


if user==1:
    atharcard_no=input("enter your atharcard number:")
    name=input("enter your name:")
    address=input("enter your address:")
    phone_number=input("enter your phone number:")
    Email=input("enter your email:")
    age=input("enter your age:")
    insert_data(atharcard_no,name,address,phone_number,Email,age)


elif user==2:
    atharcard_number=input("enter your atharcard number:")
    vaccination_name=input("enter vaccination name:")
    dose=input("enter 1 for dose1, 2 for dose2:")
    vaccination_date=input("enter the date of vaccination:")
    insert_dose(atharcard_number,vaccination_name,dose,vaccination_date)


elif user==3:
    state_name=input("enter your state name:")
    total_case=input("enter the total case:")
    new_case=input("enter the new case:")
    new_death=input("enter the new death:")
    total_death=input("enter the total death:")
    new_recovery=input("enter the new recovery case:")
    total_recovery=input("enter the total recovery case:")
    date=input("enter the date:")
    covid_status(state_name,total_case,new_case,new_death,total_death,new_recovery,total_recovery,date)    


elif user==4:
    view_member()


elif user==5:
     view_dose()


elif user==6:
    show_covid_status()


else:
    print("---------------------")
    print("SELECT CURRECT CHOICE")
    print("---------------------")