# Generated by Django 3.2.13 on 2022-09-13 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("edc_mnsi", "0004_auto_20220704_1841"),
    ]

    operations = [
        migrations.AddField(
            model_name="abnormalfootappearanceobservations",
            name="plural_name",
            field=models.CharField(max_length=250, null=True, verbose_name="Plural name"),
        ),
    ]
