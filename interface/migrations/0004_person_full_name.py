# Generated by Django 3.0.5 on 2021-05-13 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('interface', '0003_person'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='full_name',
            field=models.CharField(default='ok', max_length=30),
            preserve_default=False,
        ),
    ]
