from django.urls import reverse
from django.db import models


class Author(models.Model):

    class Meta:
        ordering = ('name',)

    name = models.CharField(max_length=100, unique=True)
    date_of_birth = models.DateField()
    date_of_death = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.name


class Quotation(models.Model):
    author = models.ForeignKey(Author, related_name='underquoted',
                               on_delete=models.CASCADE)
    text = models.CharField(max_length=500, unique=True)

    class Meta:
        ordering = ('id',)

    def __str__(self):
        return "%s - %s" % (self.text, self.author.name)

    def get_absolute_url(self):
        return reverse('show_quotation', args=[self.pk])
