from django.contrib import admin
from. models import TaskDetails
# Register your models here.
@admin.register(TaskDetails)
class TaskDetailsAdmin(admin.ModelAdmin):
  list_display=('id','Task_name','Task_status')