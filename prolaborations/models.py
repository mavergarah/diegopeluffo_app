from django.db import models
from .data import KIND_CHOICES

class Project(models.Model):
    title = models.TextField(
        max_length=200,
        blank=True,
        null=True,
        verbose_name="Project Title",
    )

    description = models.TextField(
        max_length=3000,
        blank=True,
        null=True,
        verbose_name="Project Description",
    )

    url = models.URLField(
        max_length=300,
        blank=True,
        null=True,
        verbose_name="Project URL"
    )


    kind_of_project = models.PositiveSmallIntegerField(
        choices=KIND_CHOICES,
        verbose_name='Kind of Project',
        null=False,
        blank=False,
        default=200
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Project"
        verbose_name_plural = "Projects"
