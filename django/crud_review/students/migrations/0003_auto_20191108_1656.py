# Generated by Django 2.2.6 on 2019-11-08 07:56

from django.db import migrations, models
import django.db.models.deletion
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0002_auto_20191104_1548'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='image',
            field=imagekit.models.fields.ProcessedImageField(blank=True, upload_to='students/image'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='students.Student'),
        ),
    ]
