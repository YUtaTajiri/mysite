from django.db import models

# Create your models here.
class News(models.Model):
    title = models.CharField(max_length=10)
    url = models.URLField()
    def __str__(self):
        return self.title
