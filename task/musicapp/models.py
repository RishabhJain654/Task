from django.db import models

class IntegerRangeField(models.IntegerField):
    def __init__(self, verbose_name=None, name=None, min_value=None, max_value=None, **kwargs):
        self.min_value, self.max_value = min_value, max_value
        models.IntegerField.__init__(self, verbose_name, name, **kwargs)
    def formfield(self, **kwargs):
        defaults = {'min_value': self.min_value, 'max_value':self.max_value}
        defaults.update(kwargs)
        return super(IntegerRangeField, self).formfield(**defaults)

class Tracks(models.Model):
    title = models.CharField(max_length=30)
    genre = models.CharField(max_length=30)
    rating = IntegerRangeField(min_value=1, max_value=5)

    class Meta:
        db_table = 'tracks'

    def __str__(self):
        return self.title

class Genres(models.Model):
    name = models.CharField(max_length=30)

    class Meta:
        db_table = 'genres'

    def __str__(self):
        return self.title
