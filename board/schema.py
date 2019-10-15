import graphene

from graphene_django.types import DjangoObjectType
from .models import BoardModel, ArticleModel, CommentModel, ThumbModel


class BoardModelType(DjangoObjectType):
    class Meta:
        model = BoardModel


class ArticleModelType(DjangoObjectType):
    class Meta:
        model = ArticleModel


class CommentModelType(DjangoObjectType):
    class Meta:
        model = CommentModel


class ThumbModelType(DjangoObjectType):
    class Meta:
        model = ThumbModel


class Query(object):
    all_board = graphene.List(BoardModelType)
    all_article = graphene.List(ArticleModelType)
    all_comment = graphene.List(CommentModelType)
    all_thumb = graphene.List(ThumbModelType)

    article = graphene.Field(ArticleModelType, id=graphene.Int())
    comment = graphene.Field(CommentModelType, id=graphene.Int())

    commentByArticle = graphene.Field(
        CommentModelType, article=graphene.String())

    def resolve_all_board(self, info, **kwargs):
        return BoardModel.objects.all()

    def resolve_all_article(self, info, **kwargs):
        return ArticleModel.objects.select_related('board').all()

    def resolve_all_comment(self, info, **kwargs):
        return CommentModel.objects.select_related('article').all()

    def resolve_all_thumb(self, info, **kwargs):
        return ThumbModel.objects.select_related('article').all()

    def resolve_article(self, info, **kwargs):
        id = kwargs.get('id')

        if id is not None:
            return ArticleModel.objects.get(pk=id)

        return None

    def resolve_comment(self, info, **kwargs):
        id = kwargs.get('id')

        if id is not None:
            return CommentModel.objects.get(pk=id)

        return None

    def resolve_comment_by_article(self, info, **kwargs):
        article = kwargs.get('article')

        if id is not None:
            return CommentModel.objects.get(article=article)

        return None


class ArticleMutation(graphene.Mutation):
    class Arguments:
        subject = graphene.String(required=True)
        contents = graphene.String(required=True)

    article = graphene.Field(ArticleModelType)

    def mutate(self, info, subject, contents):


class Mutation(object):
    all_board = graphene.List(BoardModelType)
