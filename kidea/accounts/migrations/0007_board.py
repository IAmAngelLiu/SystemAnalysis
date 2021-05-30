# Generated by Django 3.2.3 on 2021-05-24 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_alter_product_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='Board',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('board_type', models.CharField(choices=[('back', 'back'), ('door', 'door'), ('others', 'others')], max_length=200, null=True)),
                ('price', models.FloatField(null=True)),
            ],
        ),
    ]