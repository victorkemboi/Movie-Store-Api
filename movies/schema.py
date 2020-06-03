import graphene
from graphene_django.types import DjangoObjectType, ObjectType
from movies.models  import Actor, Movie, Genre

# Create a GraphQL type for the actor model
class ActorType(DjangoObjectType):
    class Meta:
        model = Actor

# Create a GraphQL type for the movie model
class MovieType(DjangoObjectType):
    class Meta:
        model = Movie

class GenreType(DjangoObjectType):
    class Meta:
        model = Genre


# Create a Query type
class Query(ObjectType):
    actor = graphene.Field(ActorType, id=graphene.Int())
    movie = graphene.Field(MovieType, id=graphene.Int())
    actors = graphene.List(ActorType)
    movies= graphene.List(MovieType)

    def resolve_actor(self, info, **kwargs):
        id = kwargs.get('id')

        if id is not None:
            return Actor.objects.get(pk=id)

        return None

    def resolve_movie(self, info, **kwargs):
        id = kwargs.get('id')

        if id is not None:
            return Movie.objects.get(pk=id)

        return None

    def resolve_actors(self, info, **kwargs):
        return Actor.objects.all()

    def resolve_movies(self, info, **kwargs):
        return Movie.objects.all()


# Create Input Object Types
class ActorInput(graphene.InputObjectType):
    id = graphene.ID()
    name = graphene.String()

class GenreInput(graphene.InputObjectType):
    id = graphene.ID()
    genre = graphene.String()

class MovieInput(graphene.InputObjectType):
    id = graphene.ID()
    title = graphene.String()
    cast = graphene.List(ActorInput)
    genres = graphene.List(ActorInput)
    year = graphene.Int()

class BulkMovieInput(graphene.InputObjectType):
    bulkInput = graphene.List(MovieInput)


# Create mutations for bulk input of movies
class CreateBulkMovies(graphene.Mutation):
    class Arguments:
        input = BulkMovieInput(required=True)

    ok = graphene.Boolean()
    movies = graphene.List(MovieType)

    @staticmethod
    def mutate(root,infor,input=None):
        ok = True
        moviesSaved = []
        for movie in input.bulkInput:
            cast = []
            for actor in movie.cast:
                storedActor = Actor.objects.get(name=actor.name)
                if storedActor is None:
                    #create a new actor
                    actor_instance = Actor(name=actor.name)
                    actor_instance.save()
                    cast.append(actor_instance)
                else:
                    cast.append.storedActor

            genres = []
            for genre in movie.genres:
                storedGenre = Genre.objects.get(genre=genre.genre)
                if storedGenre is None:
                    #create a new actor
                    genre_instance = Genre(genre=genre.genre)
                    genre_instance.save()
                    genres.append(genre_instance)
                else:
                    genres.append.storedGenre
            
            movie_instance = Movie(
            title=movie.title,
            year=movie.year
            )
            movie_instance.save()
            movie_instance.cast.set(cast)
            movie_instance.genres.set(genres)

            moviesSaved.append(movie_instance) 

        return CreateBulkMovies(ok=True,movies = moviesSaved )


# Create mutations for movies
class CreateMovie(graphene.Mutation):
    class Arguments:
        input = MovieInput(required=True)

    ok = graphene.Boolean()
    movie = graphene.Field(MovieType)

    @staticmethod
    def mutate(root, info, input=None):
        ok = True
        actors = []
        for actor_input in input.actors:
          actor = Actor.objects.get(pk=actor_input.id)
          if actor is None:
            return CreateMovie(ok=False, movie=None)
          actors.append(actor)
        movie_instance = Movie(
          title=input.title,
          year=input.year
          )
        movie_instance.save()
        movie_instance.actors.set(actors)
        return CreateMovie(ok=ok, movie=movie_instance)


class UpdateMovie(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)
        input = MovieInput(required=True)

    ok = graphene.Boolean()
    movie = graphene.Field(MovieType)

    @staticmethod
    def mutate(root, info, id, input=None):
        ok = False
        movie_instance = Movie.objects.get(pk=id)
        if movie_instance:
            ok = True
            actors = []
            for actor_input in input.actors:
              actor = Actor.objects.get(pk=actor_input.id)
              if actor is None:
                return UpdateMovie(ok=False, movie=None)
              actors.append(actor)
            movie_instance.title=input.title
            movie_instance.year=input.year
            movie_instance.save()
            movie_instance.actors.set(actors)
            return UpdateMovie(ok=ok, movie=movie_instance)
        return UpdateMovie(ok=ok, movie=None)



class CreateActor(graphene.Mutation):
    class Arguments:
        input = ActorInput(required=True)

    ok = graphene.Boolean()
    actor = graphene.Field(ActorType)

    @staticmethod
    def mutate(root, info, input=None):
        ok = True
        actor_instance = Actor(name=input.name)
        actor_instance.save()
        return CreateActor(ok=ok, actor=actor_instance)

class UpdateActor(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)
        input = ActorInput(required=True)

    ok = graphene.Boolean()
    actor = graphene.Field(ActorType)

    @staticmethod
    def mutate(root, info, id, input=None):
        ok = False
        actor_instance = Actor.objects.get(pk=id)
        if actor_instance:
            ok = True
            actor_instance.name = input.name
            actor_instance.save()
            return UpdateActor(ok=ok, actor=actor_instance)
        return UpdateActor(ok=ok, actor=None)


class Mutation(graphene.ObjectType):
    create_actor = CreateActor.Field()
    update_actor = UpdateActor.Field()
    create_movie = CreateMovie.Field()
    update_movie = UpdateMovie.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)