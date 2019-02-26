from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Post(models.Model):
    author= models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title= models.CharField(max_length=200)
    text= models.TextField()
    create_date= models.DateTimeField(default=timezone.now)
    entrega_date= models.DateField()
    published_date= models.DateTimeField(blank= True, null=True)
    

    def publish(self):
        self.published_date =timezone.now()
        self.save()

    def __str__(self):
        return self.title

    def entrega(self):
        self.entrega_date =timezone.now()
        self.save()
    def approved_comments(self):
        return self.comments.filter(approved_comment=True)       

    
    
class Comment(models.Model):
    post = models.ForeignKey('blog.Post', on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    text = models.TextField(help_text="Sube una imagen respecto al tema, luego nuestro personal lo verificara y lo subira")
    image = models.ImageField(upload_to='blog/images/', blank= True, null=True)
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text
