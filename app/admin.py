from django.contrib import admin

from app.models import Students

# Register your models here.
class StudentsModel(admin.ModelAdmin):
    list_display = ['id','username','fullname','email','phone_number']
    
admin.site.register(Students,StudentsModel)