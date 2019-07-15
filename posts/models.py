from django.db import models
from django.urls import reverse
from django.conf import settings
from groups.models import Group
from  django.contrib.auth import get_user_model
User=get_user_model()

class Post(models.Model):
    user=models.ForeignKey(User,related_name='posts',on_delete=models.PROTECT,unique=True)
    created_at=models.DateTimeField(auto_now=True)
    message=models.TextField(unique=True)
    message_html=models.TextField(editable=False)
    group=models.ForeignKey(Group,related_name='posts',null=True,blank=True,on_delete=models.PROTECT)

    def __str__(self):
        return self.message

    def save(self,*args,**kwargs):
        # self.message_html=misaka.html(self.message
        super().save(*args,**kwargs)

    def get_success_url(self):
        return reverse('groups:single',kwargs={'slug':self.object.slug})



    class Meta:
        ordering=['-created_at']
        unique_together=['user','message']






# Create your models here.
