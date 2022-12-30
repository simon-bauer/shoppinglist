# Generated by Django 4.1.4 on 2022-12-30 13:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ShoppingItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('position', models.CharField(choices=[('0', '0_Irgendwo'), ('1', '1_Obst'), ('2', '2_Käse'), ('3', '3_Joghurt'), ('4', '4_Nudeln'), ('5', '5_Getränke')], default='0', max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='ShoppingListItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('done', models.BooleanField(default=False)),
                ('shopping_item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='listapp.shoppingitem')),
            ],
        ),
    ]