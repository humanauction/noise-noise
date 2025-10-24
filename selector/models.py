from django.db import models


class AudioFile(models.Model):
    name = models.CharField(max_length=100)
    file = models.FileField(upload_to='audio/')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
