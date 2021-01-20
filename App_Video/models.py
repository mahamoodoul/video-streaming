from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    # video_category = (
    # (1, "Funny"),
    # (2, "English"),
    # (3, "Bangla"),
    # (4, "Movies"),
    # (5, "Drama"),
    # (6, "Trending"),
    # (7, "All Time Favorite"),
    # )
    category = models.CharField(max_length=264, verbose_name="Mention your Category")

    def __str__(self):
        return str(self.category)




class Video(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='video_author')
    video_category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='video_cat')
    vidoe_title = models.CharField(max_length=264, verbose_name="Put a Title")
    slug = models.SlugField(max_length=264, unique=True)
    video_description = models.TextField(verbose_name="What is on your mind abot video description?")
    video_link = models.URLField(verbose_name="Enter the Youtube video link here")
    publish_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-publish_date',]

    def __str__(self):
        return self.vidoe_title





class Feedback(models.Model):
    video = models.ForeignKey(Video, on_delete=models.CASCADE, related_name='video_comment')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_comment')
    comment = models.TextField()
    comment_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-comment_date',)

    def __str__(self):
        return self.comment
