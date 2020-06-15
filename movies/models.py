from django.db import models
from django.contrib.auth.models import User
import uuid




# Create your models here.
class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True,null=True,blank=True)
    updated_at = models.DateTimeField(auto_now=True,null=True,blank=True)

    class Meta:
        abstract = True



class Customer(BaseModel):
    customer_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=150)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()
    user = models.ForeignKey(User,  on_delete=models.CASCADE,)
    account_balance = models.FloatField(blank=True, default=10000)

    def to_json(self):
        return{
            'customer_id':self.agent_id,
            'name':self.name,
            'phone_number':self.phone_number,
            'email':self.email,
            'user':self.user.id,
            'account_balance':self.account_balance
        }

    def __str__(self):
        return self.name

    class Meta:
        db_table = "customer"

class Actor(BaseModel):
    actor_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)

class Genre(BaseModel):
    genre_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
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

 

