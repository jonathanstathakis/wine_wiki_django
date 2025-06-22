from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import default, slugify
from django.utils.translation import autoreload_started
from django.urls import reverse


class Producer(models.Model):
    """represents a producer"""

    producer_name = models.CharField(max_length=100)
    region = models.CharField(max_length=100)
    description = models.TextField(help_text="Description of the producer")

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.producer_name)
        super(Producer, self).save(*args, **kwargs)


class WineListCategory(models.Model):
    """
    Represents the wine list structure
    """

    order = models.IntegerField()
    category = models.CharField(max_length=100, primary_key=True)

    def __str__(self):
        return str(self.category)


class WineListSubCat(models.Model):
    """
    mixin class for wine list subcategories
    """

    winelistcategory_pk = models.ForeignKey(WineListCategory, on_delete=models.PROTECT)
    order = models.IntegerField()
    subcategory = models.CharField(max_length=100, primary_key=True)

    def __str__(self):
        return str(self.subcategory)


class Wine(models.Model):
    """base class representing a wine object"""

    winelistcategory_pk = models.ForeignKey(
        WineListCategory, on_delete=models.PROTECT, null=True
    )
    winelistsubcat_pk = models.ForeignKey(
        WineListSubCat, on_delete=models.PROTECT, null=True
    )
    wine_name = models.CharField(max_length=100, blank=True)
    vintage = models.CharField(max_length=4, blank=True)
    region = models.CharField(max_length=100, blank=True)
    subregion = models.CharField(max_length=100, blank=True)
    country = models.CharField(max_length=100, blank=True)
    variety = models.CharField(max_length=100, blank=True)
    producer = models.CharField(max_length=100, blank=True)
    is_published = models.BooleanField(default=False, verbose_name="Publish?")
    created_on = models.DateTimeField(auto_now_add=True)
    bpos_key = models.CharField(max_length=100, blank=True)
    price = models.IntegerField(blank=True)
    description = models.TextField(blank=True)

    """represents a wine wiki wine"""

    def get_absolute_url(self):
        return reverse("wine", kwargs={"pk": self.pk})

    def __str__(self):
        return f"{self.vintage} {self.wine_name} {self.region} {self.subregion}"

    def winesearcher_str(self):
        """assemble a string that matches winesearcher"""
        return f"{self.producer} {self.wine_name} {self.variety} {self.subregion} {self.region}/{self.vintage}".replace(
            " ", "+"
        ).replace("++", "+")  # in the event of null fields

    def search_eng_str(self):
        """assemble a string that matches winesearcher"""
        return f"{self.producer} {self.wine_name} {self.variety} {self.subregion} {self.region} {self.vintage}".replace(
            " ", "+"
        ).replace("++", "+")  # in the event of null fields
