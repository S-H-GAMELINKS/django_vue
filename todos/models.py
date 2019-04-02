from django.db import models

class Todo(mdoels.Model):
    title_text = models.CharField(max_length=30)
    content_text = models.CharField(max_length=140)
