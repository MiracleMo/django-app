from django.contrib import admin

from test.models import ToDo_task, ToDoItem, ToDoList
# Register your models here.
admin.site.register(ToDo_task)
admin.site.register(ToDoItem)
admin.site.register(ToDoList)
