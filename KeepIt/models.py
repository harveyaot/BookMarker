#!/usr/bin/env python
#! -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

class Profile(models.Model):
    user = models.OneToOneField(User)
    avatarImage = models.ImageField(upload_to='photos/avatars', blank=True, null=True)

def create_user_profile(sender, instance, created, **kwargs):
    if created:
        profile, created = Profile.objects.get_or_created(user=instance)

post_save.connect(create_user_profile, sender=User)

class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True, db_index=True)

    def __unicode__(self):
        return self.name

class Url(models.Model):
    url = models.URLField(max_length=255, unique=True, db_index=True)
    title = models.CharField(max_length=255, null=True, blank=True)
    abstract = models.TextField(null=True, blank=True)

    def __unicode__(self):
        return self.url

class UserUrl(models.Model):
    user = models.ForeignKey(User)
    url = models.ForeignKey(Url)
    note = models.TextField(null=True, blank=True)
    time = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return "[%s][%s]" % (user, url)

    class Meta:
        unique_together = ('user', 'url')
    
class UserUrlTag(models.Model):
    user = models.ForeignKey(User)
    url = models.ForeignKey(Url)
    tag = models.ForeignKey(Tag)
    time = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return "[%s][%s][%s]" % (user, url, tag)

    class Meta:
        unique_together = ('user', 'url', 'tag')
