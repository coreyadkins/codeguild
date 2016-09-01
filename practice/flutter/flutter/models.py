"""flutter Models."""

from django.db import models

class Flutt(models.Model):
    author = models.TextField()
    body = models.TextField()
    timestamp = models.DateTimeField()

    def __str__(self):
        return self.author.name, self.body, self.timestamp.isoformat()

    def __repr__(self):
        return 'User(author={}, body={!r}, timestamp={})'.format(self.author, self.body, self.timestamp)
