# Generated by Django 3.2.19 on 2023-05-19 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('elibrary_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Catalogue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('ISBN', models.CharField(max_length=13)),
                ('author', models.CharField(max_length=255)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('availability', models.CharField(choices=[('true', 'True'), ('false', 'False')], default='false', max_length=5)),
            ],
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
    ]