# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Articles(models.Model):
    items_id = models.AutoField(primary_key=True)
    contenttype = models.CharField(max_length=100, blank=True, null=True)
    title = models.CharField(max_length=255)
    url_page = models.CharField(max_length=255, blank=True, null=True)
    url_pdf = models.CharField(max_length=255, blank=True, null=True)
    url_doi = models.CharField(max_length=255, blank=True, null=True)
    publicationname = models.CharField(max_length=255, blank=True, null=True)
    doi = models.CharField(unique=True, max_length=255, blank=True, null=True)
    publicationdate = models.DateField(blank=True, null=True)
    abstract = models.TextField(blank=True, null=True)
    category = models.CharField(max_length=100, blank=True, null=True)
    author =  models.ManyToManyField('Authors', through='BookAuthors')

    class Meta:
        managed = True
        db_table = 'articles'


class Authors(models.Model):
    author_id = models.AutoField(primary_key=True)
    author_name = models.CharField(unique=True, max_length=255)
    

    class Meta:
        managed = False
        db_table = 'authors'
    
    def __str__(self):
        return self.author_name
    


class BookAuthors(models.Model):
    items = models.OneToOneField(Articles, models.DO_NOTHING, primary_key=True)
    author = models.ForeignKey(Authors, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'book_authors'
        unique_together = (('items', 'author'),)
