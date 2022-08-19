from django.db import models
from django import forms
import wagtail
from rest_framework import serializers
from rest_framework.fields import Field
from wagtail.contrib.routable_page.models import RoutablePageMixin, route
from wagtail.core import blocks
from wagtail.core.models import Page
from wagtail.core.fields import StreamField
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel, MultiFieldPanel
from wagtail.images.blocks import ImageChooserBlock
from wagtail.api import APIField
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.images.api.fields import ImageRenditionField
from wagtail_headless_preview.models import HeadlessPreviewMixin
from wagtail.snippets.models import register_snippet
from modelcluster.fields import ParentalKey, ParentalManyToManyField
from modelcluster.contrib.taggit import ClusterTaggableManager
from taggit.models import TaggedItemBase


class ImageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = wagtail.images.get_image_model()
        fields = ['id','title', 'usage_url', 'file', 'width', 'height']


class APIImageChooserBlock(ImageChooserBlock):
    def get_api_representation(self, value, context=None):
        return ImageSerializer(context=context).to_representation(value)


@register_snippet
class BlogAuthor(models.Model):
    """Blog author for snippets."""

    name = models.CharField(max_length=100)
    website = models.URLField(blank=True, null=True)
    bio = models.TextField(verbose_name="Bio")
    image = models.ForeignKey(
        "wagtailimages.Image",
        on_delete=models.SET_NULL,
        null=True,
        blank=False,
        related_name="+",
    )

    panels = [
        MultiFieldPanel(
            [
                FieldPanel("name"),
                
                ImageChooserPanel("image")
            ],
            heading="Name and Image",
        ),
        MultiFieldPanel([FieldPanel("bio")], heading="Bio"),
        MultiFieldPanel(
            [
                FieldPanel("website"),
            ],
            heading="Links"
        )
    ]

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Blog Author'
        verbose_name_plural = "Blog Authors"

class BlogPageTag(TaggedItemBase):
    content_object = ParentalKey('BlogPage', related_name='taged_items', on_delete=models.CASCADE)


@register_snippet
class BlogCategory(models.Model):
    """Blog category"""

    name = models.CharField(max_length=255)
    slug = models.SlugField(
        verbose_name="slug",
        allow_unicode=True,
        max_length=255,
        help_text='A slug to identify posts by this category'
    )

    panels = [
        FieldPanel("name"),
        FieldPanel("slug")
    ]

    class Meta:
        verbose_name = "Blog Category"
        verbose_name_plural = "Blog Categories"
        ordering = ["name"]


    def __str__(self):
        return self.name


class CustomTagSerializer(Field):
    """Custom Tag Serializer."""
    
    def to_representation(self, value):
        return [
            {
                "name": tag.name,
                "slug": tag.slug,
                "pk": tag.pk,
            }
            for tag in value.all()
        ]


class BlogPage(HeadlessPreviewMixin, RoutablePageMixin, Page):
    tags = ClusterTaggableManager(through=BlogPageTag, blank=True)
    intro = models.CharField(max_length=255)
    body = StreamField([
        ("heading", blocks.CharBlock(classname="full title", icon="title")),
        ("paragraph", blocks.RichTextBlock(icon="pilcrow")),
        ("image", APIImageChooserBlock(icon="image")),
    ])
    image = models.ForeignKey('wagtailimages.Image', null=True, blank=True, on_delete=models.SET_NULL)
    categories = ParentalManyToManyField("blog.BlogCategory", blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('intro'),
        StreamFieldPanel('body'),
        FieldPanel('tags'),
        ImageChooserPanel('image'),
        MultiFieldPanel(
            [
                FieldPanel("categories", widget=forms.CheckboxSelectMultiple)
            ],
            heading="Categories"
        ),
    ]

    api_fields = [
        APIField('intro'),
        APIField('body'),
        APIField('image_thumbnail', serializer=ImageRenditionField('fill-300x300', source='image')),
        APIField('tags', serializer=CustomTagSerializer()),
        APIField("categories"),
    ]


class BlogChildPageSerializer(Field):
    def to_representation(self, child_pages):
        return_posts = []
        for child in child_pages:
            post_dict = {
                'id': child.id,
                'title': child.title,
                'slug': child.slug,
                'url': child.url,
            }
            return_posts.append(post_dict)
        return return_posts

