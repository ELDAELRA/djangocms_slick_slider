# -*- coding: utf-8 -*-
from __future__ import unicode_literals, division

from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from .forms import SlickSliderForm
from .helpers import get_slider_image_dimensions
from .models import SlickSlider, SlickSliderImage
from djangocms_text_ckeditor import settings as text_settings


class SlickSliderImageInline(admin.TabularInline):
    model = SlickSliderImage
    extra = 1


@plugin_pool.register_plugin
class SlickSliderPlugin(CMSPluginBase):
    """
    The main Slick Slider Plugin. Here, we can define various settings
    and behavior of the plugin.

    This Plugin adds a Slick Slider Plugin to Django CMS. You can add
    images as inline objects. The images will be rendered as thumbnails.


    You can define `SLICK_SLIDER_CONTAINER_WIDTH` to change the behaviors.
    Check :class:`helpers.get_slider_image_dimensions` for more information.
    """
    model = SlickSlider
    form = SlickSliderForm
    name = _('Slick Slider')
    render_template = 'djangocms_slick_slider/base.html'
    cache = False
    inlines = [SlickSliderImageInline, ]

    def render_change_form(self, request, context, **kwargs):
        context['ckeditor_conf'] = text_settings.CKEDITOR_SETTINGS
        return super(SlickSliderPlugin, self).render_change_form(request, context, **kwargs)

    def render(self, context, instance, placeholder):
        context = super(SlickSliderPlugin, self).render(
            context, instance, placeholder)

        # define context vars
        images = instance.images.all()
        child_width = get_slider_image_dimensions(4)
        context.update({
            'images': images,
            'child_width': child_width}
        )

        return context
