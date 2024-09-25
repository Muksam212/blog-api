# Generated by Django 4.2.16 on 2024-09-24 14:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0005_alter_reaction_reaction'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reaction',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_reaction', to=settings.AUTH_USER_MODEL),
        ),
    ]
