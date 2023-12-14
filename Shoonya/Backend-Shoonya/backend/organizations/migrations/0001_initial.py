# Generated by Django 3.2.14 on 2023-12-14 07:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=1024, verbose_name='organization_title')),
                ('email_domain_name', models.CharField(max_length=4096, null=True, verbose_name='organization_email_domain')),
                ('is_active', models.BooleanField(default=True, help_text='Designates weather an organization is active or not.', verbose_name='organization_is_active')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created_at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updated_at')),
                ('created_by', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='organization_creator', to=settings.AUTH_USER_MODEL, verbose_name='created_by')),
            ],
        ),
        migrations.CreateModel(
            name='Invite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('invite_code', models.CharField(max_length=256, null=True, unique=True, verbose_name='invite_code')),
                ('organization', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='invite_oganization', to='organizations.organization', verbose_name='organization')),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='invite_users', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]