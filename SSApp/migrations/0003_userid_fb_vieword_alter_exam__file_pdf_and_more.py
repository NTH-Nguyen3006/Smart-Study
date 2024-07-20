# Generated by Django 5.0.3 on 2024-05-11 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SSApp', '0002_exam'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserID_FB',
            fields=[
                ('_id', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('date_start', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='VieWord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.CharField(max_length=40)),
            ],
        ),
        migrations.AlterField(
            model_name='exam',
            name='_File_PDF',
            field=models.FileField(blank=True, upload_to='files/pdf/'),
        ),
        migrations.AlterField(
            model_name='exam',
            name='_File_word',
            field=models.FileField(blank=True, upload_to='files/words/'),
        ),
        migrations.AlterField(
            model_name='exam',
            name='image',
            field=models.ImageField(blank=True, upload_to='images/'),
        ),
    ]