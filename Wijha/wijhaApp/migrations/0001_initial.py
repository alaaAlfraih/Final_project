# Generated by Django 4.1.3 on 2022-11-13 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='New_Place',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place_name', models.CharField(max_length=1024)),
                ('city', models.CharField(max_length=256)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('content', models.TextField()),
            ],
        ),
    ]