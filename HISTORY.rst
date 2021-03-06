.. :changelog:

History
-------

0.6.2 (2019-03-19)
++++++++++++++++++

* Remove change_form_template `change_form.html`.
* Remove SlickerSliderAceMixin class.


0.6.1 (2019-03-19)
++++++++++++++++++

* Add `autoplay` and `autoplay_speed` fields on `SlickSlider` model.
* Add CKEditor on change_form when user add new SlickSliderImage form


0.6.0 (2019-03-14)
++++++++++++++++++

* Use djangocms_text_ckeditor as widget on slide image caption field.
* On `SlickSliderImage` model, change TextField to djangocms_text_ckeditor HTMLField.
* Add (`speed`, `slides_to_show`, `arrows`, `dots`) fields on `SlickSlider` model.
* Update on save `SlickSlider.settings` with (`speed`, `slides_to_show`, `arrows`, `dots`) fields.


0.5.0 (2018-02-01)
++++++++++++++++++

* Made title and settings not required anymore
* Added support for multiple sliders on one page
* Fixed bug, which made arrow color option not work
* reworked the example project so you can use it with preconfigured data
* changed default arrow color to a darker gray (:code:`#666`)

0.2.4 (2017-10-13)
++++++++++++++++++

* fixed jsonfield default error due to encoding


0.2.2 (2017-10-13)
++++++++++++++++++

* bug fixes that caused whitenoise to crash due to relative paths


0.2.1 (2017-10-13)
++++++++++++++++++

* bug fixes that cause the slider not to show up
* better python 3 compatibility

0.2.0 (2017-10-13)
++++++++++++++++++

* major database change
* fixed many bugs
* you need to completey delete the old db and use the new one


0.1.4 (2017-10-13)
++++++++++++++++++

* changed structure of settings


0.1.2 (2017-10-13)
++++++++++++++++++

* added django-cms as dependency to pypi package (setup.py)


0.1.1 (2017-10-12)
++++++++++++++++++

* fixed github link in setup.py

0.1.0 (2017-10-12)
++++++++++++++++++

* First release on PyPI.
