# Generated by Django 3.2.3 on 2021-05-30 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='shoppingcart',
            name='price',
            field=models.FloatField(null=True),
        ),
    ]
