from django.db import models
from django.contrib.auth.models import AbstractUser

class MyUser(AbstractUser):
    username = models.CharField(max_length=64, null=False, unique=True)
    password = models.CharField(max_length=255, null=False, unique=False)


class Tip(models.Model):
    contenu = models.TextField()
    auteur = models.CharField(max_length = 150)
    date = models.DateTimeField(auto_now_add=True)
    upvote = models.IntegerField(default = 0)
    downvote = models.IntegerField(default = 0)
    myUserDown = models.ManyToManyField(MyUser, related_name='down')
    myUserUp = models.ManyToManyField(MyUser, related_name='up')

    class Meta:
        ordering = ['date']

    def toUpVote(self, myUserLogged):
        for myUser in self.myUserUp.all():
            if myUserLogged == myUser.username:
                self.myUserUp.remove(myUser)
                self.upvote -= 1
                self.save()
                return
        userLogged = MyUser.objects.get(username=myUserLogged)
        self.myUserUp.add(userLogged)
        self.upvote += 1
        if userLogged in self.myUserDown.all():
            self.myUserDown.remove(userLogged)
            self.downvote -= 1
        self.save()

    def toDownVote(self, myUserLogged):
        for myUser in self.myUserDown.all():
            if myUserLogged == myUser.username:
                self.myUserDown.remove(myUser)
                self.downvote -= 1
                self.save()
                return
        userLogged = MyUser.objects.get(username=myUserLogged)
        self.myUserDown.add(userLogged)
        self.downvote += 1
        if userLogged in self.myUserUp.all():
            self.myUserUp.remove(userLogged)
            self.upvote -= 1
        self.save()
