# Generated by Django 4.1.7 on 2023-03-24 19:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import simple_history.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(max_length=255, unique=True)),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='Email')),
                ('name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Name')),
                ('last_name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Last name')),
                ('image', models.ImageField(blank=True, max_length=255, null=True, upload_to='perfil/', verbose_name='Imagen')),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_verified', models.BooleanField(default=False)),
                ('auth_provider', models.CharField(default='email', max_length=255)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'Usuario',
                'verbose_name_plural': 'Usuarios',
            },
        ),
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('state', models.BooleanField(default=True, verbose_name='Satete')),
                ('created_date', models.DateField(auto_now_add=True, verbose_name='Creation date')),
                ('modified_date', models.DateField(auto_now=True, verbose_name='write date')),
                ('deleted_date', models.DateField(auto_now=True, verbose_name='Deleted date')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='Name')),
                ('symbol', models.CharField(max_length=3, unique=True, verbose_name='Symbol')),
                ('currency', models.CharField(max_length=3, unique=True, verbose_name='Currency')),
            ],
            options={
                'verbose_name': 'Currency',
                'verbose_name_plural': 'Currencies',
            },
        ),
        migrations.CreateModel(
            name='EcommerceBrand',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('state', models.BooleanField(default=True, verbose_name='Satete')),
                ('created_date', models.DateField(auto_now_add=True, verbose_name='Creation date')),
                ('modified_date', models.DateField(auto_now=True, verbose_name='write date')),
                ('deleted_date', models.DateField(auto_now=True, verbose_name='Deleted date')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='Name')),
                ('symbol', models.CharField(max_length=3, unique=True, verbose_name='Symbol')),
                ('currency', models.CharField(max_length=3, unique=True, verbose_name='Currency')),
            ],
            options={
                'verbose_name': 'Currency',
                'verbose_name_plural': 'Currencies',
            },
        ),
        migrations.CreateModel(
            name='EcommerceChanel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('state', models.BooleanField(default=True, verbose_name='Satete')),
                ('created_date', models.DateField(auto_now_add=True, verbose_name='Creation date')),
                ('modified_date', models.DateField(auto_now=True, verbose_name='write date')),
                ('deleted_date', models.DateField(auto_now=True, verbose_name='Deleted date')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='Name')),
                ('vtex_id', models.CharField(max_length=200, verbose_name='Vtes ID')),
            ],
            options={
                'verbose_name': 'Currency',
                'verbose_name_plural': 'Currencies',
            },
        ),
        migrations.CreateModel(
            name='EcommerceCountry',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('state', models.BooleanField(default=True, verbose_name='Satete')),
                ('created_date', models.DateField(auto_now_add=True, verbose_name='Creation date')),
                ('modified_date', models.DateField(auto_now=True, verbose_name='write date')),
                ('deleted_date', models.DateField(auto_now=True, verbose_name='Deleted date')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='Name')),
                ('code_country', models.CharField(max_length=4, unique=True, verbose_name='Code country')),
                ('phone_code', models.IntegerField(unique=True, verbose_name='Code phone')),
                ('currency', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.currency', verbose_name='Currency')),
            ],
            options={
                'verbose_name': 'Country',
                'verbose_name_plural': 'Countries',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='EcommerceHub',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('state', models.BooleanField(default=True, verbose_name='Satete')),
                ('created_date', models.DateField(auto_now_add=True, verbose_name='Creation date')),
                ('modified_date', models.DateField(auto_now=True, verbose_name='write date')),
                ('deleted_date', models.DateField(auto_now=True, verbose_name='Deleted date')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='Name')),
                ('vtex_id', models.CharField(max_length=200, verbose_name='Vtes ID')),
                ('title', models.CharField(max_length=200, verbose_name='Title site')),
                ('link', models.CharField(max_length=200, verbose_name='Link')),
                ('active', models.BooleanField(verbose_name='Active')),
                ('description', models.TextField(max_length=200, verbose_name='Description')),
            ],
            options={
                'verbose_name': 'Brand',
                'verbose_name_plural': 'Brands',
            },
        ),
        migrations.CreateModel(
            name='EcommerceMeasureUnit',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('state', models.BooleanField(default=True, verbose_name='Satete')),
                ('created_date', models.DateField(auto_now_add=True, verbose_name='Creation date')),
                ('modified_date', models.DateField(auto_now=True, verbose_name='write date')),
                ('deleted_date', models.DateField(auto_now=True, verbose_name='Deleted date')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='Description')),
            ],
            options={
                'verbose_name': 'MeasureUnit',
                'verbose_name_plural': 'MeasureUnits',
            },
        ),
        migrations.CreateModel(
            name='EcommercePaymentMethod',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('state', models.BooleanField(default=True, verbose_name='Satete')),
                ('created_date', models.DateField(auto_now_add=True, verbose_name='Creation date')),
                ('modified_date', models.DateField(auto_now=True, verbose_name='write date')),
                ('deleted_date', models.DateField(auto_now=True, verbose_name='Deleted date')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='Name')),
                ('vtex_id', models.CharField(max_length=200, verbose_name='Vtes ID')),
            ],
            options={
                'verbose_name': 'Payment Method',
                'verbose_name_plural': 'Payment Methods',
            },
        ),
        migrations.CreateModel(
            name='EcommerceWarehouse',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('state', models.BooleanField(default=True, verbose_name='Satete')),
                ('created_date', models.DateField(auto_now_add=True, verbose_name='Creation date')),
                ('modified_date', models.DateField(auto_now=True, verbose_name='write date')),
                ('deleted_date', models.DateField(auto_now=True, verbose_name='Deleted date')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='Name')),
                ('vtex_id', models.CharField(max_length=200, verbose_name='Vtes ID')),
            ],
            options={
                'verbose_name': 'Warehouse',
                'verbose_name_plural': 'Warehouses',
            },
        ),
        migrations.CreateModel(
            name='HistoricalUser',
            fields=[
                ('id', models.BigIntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(db_index=True, max_length=255)),
                ('email', models.EmailField(db_index=True, max_length=255, verbose_name='Email')),
                ('name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Name')),
                ('last_name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Last name')),
                ('image', models.TextField(blank=True, max_length=255, null=True, verbose_name='Imagen')),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_verified', models.BooleanField(default=False)),
                ('auth_provider', models.CharField(default='email', max_length=255)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField(db_index=True)),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical Usuario',
                'verbose_name_plural': 'historical Usuarios',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': ('history_date', 'history_id'),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='EcommerceState',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('state', models.BooleanField(default=True, verbose_name='Satete')),
                ('created_date', models.DateField(auto_now_add=True, verbose_name='Creation date')),
                ('modified_date', models.DateField(auto_now=True, verbose_name='write date')),
                ('deleted_date', models.DateField(auto_now=True, verbose_name='Deleted date')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='Name')),
                ('code_state', models.CharField(max_length=4, unique=True, verbose_name='Code country')),
                ('vtex_id', models.CharField(max_length=200, verbose_name='Vtes ID')),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.ecommercecountry', verbose_name='Country')),
            ],
            options={
                'verbose_name': 'State',
                'verbose_name_plural': 'States',
            },
        ),
        migrations.CreateModel(
            name='EcommerceContact',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created_date', models.DateField(auto_now_add=True, verbose_name='Creation date')),
                ('modified_date', models.DateField(auto_now=True, verbose_name='write date')),
                ('deleted_date', models.DateField(auto_now=True, verbose_name='Deleted date')),
                ('names', models.CharField(max_length=150, verbose_name='Name')),
                ('last_name', models.CharField(max_length=150, verbose_name='Last name')),
                ('dni', models.CharField(max_length=10, unique=True, verbose_name='DNI')),
                ('address', models.CharField(blank=True, max_length=150, null=True, verbose_name='Address')),
                ('street_door_number', models.CharField(blank=True, max_length=150, null=True, verbose_name='Street door number')),
                ('floor', models.CharField(blank=True, max_length=150, null=True, verbose_name='Floor')),
                ('apartment', models.CharField(blank=True, max_length=150, null=True, verbose_name='Apartment')),
                ('location', models.CharField(blank=True, max_length=150, null=True, verbose_name='Location')),
                ('between_street', models.CharField(blank=True, max_length=150, null=True, verbose_name='Between Street')),
                ('zip', models.CharField(blank=True, max_length=10, null=True, verbose_name='Zip')),
                ('sex', models.CharField(choices=[('male', 'Male'), ('female', 'Female')], default='male', max_length=10, verbose_name='Sex')),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='Email address')),
                ('image', models.ImageField(blank=True, max_length=255, null=True, upload_to='perfil/', verbose_name='Imagen')),
                ('phone', models.CharField(max_length=11, verbose_name='Phone')),
                ('contact_type', models.CharField(choices=[('provider', 'Provider'), ('client', 'Client')], max_length=10, verbose_name='Contact type')),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.ecommercecountry', verbose_name='Country')),
                ('state', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='base.ecommercestate', verbose_name='State')),
            ],
            options={
                'verbose_name': 'Contact',
                'verbose_name_plural': 'Contacts',
                'ordering': ['names'],
            },
        ),
        migrations.CreateModel(
            name='EcommerceCategory',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('state', models.BooleanField(default=True, verbose_name='Satete')),
                ('created_date', models.DateField(auto_now_add=True, verbose_name='Creation date')),
                ('modified_date', models.DateField(auto_now=True, verbose_name='write date')),
                ('deleted_date', models.DateField(auto_now=True, verbose_name='Deleted date')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='Name')),
                ('vtex_id', models.CharField(max_length=200, verbose_name='Vtes ID')),
                ('keywords', models.CharField(max_length=200, verbose_name='Keywords')),
                ('title', models.CharField(max_length=200, verbose_name='Title')),
                ('remarketing_code', models.CharField(max_length=200, verbose_name='Remarketing Code')),
                ('global_category', models.CharField(max_length=200, verbose_name='ID Categoría global')),
                ('description', models.TextField(max_length=200, verbose_name='Description')),
                ('showing_storefront', models.BooleanField(verbose_name='Showing Storefront')),
                ('active', models.BooleanField(verbose_name='Active')),
                ('store_front_link', models.BooleanField(verbose_name='Store Front Link')),
                ('show_brand_filter', models.BooleanField(verbose_name='Show brand filter')),
                ('score', models.IntegerField(verbose_name='Score')),
                ('mtto', models.CharField(choices=[('LIST', 'List of SKUs'), ('COMBO', 'Combo Boxes'), ('RADIO', 'Icons with radio selection (radio box)'), ('SPECIFICATION', 'Following definition of SKU specification')], max_length=20, verbose_name='Score')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='subcategories', to='base.ecommercecategory')),
                ('platform', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.ecommercehub', verbose_name='Platform')),
            ],
            options={
                'verbose_name': 'Ecommerce category',
                'verbose_name_plural': 'categories',
            },
        ),
    ]
