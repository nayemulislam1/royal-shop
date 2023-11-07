# Generated by Django 4.2.7 on 2023-11-07 21:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('product', '0003_rename_catagory_product_catagory_wishlist'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0002_multi_address'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quentity', models.PositiveIntegerField(default=1)),
                ('Order_Confirm', models.BooleanField(default=False)),
                ('Confirm_Time', models.DateTimeField(auto_now_add=True)),
                ('Payment_ID', models.CharField(blank=True, max_length=300, null=True)),
                ('Order_ID', models.CharField(blank=True, max_length=300, null=True)),
                ('Status', models.CharField(choices=[('Accepted', 'Accepted'), ('Packed', 'Packed'), ('On The Way', 'On The Way'), ('Delivered', 'Delivered'), ('Cancel', 'Cancel')], max_length=30)),
                ('Pyment_Method', models.CharField(choices=[('Cash On Delivery', 'Cash On Delivery'), ('Pyple', 'Pyple'), ('SSL Commerz', 'SSL Commerz')], default='Cash On Delivery', max_length=50)),
                ('Delivery_address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.multi_address')),
                ('Order_Products', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='product.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
