from django.db import models
from datetime import datetime
# Create your models here.

class File(models.Model):
    file_name = models.CharField(max_length=255, default="no name")
    content = models.TextField(default="")
    date = models.DateTimeField(default=datetime.today())

    def __str__(self):
        return self.file_name
