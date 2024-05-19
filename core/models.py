from django.db import models
from taggit.managers import TaggableManager

from authusers.models import User



class Category(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title
    

class Technology(models.Model):
    title = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = "Technologies"

    def __str__(self):
        return self.title
    
    
class Project(models.Model):
    title = models.CharField(max_length=100)
    description =  models.TextField()
    start_date = models.DateTimeField(auto_now_add=True)
    client = models.CharField(max_length=100)
    champion = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    team = models.ManyToManyField("TeamMember", related_name="projects")
    tag = TaggableManager()
    technology_used = models.ManyToManyField(Technology, related_name="projects")

    views = models.PositiveIntegerField(default=0)

    image = models.ImageField(upload_to="project_images")

    image_1 = models.ImageField(upload_to="project_images")
    image_2 = models.ImageField(upload_to="project_images")

    def __str__(self):
        return self.title
    

class TeamMember(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100, null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='team_images')

    def __str__(self):
        return self.name


class Testimonial(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    content = models.TextField(null=True)

    def __str__(self):
        return self.user.username


class Comment(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.content




