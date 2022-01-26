from django.db import models
from django.utils import timezone

from core.models import User

from django.urls import reverse


class Base(models.Model):
    created = models.DateTimeField('Data de Criação:', auto_now_add=True)
    updated = models.DateTimeField('Última Atualização:', auto_now=True)

    class Meta:
        abstract = True


class Post(Base):
    SECTION_CHOICES = (
        ('home', 'Home'),
        ('python', 'Python'),
        ('django', 'Django')
    )

    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    title = models.CharField('Título', max_length=250)
    slug = models.SlugField(
        max_length=250,
        unique_for_date='publish',
        blank=True)
    author = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        related_name='blog_posts',
        verbose_name='Autor')
    body = models.TextField('Texto')
    section = models.CharField('Seção', max_length=6, choices=SECTION_CHOICES)
    publish = models.DateTimeField('Publicação', default=timezone.now)
    status = models.CharField(
        'Status',
        max_length=10,
        choices=STATUS_CHOICES,
        default='draft')

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse(
        'website:post_detail',
        args=[self.publish.year,
              self.publish.month,
              self.publish.day,
              self.slug])
