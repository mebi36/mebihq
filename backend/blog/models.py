from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.api import APIField

class BlogPage(Page):
    intro = models.CharField(max_length=255)
    body = RichTextField(blank=True, features=['h2', 'h3', 'bold', 'italic', 'link', 'image', 'code', 'embed'])

    content_panels = Page.content_panels + [
        FieldPanel('intro'),
        FieldPanel('body')
    ]


    api_fields = [
        APIField('intro'),
        APIField('body'),
    ]