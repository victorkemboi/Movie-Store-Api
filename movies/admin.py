from django.contrib import admin
from movies.models import *
# Register your models here.

class CastInline(admin.TabularInline):
    model = Movie.actors.through
    extra = 1

class GenreInline(admin.TabularInline):
    model = Movie.genres.through
    extra = 1

class ActorAdmin(admin.ModelAdmin):
    list_display = ('id','name')
    inlines = [
        CastInline,
    ]
   

admin.site.register(Actor,ActorAdmin)


class GenreAdmin(admin.ModelAdmin):
    list_display = ('id','genre')
    inlines = [
        GenreInline,
    ]
   

admin.site.register(Genre,GenreAdmin)


class MovieAdmin(admin.ModelAdmin):
    list_display = ('id','title','year')
    inlines = [
        CastInline,GenreInline,
    ]
admin.site.register(Movie,MovieAdmin)



admin.site.site_header = 'Movies Admin Panel '