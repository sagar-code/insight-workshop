# Generated by Django 3.1.6 on 2021-03-18 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modelrelation', '0004_auto_20210318_1531'),
    ]

    operations = [
        migrations.CreateModel(
            name='Information',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('info', models.CharField(max_length=30)),
                ('bio', models.TextField()),
            ],
        ),
    ]
