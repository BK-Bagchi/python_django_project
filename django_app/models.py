from django.db import models


# It somewhat looks like 'CREATE TABLE Musician (first_name varchar(20), last_name varchar(20), instrument varchar(20))'
class Musician(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20, null=True, blank=True)
    instrument = models.CharField(max_length=20)

    def __str__(self):
        return self.first_name+" "+self.last_name


# It somewhat looks like 'CREATE TABLE Album (artist varchar(20) foreign key references Musician(first_name), name varchar(20), release_date date)'
class Album(models.Model):
    artist = models.ForeignKey(Musician, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    release_date = models.DateTimeField(auto_now_add=True)

    rating = (
        (1, "Worst"),
        (2, "Bad"),
        (3, "Neutral"),
        (4, "Good"),
        (5, "Great")
    )
    num_stars = models.IntegerField(choices=rating)

    def __str__(self):
        return self.name
