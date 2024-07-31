import datetime
from django.contrib import admin



from django.db import models
from django.utils import timezone
from django.urls import reverse



# todo_list/todo_app/models.py
def one_week_hence():
    return timezone.now() + timezone.timedelta(days=7)

class ToDoList(models.Model):
    title = models.CharField(max_length=100, unique=True)

    def get_absolute_url(self):
        return reverse("test:list", args=[self.id])

    def __str__(self):
        return self.title

class ToDoItem(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField(default=one_week_hence)
    todo_list = models.ForeignKey(ToDoList, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse("test:item-update", args=[str(self.todo_list.id), str(self.id)]
        )

    def __str__(self):
        return f"{self.title}: due {self.due_date}"

    """class Meta:
        ordering = ["due_date"]"""




class ToDo_task(models.Model):
    toDo_task_text = models.CharField(max_length=200)

    created_date_time = models.DateTimeField("date and time this task got created")
    task_start_date_time = models.DateTimeField("date and time where this task starts")
    task_deadline_date_time = models.DateTimeField("deadline(date and time) of this tasks ")

    # id_of_creator as foreign_key?
    #id_of_creator = models.ForeignKey()

    def __str__(self):
        return self.toDo_task_text

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("data published")
    
    def __str__(self):
        return self.question_text
    
    @admin.display(
        boolean=True,
        ordering="pub_date",
        description="Published recently?",
    )
    def was_published_recently(self):
        now = timezone.now()
        return now >= self.pub_date >= now - datetime.timedelta(days=1)
    
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
    