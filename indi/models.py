from django.db import models


category_choices = [
    ('EN', 'Economie'),
    ('PO', 'Politique'),
    ('EL', 'Ecologie'),
    ('NU', 'Numérique'),
    ('HU', 'Humanités'),
]


class Article(models.Model):
    link = models.URLField()
    user = models.CharField(max_length=30)
    category = models.CharField(max_length=30, choices=category_choices)
    date = models.DateTimeField(auto_now=True)
