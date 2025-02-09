# Generated by Django 5.1.2 on 2024-10-09 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ClothingProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('brand', models.CharField(max_length=100)),
                ('size', models.CharField(choices=[('S', 'Small'), ('M', 'Medium'), ('L', 'Large'), ('XL', 'Extra Large')], max_length=3)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('description', models.TextField()),
                ('category', models.CharField(choices=[('T', 'T-Shirts'), ('D', 'Dresses'), ('J', 'Jeans'), ('S', 'Shirts'), ('O', 'Others')], max_length=3)),
                ('color', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='products/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
