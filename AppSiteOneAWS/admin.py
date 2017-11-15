# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.

from .models import Question
from .models import BlogAssunto
from .models import BlogComments

admin.site.register (Question)
admin.site.register (BlogAssunto)
admin.site.register (BlogComments)