# Generated by Django 4.0 on 2022-02-10 21:30

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Data de Criação:')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Última Atualização:')),
                ('title', models.CharField(max_length=250, verbose_name='Título')),
                ('slug', models.SlugField(blank=True, max_length=250, unique_for_date='publish')),
                ('body', models.TextField(verbose_name='Texto')),
                ('section', models.CharField(choices=[('home', 'Home'), ('python', 'Python'), ('django', 'Django')], max_length=6, verbose_name='Seção')),
                ('publish', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Publicação')),
                ('status', models.CharField(choices=[('draft', 'Draft'), ('published', 'Published')], default='draft', max_length=10, verbose_name='Status')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='blog_posts', to='core.user', verbose_name='Autor')),
            ],
            options={
                'ordering': ('-publish',),
            },
        ),
    ]
