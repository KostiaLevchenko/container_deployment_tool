from django.db import models


class Container(models.Model):
    image = models.CharField(max_length=25)
    cmd = models.CharField(max_length=25)

    def __str__(self):
        return self.image

    def run_container(self):
        pass
