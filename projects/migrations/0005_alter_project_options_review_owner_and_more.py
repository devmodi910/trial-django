# Generated by Django 5.1.4 on 2025-01-17 08:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0004_project_owner'),
        ('users', '0004_profile_social_linkedin'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='project',
            options={'ordering': ['created']},
        ),
        migrations.AddField(
            model_name='review',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='users.profile'),
        ),
        migrations.AlterUniqueTogether(
            name='review',
            unique_together={('owner', 'project')},
        ),
    ]
