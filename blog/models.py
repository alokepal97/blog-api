from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from random import randint
from django.utils.text import slugify
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    url = models.SlugField(unique=True)
    insdate = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if Post.objects.filter(title=self.title).exists():
            extra = str(randint(1, 10000))
            self.url = slugify(self.title) + "-" + extra
        else:
            self.url = slugify(self.title)
        super(Post, self).save(*args, **kwargs)
