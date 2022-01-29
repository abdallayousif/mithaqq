from django.db import models
from acount.models import UserBase
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager, PermissionsMixin)
from random import randrange



CHARSET = '0123456789'
LENGTH = 4
MAX_TRIES = 32




class Marketers(models.Model):
    
    user = models.ForeignKey(UserBase, on_delete=models.CASCADE)
    refrens = models.CharField(max_length=255, editable=True, unique=True, blank=True)
   

    is_tts = models.BooleanField(default=False)
    is_ts =  models.BooleanField(default=False)

    
    def save(self, *args, **kwargs):
        """
        Upon saving, generate a code by randomly picking LENGTH number of
        characters from CHARSET and concatenating them. If code has already
        been used, repeat until a unique code is found, or fail after trying
        MAX_TRIES number of times. (This will work reliably for even modest
        values of LENGTH and MAX_TRIES, but do check for the exception.)
        Discussion of method: http://stackoverflow.com/questions/2076838/
        """
        loop_num = 0
        unique = False
        while not unique:
            if loop_num < MAX_TRIES:
                new_code = 'MQ'
                for i in range(LENGTH): # TODO: change to xrange() for python 2
                    new_code += CHARSET[randrange(0, len(CHARSET))]
                if not Marketers.objects.filter(refrens=new_code):
                    self.refrens = new_code
                    unique = True
                loop_num += 1
            else:
                raise ValueError("Couldn't generate a unique code.")
        super(Marketers, self).save(*args, **kwargs)
    
    

    def __str__(self):
        return self.user.user_name
    
class MarketersComisions(models.Model):
    marketers = models.ForeignKey(Marketers, on_delete=models.CASCADE, related_name='comisions')
    comisions =  models.FloatField()
    
    def __str__(self):
        return self.marketers.refrens 
    
    
class Ecard(models.Model):
    ecard = models.CharField(max_length=255, editable=True, unique=True, blank=True)
    is_use = models.BooleanField(default=False)
    
    def save(self, *args, **kwargs):
        """
        Upon saving, generate a code by randomly picking LENGTH number of
        characters from CHARSET and concatenating them. If code has already
        been used, repeat until a unique code is found, or fail after trying
        MAX_TRIES number of times. (This will work reliably for even modest
        values of LENGTH and MAX_TRIES, but do check for the exception.)
        Discussion of method: http://stackoverflow.com/questions/2076838/
        """
        loop_num = 0
        unique = False
        while not unique:
            if loop_num < MAX_TRIES:
                new_code = 'EC'
                for i in range(LENGTH): # TODO: change to xrange() for python 2
                    new_code += CHARSET[randrange(0, len(CHARSET))]
                if not Ecard.objects.filter(ecard=new_code):
                    self.ecard = new_code
                    unique = True
                loop_num += 1
            else:
                raise ValueError("Couldn't generate a unique code.")
        super(Ecard, self).save(*args, **kwargs)
    
    def __str__(self):
        return self.ecard    
        
# Create your models here.
class Campany(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)

    class Meta:
        verbose_name_plural = 'Campany'

    def get_absolute_url(self):
        return reverse("metheqq_root:campany_list", args=[self.slug])

    def __str__(self):
        return self.name


class MangerWord(models.Model):
    name = models.CharField(max_length=100)
    iamge = models.ImageField()
    word = models.TextField(max_length=255)
    postion = models.CharField(max_length=100)
    
    
    def __str__(self):
        return self.name