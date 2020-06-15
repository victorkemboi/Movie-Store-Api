from django.db import models
import uuid




# Create your models here.
class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True,null=True,blank=True)
    updated_at = models.DateTimeField(auto_now=True,null=True,blank=True)

    class Meta:
        abstract = True

class Actor(BaseModel):
    actor_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)

class Genre(BaseModel):
    genre_id = models.UUIDField( primary_key=True, default=uuid.uuid4, editable=False)
    genre = models.CharField(max_length=250)

    def __str__(self):
        return self.genre

    class Meta:
        ordering = ('genre',)

class Movie(BaseModel):
    movie_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=250)
    cast = models.ManyToManyField(Actor)
    year = models.IntegerField()
    genres = models.ManyToManyField(Genre)
    def __str__(self):
        return self.title

    class Meta:
        ordering = ('title',)

#class Cast (models.Model):
   # actor = models.ForeignKey(Actor, on_delete=models.CASCADE)
  #  movie = models.ForeignKey(Movie, on_delete=models.CASCADE)

 

