from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from PIL import Image


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'  


class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

        


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(default='default.jpg')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    likes = models.ManyToManyField(User, related_name='post_likes')
    dislikes =models.ManyToManyField(User, related_name='post_dislikes')
    views =models.PositiveIntegerField(default=0)
    tags = models.ManyToManyField(Tag, blank=True)


    class Meta:
        ordering = ('-created_at',)

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})    

    def __str__(self):
        return self.title 

    def save(self, raw=False, force_insert=False,
                  force_update=False, using=None, update_fields=None):
        super().save()

        img = Image.open(self.image.path)

        if img.height > 770 or img.width > 340:
            output_size = (770,340)
            img.thumbnail(output_size)
            img.save(self.image.path)

    def total_likes(self):
        return self.likes.count() 

    def total_dislikes(self):
        return self.dislikes.count()           


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    comment = models.TextField(blank=True)
    date_commited = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    post = models.ForeignKey(Post, on_delete=models.SET_NULL, null=True, blank=True)
    

    def __str__(self):
        return  f"{self.author.username} commited: {self.comment}"
        

    class Meta:
        ordering = ('-date_commited',)    
    
