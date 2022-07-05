import faker
from factory.django import DjangoModelFactory

from instagram.models import Content, Niche, PostImage, Rubric, Text


fake = faker.Faker(['ru-RU'])


class RubricFactory(DjangoModelFactory):
    class Meta:
        model = Rubric

    name = 'REVIEW_NEW_PRODUCTS'


class NicheFactory(DjangoModelFactory):
    class Meta:
        model = Niche

    name = 'BEAUTY'


class ContentFactory(DjangoModelFactory):
    class Meta:
        model = Content

    name = 'ENTERTAINING'


class TextFactory(DjangoModelFactory):
    class Meta:
        model = Text

    level = ''
    body = fake.text()

    @classmethod
    def create(cls, **kwargs):
        rubric = Rubric.objects.last()
        if not rubric:
            rubric = RubricFactory()
        niche = Niche.objects.last()
        if not niche:
            niche = NicheFactory()
        content = Content.objects.last()
        if not content:
            content = ContentFactory()
        kwargs['rubric'] = rubric
        kwargs['niche'] = niche
        kwargs['content'] = content
        return super(TextFactory, cls).create(**kwargs)


class PostImageFactory(DjangoModelFactory):
    class Meta:
        model = PostImage

    file = ''

    @classmethod
    def create(cls, **kwargs):
        rubric = Rubric.objects.last()
        if not rubric:
            rubric = RubricFactory()
        niche = Niche.objects.last()
        if not niche:
            niche = NicheFactory()
        content = Content.objects.last()
        if not content:
            content = ContentFactory()
        kwargs['rubric'] = rubric
        kwargs['niche'] = niche
        kwargs['content'] = content
        return super(PostImageFactory, cls).create(**kwargs)
