from django.contrib import admin
from .models import Contact,Feedback,User ,LegalAdvisor,LeagalService,ClientDocument
class Contact_Admin(admin.ModelAdmin):
    list_display=["name","email","phone","query","date"]
class Feedback_Admin(admin.ModelAdmin):
    list_display=["name","email","rating","remark","date"]
class User_Admin(admin.ModelAdmin):
    list_display=["name","email","password","phone","profile_pic","date"]
# class LegalAdvisor_Admin(admin.ModelAdmin):
    # list_display=["name","email","password","phone","qualification","profile_pic","experience","skills","services"]
class LeagalService_Admin(admin.ModelAdmin):
    list_display=["service_type","service_description","service_pic"]
class ClientDocument_Admin(admin.ModelAdmin):
    list_display=["user","advisor_email","document_name","document_description","document_pic","date"]



admin.site.register(Contact,Contact_Admin)
admin.site.register(Feedback,Feedback_Admin)
admin.site.register(User,User_Admin)
admin.site.register(LegalAdvisor)
admin.site.register(LeagalService,LeagalService_Admin)
admin.site.register(ClientDocument,ClientDocument_Admin)

admin.site.site_header="Law Firm Admin Dashboard"
admin.site.site_title="Find Your Best Way Of Justice"
admin.site.index_title="Legal Firm"