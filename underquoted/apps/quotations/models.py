from django.core.urlresolvers import reverse
from django.db import models


class Author(models.Model):

    name = models.CharField(max_length=100, unique=True)
    date_of_birth = models.DateField()
    date_of_death = models.DateField(null=True, blank=True)

    def __str__(self):
        death_year = ''
        if self.date_of_death:
            death_year = self.date_of_death.year
        return "%s (%s-%s)" % (self.name, self.date_of_birth.year,
                               death_year)


class Quotation(models.Model):

    author = models.ForeignKey(Author, related_name='underquoted')
    text = models.CharField(max_length=500, unique=True)

    def __str__(self):
        return "%s - %s" % (self.text, self.author.name)

    def get_absolute_url(self):
        return reverse('show_quotation', args=[self.pk])
