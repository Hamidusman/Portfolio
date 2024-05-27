# Generated by Django 4.2.7 on 2024-05-27 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0016_alter_experience_tech1'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60)),
                ('tech', models.CharField(max_length=100)),
                ('github_link', models.URLField(max_length=150)),
                ('website_link', models.URLField(max_length=150)),
            ],
        ),
    ]
