import imp
from django.db import models

from wagtail.core import blocks
from wagtail.core.models import Page
from wagtail.core.fields import StreamField
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.images.blocks import ImageChooserBlock
from wagtail.api import APIField
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.images.api.fields import ImageRenditionField
from wagtail_headless_preview.models import HeadlessPreviewMixin


class BlogPage(HeadlessPreviewMixin, Page):
    intro = models.CharField(max_length=255)
    # body = RichTextField(blank=True, features=['h2', 'h3', 'bold', 'italic', 'link', 'image', 'code', 'embed'])
    body = StreamField([
        ("heading", blocks.CharBlock(classname="full title", icon="title")),
        ("paragraph", blocks.RichTextBlock(icon="pilcrow")),
        ("image", ImageChooserBlock(icon="image")),
    ])
    image = models.ForeignKey('wagtailimages.Image', null=True, blank=True, on_delete=models.SET_NULL)

    content_panels = Page.content_panels + [
        FieldPanel('intro'),
        StreamFieldPanel('body'),
        ImageChooserPanel('image'),
    ]


    api_fields = [
        APIField('intro'),
        APIField('body'),
        APIField('image_thumbnail', serializer=ImageRenditionField('fill-300x300', source='image'))
    ]