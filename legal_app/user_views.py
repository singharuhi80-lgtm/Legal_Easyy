from django.shortcuts import render,redirect
from .models import User,Feedback,LegalAdvisor,ClientDocument
from django.contrib import messages

def user_feedback(request):
  if request.method=="GET":
    return render(request,'legal_app/user/user_feedback.html')
  if request.method=="POST":
   user_email=request.session["web_key"]
   user_name=request.POST["name"]
  #  user_feedback=request.POST["review"]
   user_rating=request.POST["rating"]
   user_remarks=request.POST["remarks"]

  feedback_obj=Feedback(name=user_name,email=user_email,rating=user_rating,remark=user_remarks)
  feedback_obj.save()
  messages.success(request,"Thankyou for your time")
  return redirect("user_feedback")

def user_logout(request):
  request.session.flush()
  messages.success(request,"Successfully logged out!!!")
  return redirect("user_login")


def user_advisors(request):
     advisor_list=LegalAdvisor.objects.all()
     context= {

    "advisor_key":advisor_list
     }
     return render(request,'legal_app/user/user_advisors.html',context)



def upload_document(request):
 
    if request.method=="GET":
      return render(request,'legal_app/user/upload_document.html')
    if request.method=="POST":
      user_email=request.session["web_key"]
      user_Obj=User.objects.get(email=user_email)
      doc_name=request.POST["name"]
      advisor_email=request.POST["email"]
      doc_description=request.POST["description"]
      doc_pic=request.FILES.get("document_pic")
      doc_obj=ClientDocument(user=user_Obj,advisor_email=advisor_email,document_name=doc_name,document_description=doc_description,document_pic=doc_pic)
      doc_obj.save()
      messages.success(request,"document uploaded successfully")
      return redirect("upload_document")



def user_edit_profile(request):
   
    if request.method=="GET":
             user_email=request.session["web_key"]
             User_Obj=User.objects.get(email=user_email)
             user_dict={
                "user_key":User_Obj
                }
             return render(request,'legal_app/user/user_edit_profile.html',user_dict)
    


    if request.method=="POST":
             user_name=request.POST["name"]
             user_phone=request.POST["phone"]
             user_pic=request.FILES.get("pic")
             user_email=request.session["web_key"]
             User_Obj=User.objects.get(email=user_email)
             if user_pic is not None:
              User_Obj.profile_pic=user_pic
             User_Obj.name=user_name
             User_Obj.phone=user_phone
             User_Obj.save()
             messages.success(request,"Profile updated Succesfully👍") 
             return redirect("user_home")

def user_home(request):
  ####fetching email from session to indentify the user
  if request.method=="GET":
    user_email=request.session["web_key"]
    user_obj=User.objects.get(email=user_email) #it will return a single object
    ####sending data from view to html (template)page
    ##create a dictinary and bind data with a key
    ######send that dic with render function
    user_dict={
      "user_key":user_obj
    }

  return render(request,"legal_app/user/user_home.html",user_dict)
  


def user_login(request):
    if request.method=="GET":
     return render(request,'legal_app/user/user_login.html')
    if request.method=="POST":
      user_email=request.POST["Email"]
      user_pass=request.POST["Password"]
      ##select * from user where email=useremail and password=userpass
      user_list=User.objects.filter(email=user_email,password=user_pass)
    if len(user_list)>0:
     request.session["web_key"]=user_email 
       #########binding email in a session to tract
       ####3user for multiple request
     return redirect("user_home")

    else:
     messages.error(request,"Invalid Credentails")
    return redirect("user_login")



def user_registration(request):
 if request.method=="GET":
    return render(request,'legal_app/user/user_registration.html')
 if request.method=="POST":
      user_email=request.POST["Email"]   #####control name input field
      user_password=request.POST["Password"]
      user_name=request.POST["Name"]
      user_phone=request.POST["PhoneNumber"]
      user_pic=request.FILES["profile_pic"]
      ##ORMapping frameworks###
      ###create object of user model
      ##set values
      #####save object-> it automatically stores values in table

      user_obj=User(name=user_name,email=user_email,password=user_password,phone=user_phone,profile_pic=user_pic)
      user_obj.save()
      return redirect("user_login")
