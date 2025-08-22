from django.shortcuts import render,redirect
from .models import Contact,LeagalService,Feedback,User,LegalAdvisor
from django.contrib import messages
# Create your views here.
def home(request):
    feedback = Feedback.objects.all()
    data=[]
    for f in feedback:
       data.append(
          {
             "rating":f.rating,
             "remark":f.remark,
             "name":f.name,
             "profile_pic":User.objects.get(email=f.email).profile_pic
          }
       )
       feedback_dict={
          "feedback_key":data
       }
       
    return render(request,'legal_app/html/index.html',feedback_dict)




def contact_us(request):
 if request.method=="GET":
  return render(request,'legal_app/html/contact_us.html')
 if request.method=="POST":
    user_name=request.POST["name"]
    user_email=request.POST["email"]
    user_phone=request.POST["phone"]
    user_query=request.POST["query"]

    user_obj=Contact(name=user_name,email=user_email,phone=user_phone,query=user_query)
    user_obj.save()
 messages.success(request,"🙏Thankyou for your time🙏")
 return redirect("contact_us")
 

def about_us(request):
    return render(request,'legal_app/html/about_us.html')

def views_services(request):
     service_list=LeagalService.objects.all()
     context= {

    "service_key":service_list
     }
     return render(request,'legal_app/html/views_services.html',context)



def views_advisors(request):
     advisor_list=LegalAdvisor.objects.all()
     context= {

    "advisor_key":advisor_list
     }
     return render(request,'legal_app/html/views_advisors.html',context)


     
