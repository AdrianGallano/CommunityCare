# Generated by Django 4.2.11 on 2024-04-13 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_alter_member_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='contact_no',
            field=models.CharField(max_length=20),
        ),
    ]
