from django.db import models

# Create your models here.

class Author(models.Model):
    id = models.IntegerField(primary_key=True)
    birth_year = models.SmallIntegerField(null=True, blank=True)
    death_year = models.SmallIntegerField(null=True, blank=True)
    name = models.CharField(max_length=128)

    def __str__(self):
        return f"{self.name} {self.birth_year}"
    
class Book(models.Model):
    id = models.IntegerField(primary_key=True)
    download_count = models.IntegerField(default=0, null=True, blank=True)
    gutenberg_id = models.IntegerField()
    media_type = models.CharField(max_length=16)
    title = models.CharField(max_length=1024, null=True, blank=True)
    
    def __str__(self):
        return f"{self.title} {self.media_type}"
    
    
class Language(models.Model):
    id= models.IntegerField(primary_key=True)
    code = models.CharField(max_length=5)
    
    def __str__(self):
        return self.code
    

class BookAuthor(models.Model):
    id = models.IntegerField(primary_key=True)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    
class Subject(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=256)

class BookBookshelf(models.Model):
    id = models.IntegerField(primary_key=True)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    bookshelf_id = models.IntegerField()

class BookLanguage(models.Model):
    id = models.IntegerField(primary_key=True)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    language_id = models.IntegerField()

class BookSubject(models.Model):
    id = models.IntegerField(primary_key=True)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    subject_id = models.IntegerField()

class Bookshelf(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=64)

class Format(models.Model):
    id = models.IntegerField(primary_key=True)
    mime_type = models.CharField(max_length=32)
    url = models.CharField(max_length=256)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
