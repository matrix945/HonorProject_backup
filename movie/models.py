from django.db import models


class Movie(models.Model):


    genreChoice = (
        ('Action', 'Action'),
        ('Adventure', 'Adventure'),
        ('Animation', 'Animation'),
        ('Children', 'Children'),
        ('Comedy', 'Comedy'),
        ('Crime', 'Crime'),
        ('Documentary', 'Documentary'),
        ('Drama', 'Drama'),
        ('Fantasy', 'Fantasy'),
        ('Film-Noir', 'Film-Noir'),
        ('Horror', 'Horror'),
        ('Musical', 'Musical'),
        ('Mystery', 'Mystery'),
        ('Romance', 'Romance'),
        ('Sci-Fi', 'Sci-Fi'),
        ('Thriller', 'Thriller'),
        ('War', 'War'),
        ('Western', 'Western'),
    )

    title = models.CharField(max_length=100, default='', blank=True)
    genres = models.CharField(max_length=100,default='')

    movieid = models.CharField(max_length=20, primary_key=True)
    # title = models.CharField(max_length=30)
    year = models.CharField(max_length=4)
    length = models.CharField(max_length=10)
    # genres = models.CharField(max_length=100)
    rate = models.IntegerField(default=0)
    poster = models.URLField(default='',blank=True)
    plot = models.CharField(max_length=500,blank=True)
    trailer = models.URLField(default='',blank=True)

    def __str__(self):
        return self.movieid + '|' + self.title

    @staticmethod
    def get_name():
        return 'movie'


# class Actor(models.Model):
#     actorid = models.CharField(max_length=20, primary_key=True)
#     name = models.CharField(max_length=30)
#     photo = models.URLField()
#
#     def __str__(self):
#         return self.actorid + '|' + self.name
#
#     @staticmethod
#     def get_name():
#         return 'actor'
#
#
# class Act(models.Model):
#     movieid = models.ForeignKey('Movie', default=1, on_delete=models.CASCADE)
#     actorid = models.ForeignKey('Actor', default=1, on_delete=models.CASCADE)
#
#     def __str__(self):
#         return self.actorid.actorid + '|' + self.movieid.movieid
#
#
# class Seen(models.Model):
#     username = models.CharField(max_length=150)
#     movieid = models.ForeignKey('Movie', default=1, on_delete=models.CASCADE)
#
#     def __str__(self):
#         return self.username + '|' + self.movieid.movieid
#
#
# class Expect(models.Model):
#     username = models.CharField(max_length=150)
#     movieid = models.ForeignKey('Movie', default=1, on_delete=models.CASCADE)
#
#     def __str__(self):
#         return self.username + '|' + self.movieid.movieid
#
#
# class Popularity(models.Model):
#     movieid = models.ForeignKey('Movie', default=' ', on_delete=models.CASCADE)
#     weight = models.IntegerField(default=0)
#
#     def __str__(self):
#         return self.movieid.movieid + '|' + str(self.weight)
#

class Rating(models.Model):
    username = models.CharField(max_length=150)
    movieid = models.ForeignKey('Movie', default=1, on_delete=models.CASCADE)
    rate = models.IntegerField(default=0,blank=True)
    timestamp = models.IntegerField(default=0,blank=True)