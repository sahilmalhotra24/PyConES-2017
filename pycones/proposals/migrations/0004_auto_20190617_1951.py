# Generated by Django 2.2.2 on 2019-06-17 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("proposals", "0003_proposal_is_beginners_friendly")]

    operations = [
        migrations.AlterField(
            model_name="proposal",
            name="_abstract_en_rendered",
            field=models.TextField(default="", editable=False, null=True),
        ),
        migrations.AlterField(
            model_name="proposal",
            name="_abstract_es_rendered",
            field=models.TextField(default="", editable=False, null=True),
        ),
        migrations.AlterField(
            model_name="proposal",
            name="_abstract_rendered",
            field=models.TextField(default="", editable=False),
        ),
        migrations.AlterField(
            model_name="proposal",
            name="_additional_notes_en_rendered",
            field=models.TextField(default="", editable=False, null=True),
        ),
        migrations.AlterField(
            model_name="proposal",
            name="_additional_notes_es_rendered",
            field=models.TextField(default="", editable=False, null=True),
        ),
        migrations.AlterField(
            model_name="proposal",
            name="_additional_notes_rendered",
            field=models.TextField(default="", editable=False),
        ),
    ]
