# Generated by Django 4.1.3 on 2023-11-30 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_rename_icon_work_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='work',
            name='tech_stack',
            field=models.CharField(default='HTML, CSS', max_length=30),
        ),
    ]