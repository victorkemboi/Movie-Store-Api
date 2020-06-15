import graphene
import movies.schema
import market.schema
import graphql_jwt

class Query(movies.schema.Query,market.schema.Query ,graphene.ObjectType):
    # This class will inherit from multiple Queries
    # as we begin to add more apps to our project
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()

class Mutation(movies.schema.Mutation,market.schema.Mutation , graphene.ObjectType):
    # This class will inherit from multiple Queries
    # as we begin to add more apps to our project
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)