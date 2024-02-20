# Generated by Django 4.0 on 2022-02-16 14:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('employee', '0002_rename_department_empdetail_department_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmpExp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company1Name', models.CharField(max_length=100, null=True)),
                ('company1Desig', models.CharField(max_length=100, null=True)),
                ('company1Salary', models.CharField(max_length=100, null=True)),
                ('company1Duration', models.CharField(max_length=100, null=True)),
                ('company2Name', models.CharField(max_length=100, null=True)),
                ('company2Desig', models.CharField(max_length=100, null=True)),
                ('company2Salary', models.CharField(max_length=100, null=True)),
                ('company2Duration', models.CharField(max_length=100, null=True)),
                ('company3Name', models.CharField(max_length=100, null=True)),
                ('company3Desig', models.CharField(max_length=100, null=True)),
                ('company3Salary', models.CharField(max_length=100, null=True)),
                ('company3Duration', models.CharField(max_length=100, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth.user')),
            ],
        ),
        migrations.CreateModel(
            name='EmpEdu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pgCourse', models.CharField(max_length=100, null=True)),
                ('pgClg', models.CharField(max_length=200, null=True)),
                ('pgYOP', models.CharField(max_length=10, null=True)),
                ('pgPercentage', models.CharField(max_length=10, null=True)),
                ('gradCourse', models.CharField(max_length=100, null=True)),
                ('gradClg', models.CharField(max_length=200, null=True)),
                ('gradYOP', models.CharField(max_length=10, null=True)),
                ('gradPercentage', models.CharField(max_length=10, null=True)),
                ('sscSchool', models.CharField(max_length=200, null=True)),
                ('sscYOP', models.CharField(max_length=10, null=True)),
                ('sscPercentage', models.CharField(max_length=10, null=True)),
                ('hscSchool', models.CharField(max_length=200, null=True)),
                ('hscYOP', models.CharField(max_length=10, null=True)),
                ('hscPercentage', models.CharField(max_length=10, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth.user')),
            ],
        ),
    ]
