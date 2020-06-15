import graphene
from movies.query import Query
from movies.mutation import Mutation






schema = graphene.Schema(query=Query, mutation=Mutation)