# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import customer,disaster
admin.site.register(customer)
admin.site.register(disaster)



