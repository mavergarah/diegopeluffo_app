from django.db import models
from django_summernote.fields import SummernoteTextField

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
        max_length=5000,
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
