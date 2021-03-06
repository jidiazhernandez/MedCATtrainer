# Generated by Django 2.2.3 on 2019-10-02 23:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0015_auto_20191002_1615'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projectannotateentities',
            name='medcat_models',
        ),
        migrations.AddField(
            model_name='projectannotateentities',
            name='concept_db',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.ConceptDB'),
        ),
        migrations.AddField(
            model_name='projectannotateentities',
            name='vocab',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.Vocabulary'),
        ),
        migrations.AlterField(
            model_name='projectannotateentities',
            name='cdb_search_filter',
            field=models.ManyToManyField(blank=True, default=None, related_name='concept_source', to='api.ConceptDB'),
        ),
    ]
