from django.db import models


# Create your models here.

# add this
class firstApp(models.Model):
  title = models.CharField(max_length=120)
  description = models.TextField()
  halal = models.BooleanField(default=False)
      
  def __str__(self):
    return self.title
