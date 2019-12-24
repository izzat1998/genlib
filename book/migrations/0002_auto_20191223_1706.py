# Generated by Django 2.2.6 on 2019-12-23 17:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='genre',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='books', to='book.Genre'),
        ),
        migrations.DeleteModel(
            name='GenreBookManyRelation',
        ),
    ]
