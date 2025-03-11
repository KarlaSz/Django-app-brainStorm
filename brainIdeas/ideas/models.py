from django.db import models

# Create your models here.
# #model to jak 1 tabela w bazie danych dlatego sa w liczbie pojedynczej

IDEA_STATUS = (
    ('pending', 'Waiting for review'),
    ('accepted', 'Accepted'),
    ('done', 'Done'),
    ('rejected', 'Rejected')
)

class Idea(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    youtube_url = models.URLField(null=True, blank=True)
    status = models.CharField(choices=IDEA_STATUS, max_length=30, default='pending')

    #z obiektu zrobic string to zrobic metode
    def __str__(self):
        return self.title

# pomysl posiada wiele glosow - Foreign key
class Vote(models.Model):
    idea = models.ForeignKey(Idea, on_delete=models.CASCADE)
    reason = models.TextField()

    def __str__(self):
        return f'Id {self.id}'
