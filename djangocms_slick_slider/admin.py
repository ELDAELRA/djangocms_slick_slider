#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import SlickSliderImage

admin.site.register(SlickSliderImage)


class SlickerSliderAceMixin:
    change_form_template = 'djangocms_slick_slider/change_form.html'
