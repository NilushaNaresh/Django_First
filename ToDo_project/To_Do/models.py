from django.db import models


class ToDoItem(models.Model):
    content = models.TextField(blank=False)
    author = models.CharField(max_length=50)

