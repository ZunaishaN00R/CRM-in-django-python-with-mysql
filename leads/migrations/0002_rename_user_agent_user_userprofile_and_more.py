# Generated by Django 4.2.5 on 2023-10-12 12:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='agent',
            old_name='User',
            new_name='user',
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='agent',
            name='organisation',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='leads.userprofile'),
            preserve_default=False,
        ),
    ]