from django.db import models

# This first model is for Journal. It will have the BibBase URL
class JournalInfo(models.Model):
    bibbase_url = models.URLField(
        max_length=300,
        blank=True,
        null=True,
        verbose_name="BibBase URL"
    )

    def __str__(self):
        return self.bibbase_url

    class Meta:
        verbose_name = "Journal"
        verbose_name_plural = "Journals"

class BookInfo(models.Model):
    title = models.TextField(
        max_length=100,
        blank=True,
        null=True,
        verbose_name="Title",
    )

    publishing = models.TextField(
        max_length=100,
        blank=True,
        null=True,
        verbose_name="Publishing",
    )

    authors = models.TextField(
        max_length=100,
        blank=True,
        null=True,
        verbose_name="Authors",
    )

    isbn = models.TextField(
        max_length=100,
        blank=True,
        null=True,
        verbose_name="ISBN",
    )

    category = models.TextField(
        max_length=100,
        blank=True,
        null=True,
        verbose_name="Category",
    )

    book_url = models.URLField(
        max_length=300,
        blank=True,
        null=True,
        verbose_name="Book URL"
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Book"
        verbose_name_plural = "Books"

class ThesesInfo(models.Model):
    title = models.TextField(
        max_length=100,
        blank=True,
        null=True,
        verbose_name="Title",
    )

    author = models.TextField(
        max_length=100,
        blank=True,
        null=True,
        verbose_name="Authors",
    )

    theses_url = models.URLField(
        max_length=300,
        blank=True,
        null=True,
        verbose_name="Book URL"
    )

    category = models.TextField(
        max_length=100,
        blank=True,
        null=True,
        verbose_name="Category",
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Theses"
        verbose_name_plural = "Theses"
