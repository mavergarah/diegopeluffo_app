from django.db import models
from django_summernote.fields import SummernoteTextField
from .data import LINKS_CHOICES, RESEARCH_CHOICES

# Create your models here.
class PersonalInfo(models.Model):
    website = models.URLField(
        max_length=200,
        blank=True,
        null=True,
        verbose_name="Personal Website"
    )

    email = models.EmailField(
        max_length=254,
        unique=True,
        verbose_name="Email"
    )

    profile = SummernoteTextField(
        max_length=10000,
        blank=True,
        null=True,
        verbose_name="Professional Profile",
    )

    city = models.TextField(
        max_length=100,
        blank=True,
        null=True,
        verbose_name="City",
    )

    phone = models.CharField(
        max_length=20,
        blank=True,
        null=True
    )

    profile_photo = models.ImageField(
        upload_to='uploads',
        blank=True,
        null=True
    )

    researchgate_url = models.URLField(
        max_length=200,
        blank=True,
        null=True,
        verbose_name="ResearchGate URL"
    )

    linkedin_url = models.URLField(
        max_length=200,
        blank=True,
        null=True,
        verbose_name="LinkedIn URL"
    )

    twitter_url = models.URLField(
        max_length=200,
        blank=True,
        null=True,
        verbose_name="Twitter URL"
    )

    facebook_url = models.URLField(
        max_length=200,
        blank=True,
        null=True,
        verbose_name="Facebook URL"
    )

    def __str__(self):
        return self.city

    class Meta:
        verbose_name = "Personal Info"
        verbose_name_plural = "Infos"

class LinkInterest(models.Model):
    title = models.TextField(
        max_length=200,
        blank=True,
        null=True,
        verbose_name="Link Title",
    )

    url = models.URLField(
        max_length=300,
        blank=True,
        null=True,
        verbose_name="Link URL"
    )

    kind_of_link = models.PositiveSmallIntegerField(
        choices=LINKS_CHOICES,
        verbose_name='Kind of Link',
        null=False,
        blank=False,
        default=200
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Link"
        verbose_name_plural = "Links"

class ResearchLine(models.Model):
    title = models.TextField(
        max_length=200,
        blank=True,
        null=True,
        verbose_name="Research Title",
    )

    description = models.TextField(
        max_length=3000,
        blank=True,
        null=True,
        verbose_name="Research Description",
    )

    kind_of_research = models.PositiveSmallIntegerField(
        choices=RESEARCH_CHOICES,
        verbose_name='Kind of Research',
        null=False,
        blank=False,
        default=200
    )

    url = models.URLField(
        max_length=300,
        blank=True,
        null=True,
        verbose_name="Research URL"
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Research"
        verbose_name_plural = "Researches"

class DownloadDocument(models.Model):
    title = models.TextField(
        max_length=200,
        blank=True,
        null=True,
        verbose_name="Link Title",
    )

    document = models.FileField(
        upload_to='documents/'
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Download Document"
        verbose_name_plural = "Download Documents"
