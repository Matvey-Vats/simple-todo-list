from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Task(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    is_completed = models.BooleanField(default=True)
    time_create = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return f"User: {self.user} | Task: {self.title}"
            
    class Meta:
        verbose_name = "Завданя"
        verbose_name_plural = "Завдання"
        ordering = ['-time_create']
        indexes = [
            models.Index(fields=['-time_create'])
        ]