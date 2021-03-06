# Generated by Django 2.2.2 on 2019-09-02 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TshirtBooking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=120)),
                ('booking_id', models.CharField(max_length=120)),
                ('tshirt_size', models.CharField(blank=True, choices=[('S', 'Small'), ('M', 'Medium'), ('L', 'Large'), ('XL', 'Extra Large'), ('XXL', 'Double Extra Large')], max_length=3, verbose_name='Talla')),
                ('sex', models.CharField(blank=True, choices=[('M', 'Hombre'), ('F', 'Mujer')], max_length=1, verbose_name='Tallaje')),
                ('nif', models.CharField(blank=True, help_text='Ingresa tu ID', max_length=9, verbose_name='NIF/NIE')),
                ('date_sent', models.DateTimeField(auto_now_add=True, null=True)),
            ],
            options={
                'unique_together': {('email', 'booking_id')},
            },
        ),
    ]
