from django.contrib.auth import get_user_model
import graphene
import graphql_social_auth
from graphene_django import DjangoObjectType
import board.schema


class UserType(DjangoObjectType):
    class Meta:
        model = get_user_model()


class Mutation(board.schema.Mutation, graphene.ObjectType):
    social_auth = graphql_social_auth.SocialAuthJWT.Field()
    pass


class Query(board.schema.Query, graphene.ObjectType):
    users = graphene.List(UserType)

    def resolve_users(self, info, **kwargs):
        return get_user_model().objects.all()
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
