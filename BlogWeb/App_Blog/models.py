from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Blog(models.Model):
    user = models.ForeignKey(User, related_name='blog_user', on_delete=models.CASCADE)
    blog_title = models.CharField(max_length=100,verbose_name='Title')
    slug = models.SlugField(max_length=100,unique=True)
    blog_content = models.TextField(verbose_name='What is your mind?')
    publish_date = models.DateField(auto_now_add=True)
    update_date = models.DateField(auto_now=True)
    blog_image = models.ImageField(upload_to='blog_images', verbose_name='Image')

    class Meta:
        ordering = ('-publish_date',)
    
    def __str__(self):
        return self.blog_title

class Comment(models.Model):
    user = models.ForeignKey(User, related_name='comment_user', on_delete=models.CASCADE)
    blog = models.ForeignKey(Blog, related_name='comment_blog', on_delete=models.CASCADE)
    blog_comment = models.TextField(verbose_name="Comment")
    publish_date = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.blog_comment

class Likes(models.Model):
    user = models.ForeignKey(User, related_name='likes_user', on_delete=models.CASCADE)
    blog = models.ForeignKey(Blog, related_name='likes_blog', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.user.username
    