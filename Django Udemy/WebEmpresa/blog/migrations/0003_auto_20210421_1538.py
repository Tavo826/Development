# Generated by Django 3.1.7 on 2021-04-21 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20210420_2334'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='categories',
            field=models.ManyToManyField(related_name='get_post', to='blog.Category', verbose_name='Categorías'),
        ),
    ]
