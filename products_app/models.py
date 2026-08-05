from django.db import models


class Category(models.Model):

    name = models.CharField(
        max_length=100
    )


    def str(self):
        return self.name