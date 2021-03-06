# Generated by Django 3.2.8 on 2021-10-28 15:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tadoku', '0002_auto_20211028_2356'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('words', models.IntegerField()),
                ('series', models.CharField(blank=True, max_length=255, null=True)),
                ('yl', models.FloatField(blank=True, null=True)),
                ('isbn', models.CharField(max_length=13, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='ReadBook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField(blank=True, null=True)),
                ('rate', models.PositiveSmallIntegerField(blank=True, choices=[(1, '★'), (2, '★★'), (3, '★★★'), (4, '★★★★'), (5, '★★★★★')], null=True)),
                ('read_at', models.DateField(auto_now_add=True)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tadoku.book')),
                ('reader', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='readbooks',
            name='book',
        ),
        migrations.RemoveField(
            model_name='readbooks',
            name='reader',
        ),
        migrations.DeleteModel(
            name='Books',
        ),
        migrations.DeleteModel(
            name='ReadBooks',
        ),
    ]
