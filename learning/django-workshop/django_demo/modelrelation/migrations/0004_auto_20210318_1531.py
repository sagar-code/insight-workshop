# Generated by Django 3.1.6 on 2021-03-18 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modelrelation', '0003_auto_20210318_1526'),
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('c_name', models.CharField(max_length=30)),
            ],
        ),
        migrations.AddField(
            model_name='userdetail',
            name='country',
            field=models.ManyToManyField(to='modelrelation.Country'),
        ),
    ]
