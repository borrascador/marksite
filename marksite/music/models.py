# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Song(models.Model):
    title = models.CharField(max_length=255)
    source = models.FileField(upload_to='songs')

    def publish(self):
        self.save()

    def __str__(self):
        return self.title
