# Generated by Django 4.1 on 2022-12-09 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0003_user_role_delete_customtoken"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="role",
            field=models.CharField(
                choices=[
                    ("LOGISTICS", "Logistics"),
                    ("NSH", "Nsh"),
                    ("NLH", "Nlh"),
                    ("NTH", "Nth"),
                ],
                max_length=20,
            ),
        ),
    ]