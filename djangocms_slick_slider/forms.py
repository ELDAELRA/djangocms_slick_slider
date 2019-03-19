# -*- coding: utf-8 -*-
from __future__ import absolute_import

from django import forms

from .models import SlickSlider


class SlickSliderForm(forms.ModelForm):
    model = SlickSlider
