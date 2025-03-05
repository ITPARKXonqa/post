from django.db import models
from django.utils import timezone

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=150)
    content = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    views = models.IntegerField()
    author = models.ForeignKey(
        'auth.User',
        on_delete= models.CASCADE    
    )
    
    def __str__(self):
        return self.title