from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')

    author = models.CharField(max_length=100)
    book = models.FileField(upload_to='uploads/')
    publication_date = models.DateField()

    def __str__(self):
        return self.title