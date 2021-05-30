# Generated by Django 3.1.7 on 2021-05-24 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BlogAPP', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='Admin_Name',
        ),
        migrations.AlterField(
            model_name='category',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='user_information',
            name='User_Name',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
