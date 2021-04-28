from django.contrib import admin
from .models import Setting
from .models import ContactFormMessage
class ContactFormAdmin(admin.ModelAdmin):
    list_display = ['name','email','subject','status']
    liist_filter = ['status']
# Register your models here.


admin.site.register(Setting)
admin.site.register(ContactFormMessage,ContactFormAdmin)