# Generated by Django 2.2.5 on 2019-09-29 18:03

from django.db import migrations, models
import django_better_admin_arrayfield.models.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ArrayModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sample_array', django_better_admin_arrayfield.models.fields.ArrayField(base_field=models.CharField(max_length=20), size=None)),
            ],
        ),
    ]