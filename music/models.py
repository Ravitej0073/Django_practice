from django.db import models

# This denotes a table Album with columns artist,album_title etc

class Album(models.Model):

    artist = models.CharField(max_length=250)
    album_title = models.CharField(max_length=250)
    genre = models.CharField(max_length=100)
    album_logo = models.CharField(max_length=1000)

    def __str__(self):
        return "{}-{}".format(self.album_title,self.artist)


class Song(models.Model):

    album = models.ForeignKey(Album,on_delete=models.CASCADE)
    file_type = models.CharField(max_length=10)
    song_title = models.CharField(max_length=250)
    is_favourite=models.BooleanField(default=False)

    def __str__(self):
        return self.song_title


# After any changes in models file. 2 steps will replicate changes
# 1. Make migrate app - python manage.py makemigrations music
# 2. Actual migrate - python manage.py migrate.



