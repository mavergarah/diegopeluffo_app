from django.db import models
from .data import KIND_CHOICES, THESIS_CHOICES

class Project(models.Model):
    title = models.TextField(
        max_length=400,
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

class Collaborations(models.Model):
    title = models.TextField(
        max_length=400,
        blank=True,
        null=True,
        verbose_name="Collaboration Title",
    )

    url = models.URLField(
        max_length=300,
        blank=True,
        null=True,
        verbose_name="Collaboration URL"
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Collaboration"
        verbose_name_plural = "Collaborations"

class ThesisAdvisory(models.Model):
    title = models.TextField(
        max_length=400,
        blank=True,
        null=True,
        verbose_name="Thesis Title",
    )

    url = models.URLField(
        max_length=300,
        blank=True,
        null=True,
        verbose_name="Thesis URL"
    )

    authors = models.TextField(
        max_length=100,
        blank=True,
        null=True,
        verbose_name="Author",
    )

    kind_of_thesis = models.PositiveSmallIntegerField(
        choices=THESIS_CHOICES,
        verbose_name='Kind of Thesis',
        null=False,
        blank=False,
        default=200
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Thesis"
        verbose_name_plural = "Theses"

class Teaching(models.Model):
    title = models.TextField(
        max_length=400,
        blank=True,
        null=True,
        verbose_name="Course Title",
    )

    description = models.TextField(
        max_length=3000,
        blank=True,
        null=True,
        verbose_name="Course Description",
    )

    url = models.URLField(
        max_length=300,
        blank=True,
        null=True,
        verbose_name="Course URL"
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Course"
        verbose_name_plural = "Courses"
