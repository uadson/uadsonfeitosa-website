# Generated by Django 4.0 on 2022-02-10 23:12

from django.db import migrations, models
import stdimage.models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=stdimage.models.StdImageField(default='', upload_to='images', verbose_name='Imagem'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='post',
            name='section',
            field=models.CharField(choices=[('tutoriais', 'Tutoriais'), ('python', 'Python'), ('django', 'Django')], max_length=9, verbose_name='Seção'),
        ),
    ]
