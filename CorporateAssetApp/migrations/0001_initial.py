# Generated by Django 4.2.5 on 2023-09-11 17:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Assets",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=350)),
                ("details", models.TextField(blank=True, null=True)),
            ],
            options={
                "verbose_name_plural": "Assets",
            },
        ),
        migrations.CreateModel(
            name="Company",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("company_title", models.CharField(max_length=300)),
                ("address", models.CharField(blank=True, max_length=550, null=True)),
                ("phone_no", models.IntegerField(blank=True, null=True)),
            ],
            options={
                "verbose_name_plural": "Companies",
            },
        ),
        migrations.CreateModel(
            name="Role",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="Employees",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("employee_name", models.CharField(max_length=400)),
                (
                    "company_employee",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="CorporateAssetApp.company",
                    ),
                ),
                (
                    "roles",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="Employee_Role",
                        to="CorporateAssetApp.role",
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "Employees",
            },
        ),
        migrations.CreateModel(
            name="AssetTrack",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=100)),
                (
                    "condition_at_checkout",
                    models.CharField(blank=True, max_length=200, null=True),
                ),
                (
                    "condition_at_return",
                    models.CharField(blank=True, max_length=200, null=True),
                ),
                ("checkout_at", models.DateField()),
                ("returned_at", models.DateField()),
                ("is_returned", models.BooleanField(default=False)),
                ("asset", models.ManyToManyField(to="CorporateAssetApp.assets")),
                (
                    "employee",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="Assign_Assets",
                        to="CorporateAssetApp.employees",
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "Assets Track Record",
            },
        ),
        migrations.AddField(
            model_name="assets",
            name="company_asset",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="Company_Asset",
                to="CorporateAssetApp.company",
            ),
        ),
    ]
