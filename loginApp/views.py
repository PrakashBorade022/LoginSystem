from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import UserModelForm
from .models import User
from django.db import connections
import mysql.connector
from operator import itemgetter
class LoginAndRegister():
    
    def login(request):
        con = mysql.connector.connect(host="localhost",user="root",passwd="9120",database="loginSystem")
        cursor = con.cursor()
        con2 = mysql.connector.connect(host="localhost",user="root",passwd="9120",database="loginSystem")
        cursor2 = con2.cursor()
        sqlcommand = "select email from loginapp_user"
        sqlcommand2 = "select password from loginapp_user"
        cursor.execute(sqlcommand)
        cursor2.execute(sqlcommand2)
        e=[]
        p=[]
       
        for i in cursor:
            e.append(i)
        for j in cursor2:
            p.append(j)
        res = list(map(itemgetter(0), e))
        res2 = list(map(itemgetter(0), p))    
        con3 = mysql.connector.connect(host="localhost",user="root",passwd="9120",database="loginSystem")
        cursor3 = con2.cursor()

        if request.method =="POST":
            email = request.POST['email']
            password = request.POST['password']
            k=len(res)
            i=1
            sqlcommand3 = "select fname from loginapp_user where email = email"
            cursor3.execute(sqlcommand3)
            lst =[]
            for name in cursor3:
                name = name
                name2 =''.join(name)
            print(name2)
            while i <k:
                if res[i]==email and res2[i]==password:
                   return render(request,'welcome.html',{'name':name2})
                   break
                i+=1
            else:
                messages.info(request,"Check userName or password")
                return redirect('login')

        return render(request,'login.html')   
    def welcome(request):
        return render(request,'welcome.html')     
    def register(request):
        
        if request.method =="POST":
            user = User()
            
            user.fname = request.POST['fname']
            user.lname = request.POST['lname']
            user.email = request.POST['email']
            user.password = request.POST['password']
            user.repassword = request.POST['repassword']
            if user.password!=user.repassword:
                messages.info(request,"Passwords not match")
                return redirect('register')  
            elif user.fname=="" or user.lname=="" or user.email=="" or user.password =="" or user.repassword=="":
                messages.info(request,"Some fields are missing")
                return redirect('register')    
            else:
                messages.info(request,"registration is done go to login")
                user.save()
            
            return render(request,'registration.html')    
        else:
            return render(request,'registration.html')    
            
            
            


                
        
        return render(request,'registration.html')    













# if request.method=="POST":
#             fname = request.POST['fname']
#             lname = request.POST['lname']
#             email = request.POST['email']

#             password = request.POST['password']
#             repassword = request.POST['repassword']
#             if password!=repassword:
#                 messages.info(request,"Passwords not match")
#                 return redirect('register')

#             else:
#                 print("First name",fname)
#                 print("Last Name",lname)
#                 print("Email ",email)
#                 print("Password ",password)
#                 print("Re-password ",repassword)