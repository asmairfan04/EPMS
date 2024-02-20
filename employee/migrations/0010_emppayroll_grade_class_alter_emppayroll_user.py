# Generated by Django 4.0 on 2022-03-13 20:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('employee', '0009_grade'),
    ]

    operations = [
        migrations.AddField(
            model_name='emppayroll',
            name='grade_class',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='grade_class', to='employee.grade'),
        ),
        migrations.AlterField(
            model_name='emppayroll',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user', to='auth.user'),
        ),
    ]