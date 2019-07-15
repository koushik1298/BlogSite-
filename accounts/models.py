from django.db import models
from django.contrib import auth
class User(auth.models.User,auth.models.PermissionsMixin):
    def _self_(self):
        return "@{}".format(self.username)

# Create your models here.
