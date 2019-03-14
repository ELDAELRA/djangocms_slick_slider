# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.dispatch import receiver
from django.db.models.signals import pre_save
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _
from djangocms_text_ckeditor.fields import HTMLField
from cms.models.pluginmodel import CMSPlugin
from filer.fields.image import FilerImageField
from jsonfield import JSONField


@python_2_unicode_compatible
class SlickSlider(CMSPlugin):
    """
    Main Plugin Model for the slider.
    """
    class Meta:
        verbose_name = _('slick slider')
        verbose_name_plural = _('slick sliders')

    title = models.CharField(
        verbose_name=_('slider title'),
        max_length=255,
        null=True, blank=True)

    settings = JSONField(
        verbose_name=_('slick settings'),
        blank=True, null=True,
        help_text=_(
            'Check <a href="http://kenwheeler.github.io/slick/" '
            'target="_blank">'
            'Slick Documentation</a> for possible settings '
            '<br>'
            'Use JSON format and check the errors in the editor<br>'
            'You can also use online JSON validators'))

    speed = models.PositiveIntegerField(
        verbose_name=_('Speed (ms)'),
        default=300)

    slides_to_show = models.PositiveIntegerField(
        verbose_name=_('Slides to show'),
        default=1)

    arrows = models.BooleanField(
        verbose_name=_('Arrows'),
        default=True)

    arrow_color = models.CharField(
        verbose_name=_('arrow color'),
        max_length=255,
        default="#666",
        help_text=_('Define the color of slider arrows here. All CSS '
                    'color values work (e.g. #efefef).'))
    dots = models.BooleanField(
        _('Dots'),
        default=True)

    def copy_relations(self, oldinstance):
        """
        Take an instance and copy the images of that instance to this
        instance.
        """
        for image in oldinstance.images.all():
            image.pk = None
            image.slider = self
            image.save()

    def __str__(self):
        """
        String representation of SlickSlider class.
        """
        return "{title}".format(title=self.title)


@receiver(pre_save, sender=SlickSlider)
def settings_handler(sender, instance, **kwargs):
    """ Update `instance.settings` with slide settings form fields
    """
    instance.settings['speed'] = instance.speed
    instance.settings['arrows'] = instance.arrows
    instance.settings['dots'] = instance.dots
    instance.settings['slidesToShow'] = instance.slides_to_show
    return


@python_2_unicode_compatible
class SlickSliderImage(models.Model):
    """
    Image model für SlickSlider class.
    """
    class Meta:
        verbose_name = _('slider image')
        verbose_name_plural = _('slider images')

    slider = models.ForeignKey(
        SlickSlider,
        related_name="images")

    image = FilerImageField(
        verbose_name=_('slider Image'),
        related_name='slider_images_filer')

    link = models.URLField(
        verbose_name=_('image link'),
        null=True, blank=True)

    link_target = models.BooleanField(
        verbose_name=_('image link target'),
        help_text=_('open link in new window'),
        default=True)

    caption_text = HTMLField(
        _('caption text'),
        null=True,
        blank=True)

    def __str__(self):
        """
        String representation of SlickSliderImage class.
        """
        return "{filename}".format(filename=self.image.original_filename)
