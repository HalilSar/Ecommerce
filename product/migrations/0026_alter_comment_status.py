# Generated by Django 3.2 on 2021-04-29 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0025_alter_comment_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='status',
            field=models.CharField(choices=[('New', 'Yeni'), ('True', 'Evet'), ('False', 'Hayır')], default='New', max_length=10),
        ),
    ]
