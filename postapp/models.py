from django.db import models
from django.db.models.fields import *

class Post(models.Model):
    title = CharField(max_length=100)
    content = TextField()
    created_at = DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title
