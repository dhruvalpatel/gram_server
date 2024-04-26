import graphene
from .gram_server.views.application import schema as application_schema
from .gram_server.views.user import schema as user_schema


class Mutation(application_schema.Mutation, user_schema.Mutation):
    pass


class Query(application_schema.Query, user_schema.Query):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
