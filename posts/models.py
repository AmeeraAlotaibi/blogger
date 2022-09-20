from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    genders = [
        ("female", "female"),
        ("male", "male"),
        ("unknown", "unknown"),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="user")
    image = models.ImageField()
    bio = models.CharField(max_length=350)
    gender = models.CharField(max_length=15, choices=genders, default='unknown')
    occupation = models.CharField(max_length=100)
    birth_date = models.DateField(null=True, blank=True)
    date_joined = models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.user.first_name}'s Profile"



class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name



class Post(models.Model):
    author = models.ManyToManyField(User, related_name='author')
    title = models.CharField(max_length=250)
    content = models.TextField()
    cover_image = models.ImageField()
    length = models.TimeField(default="10:00")
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_created=True)
    tags = models.ManyToManyField(Tag, related_name="tags")

    def __str__(self):
        return f"{self.title} by {self.author}"




class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.PROTECT, related_name='posts')
    commentor = models.ManyToManyField(User, related_name='commentor')
    comment = models.TextField()
    # likes and dislikes field here

    def __Str__(self):
        return self.commentor.first_name