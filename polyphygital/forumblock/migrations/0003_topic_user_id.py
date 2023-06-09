# Generated by Django 4.2.1 on 2023-06-15 14:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('forumblock', '0002_remove_topic_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='topic',
            name='user_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='ID создателя обсуждения'),
            preserve_default=False,
        ),
    ]
