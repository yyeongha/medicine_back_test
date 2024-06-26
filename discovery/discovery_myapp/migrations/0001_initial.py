# Generated by Django 5.0.6 on 2024-06-20 06:27

import django.contrib.auth.validators
import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
    ]

    operations = [
        migrations.CreateModel(
            name="Drug",
            fields=[
                (
                    "drug_no",
                    models.CharField(max_length=20, primary_key=True, serialize=False),
                ),
                ("drug_name", models.CharField(max_length=200)),
                ("drug_name_en", models.CharField(max_length=200)),
                ("drug_material", models.CharField(max_length=50)),
                ("drug_company", models.CharField(max_length=200)),
                ("drug_shape", models.CharField(max_length=20)),
                ("drug_color", models.CharField(max_length=100)),
                (
                    "drug_print_front",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                (
                    "drug_print_back",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                (
                    "drug_line_front",
                    models.CharField(blank=True, max_length=20, null=True),
                ),
                (
                    "drug_line_back",
                    models.CharField(blank=True, max_length=20, null=True),
                ),
                ("drug_price_amount", models.FloatField()),
                ("drug_price_unit", models.CharField(max_length=20)),
                ("drug_price", models.IntegerField()),
                ("drug_illness", models.CharField(max_length=20)),
                ("drug_img_path", models.CharField(max_length=400)),
            ],
            options={
                "db_table": "drug",
                "managed": True,
            },
        ),
        migrations.CreateModel(
            name="DrugDetail",
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
                ("customer_id", models.CharField(max_length=36)),
                ("drug_no", models.CharField(max_length=20)),
                ("drug_code", models.CharField(blank=True, max_length=20, null=True)),
                ("drug_name", models.CharField(max_length=200)),
            ],
            options={
                "verbose_name_plural": "Drug Details",
                "db_table": "drug_details",
                "managed": True,
            },
        ),
        
        # db에서 drug_images 테이블 사라짐..
        # migrations.CreateModel(
        #     name="DrugImage",
        #     fields=[
        #         ("drug_image_id", models.AutoField(primary_key=True, serialize=False)),
        #         ("drug_img_path", models.CharField(max_length=200)),
        #         (
        #             "drug_no",
        #             models.ForeignKey(
        #                 db_column="drug_no",
        #                 on_delete=django.db.models.deletion.CASCADE,
        #                 to="discovery_myapp.drug",
        #             ),
        #         ),
        #     ],
        #     options={
        #         "verbose_name_plural": "Drug Images",
        #         "db_table": "drug_images",
        #         "managed": True,
        #     },
        # ),
        migrations.CreateModel(
            name="Search",
            fields=[
                ("search_id", models.AutoField(primary_key=True, serialize=False)),
                ("customer_id", models.CharField(max_length=36)),
                ("drug_code", models.CharField(max_length=20)),
                ("search_ip", models.CharField(max_length=20)),
                ("search_date", models.CharField(max_length=100)),
                ("drug_name", models.CharField(max_length=200)),
                ("search_response", models.CharField(max_length=100)),
                (
                    "drug_no",
                    models.ForeignKey(
                        db_column="drug_no",
                        on_delete=django.db.models.deletion.CASCADE,
                        to="discovery_myapp.drug",
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "Search",
                "db_table": "search",
                "managed": True,
            },
        ),
        migrations.CreateModel(
            name="User",
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
                ("password", models.CharField(max_length=128, verbose_name="password")),
                (
                    "last_login",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="last login"
                    ),
                ),
                (
                    "is_superuser",
                    models.BooleanField(
                        default=False,
                        help_text="Designates that this user has all permissions without explicitly assigning them.",
                        verbose_name="superuser status",
                    ),
                ),
                (
                    "username",
                    models.CharField(
                        error_messages={
                            "unique": "A user with that username already exists."
                        },
                        help_text="Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.",
                        max_length=150,
                        unique=True,
                        validators=[
                            django.contrib.auth.validators.UnicodeUsernameValidator()
                        ],
                        verbose_name="username",
                    ),
                ),
                (
                    "first_name",
                    models.CharField(
                        blank=True, max_length=150, verbose_name="first name"
                    ),
                ),
                (
                    "last_name",
                    models.CharField(
                        blank=True, max_length=150, verbose_name="last name"
                    ),
                ),
                (
                    "email",
                    models.EmailField(
                        blank=True, max_length=254, verbose_name="email address"
                    ),
                ),
                (
                    "is_staff",
                    models.BooleanField(
                        default=False,
                        help_text="Designates whether the user can log into this admin site.",
                        verbose_name="staff status",
                    ),
                ),
                (
                    "is_active",
                    models.BooleanField(
                        default=True,
                        help_text="Designates whether this user should be treated as active. Unselect this instead of deleting accounts.",
                        verbose_name="active",
                    ),
                ),
                (
                    "date_joined",
                    models.DateTimeField(
                        default=django.utils.timezone.now, verbose_name="date joined"
                    ),
                ),
                (
                    "groups",
                    models.ManyToManyField(
                        blank=True, related_name="custom_user_set", to="auth.group"
                    ),
                ),
                (
                    "user_permissions",
                    models.ManyToManyField(
                        blank=True, related_name="custom_user_set", to="auth.permission"
                    ),
                ),
            ],
            options={
                "verbose_name": "user",
                "verbose_name_plural": "users",
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Customer",
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
                ("sex", models.CharField(max_length=20)),
                ("age", models.IntegerField()),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="customer_profile",
                        to="discovery_myapp.user",
                    ),
                ),
            ],
        ),
    ]
