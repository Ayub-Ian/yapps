# Generated by Django 4.2.16 on 2024-10-03 16:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0002_alter_menuitem_external_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='image_url',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='menuitem',
            name='image_url',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='menuitem',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='menu.category'),
        ),
    ]