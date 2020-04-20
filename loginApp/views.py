from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import UserModelForm
from .models import User
class LoginAndRegister():
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