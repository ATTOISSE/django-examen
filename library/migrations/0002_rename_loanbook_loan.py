# Generated by Django 5.1.1 on 2024-09-20 22:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='LoanBook',
            new_name='Loan',
        ),
    ]
