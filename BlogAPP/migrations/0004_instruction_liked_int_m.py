# Generated by Django 3.1.7 on 2021-05-25 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BlogAPP', '0003_auto_20210524_2338'),
    ]

    operations = [
        migrations.AddField(
            model_name='instruction',
            name='Liked_int_M',
            field=models.CharField(default='0', max_length=100),
        ),
    ]
