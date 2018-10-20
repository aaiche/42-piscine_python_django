from django.db import models

#
# class Movies herite de models.Model qui est importe depuis django.db
# a l interieur de la class: je defini mes champs sous forme d attributs
# ensuite on donne les types de nos champs, ie models.CharField(max_length=32)
# ces types sont contenus dans models sous forme de membres
# le membre CharField qui correspond au type varchar
#
class Movies(models.Model):
    title = models.CharField(max_length=64, unique=True, null=False)
    episode_nb = models.IntegerField(primary_key=True)
    opening_crawl = models.TextField(null=True)
    director = models.CharField(max_length=32, null=False)
    producer = models.CharField(max_length=128, null=False)
    release_date = models.DateField(null=False)
    def __str__(self):
        return self.title
