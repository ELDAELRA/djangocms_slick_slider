from django.test import TestCase
from django.test.client import RequestFactory

from cms.api import add_plugin
from cms.models import Placeholder
from cms.plugin_rendering import ContentRenderer

from djangocms_slick_slider.cms_plugins import SlickSliderPlugin
from djangocms_slick_slider.models import SlickSlider


class SlickSliderPluginTests(TestCase):

    def test_plugin_context(self):
        placeholder = Placeholder.objects.create(slot='test')
        model_instance = add_plugin(
            placeholder,
            SlickSliderPlugin,
            'de',
        )
        plugin_instance = model_instance.get_plugin_class_instance()
        context = plugin_instance.render(
            {},
            model_instance, None)
        # self.assertEqual(context['instance'], 'Test Slider')

    def test_plugin_html(self):
        placeholder = Placeholder.objects.create(slot='test')
        model_instance = add_plugin(
            placeholder,
            SlickSliderPlugin,
            'de',
        )
        renderer = ContentRenderer(request=RequestFactory())
        from sekizai.context import SekizaiContext
        html = renderer.render_plugin(model_instance, SekizaiContext())
        self.assertIn('id="slider-wrapper"', html)
