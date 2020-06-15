from django.contrib import admin
from movies.models import *
# Register your models here.

class CastInline(admin.TabularInline):
    model = Movie.cast.through
    extra = 1

class GenreInline(admin.TabularInline):
    model = Movie.genres.through
    extra = 1

class ActorAdmin(admin.ModelAdmin):
    list_display = ('actor_id','name')
    inlines = [
        CastInline,
    ]
   

admin.site.register(Actor,ActorAdmin)


class GenreAdmin(admin.ModelAdmin):
    list_display = ('genre_id','genre')
    inlines = [
        GenreInline,
    ]
   

admin.site.register(Genre,GenreAdmin)


class MovieAdmin(admin.ModelAdmin):
    list_display = ('movie_id','title','year')
    inlines = [
        CastInline,GenreInline,
    ]
admin.site.register(Movie,MovieAdmin)

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('customer_id','name','email','account_balance')
    
admin.site.register(Customer,CustomerAdmin)

admin.site.site_header = 'Movies Admin Panel '