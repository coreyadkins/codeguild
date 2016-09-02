"""flutter Models."""

from django.db import models
import datetime

class Flutt(models.Model):
    """Flutt model stores a single Flutt, including its author, author id, the text or body of the Flutt, and a
    timestamp for the time of posting.
    """
    author = models.TextField()
    author_id = models.IntegerField()
    body = models.TextField()
    timestamp = models.DateTimeField()

    def __str__(self):
        """Return str.

        >>> str(Flutt(author='adkinsbass', author_id=0, body='Hi!', timestamp=datetime.datetime(2016, 9, 2, 10, 28, 35)))
        'Flutt(adkinsbass, Hi!)'
        """
        return 'Flutt({}, {})'.format(self.author, self.body)

    def __repr__(self):
        """Return repr.

        >>> repr(Flutt(author='adkinsbass', author_id=0, body='Hi!', timestamp=datetime.datetime(2016, 9, 2, 10, 28, 35\
                )))
        "Flutt(author='adkinsbass', body='Hi!', timestamp=2016-09-02 10:28:35, author_id=0)"
        """
        return 'Flutt(author={!r}, body={!r}, timestamp={}, author_id={})'.format(self.author, self.body, self.timestamp,
                                                                                 self.author_id)
