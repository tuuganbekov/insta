from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=255)
    descr = models.TextField()
    author = models.ForeignKey(
            User, on_delete=models.CASCADE,
            related_name='authors', null=True
    )
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'post'

    def __str__(self):
        return f"{self.title}--{self.id}"

class Image(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='insta_projects/')
    post = models.ForeignKey(
        Post, related_name='posts',
        on_delete=models.CASCADE)

    class Meta:
        db_table = 'images'

    def __str__(self):
        return f"{self.image.url}"


class HashTag(models.Model):
    title = models.CharField(max_length=255)
    posts = models.ManyToManyField(Post)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'hash'

    def __str__(self):
        return self.title




