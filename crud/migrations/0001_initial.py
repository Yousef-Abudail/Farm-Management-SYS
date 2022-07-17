# Generated by Django 4.0.5 on 2022-07-03 13:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Disease',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=30, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Farmers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=30, null=True)),
                ('discreption', models.CharField(blank=True, max_length=200, null=True)),
                ('cost_per_hour', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Fertilizer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=30, null=True)),
                ('cost', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Land',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=30, null=True)),
                ('size', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Medicine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=30, null=True)),
                ('cost', models.IntegerField(blank=True, null=True)),
                ('disease', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='crud.disease')),
            ],
        ),
        migrations.CreateModel(
            name='Pesticides',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=30, null=True)),
                ('cost', models.IntegerField(blank=True, null=True)),
                ('pesticide_land', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='crud.land')),
            ],
        ),
        migrations.CreateModel(
            name='Plant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=30, null=True)),
                ('seed_cost', models.IntegerField(blank=True, null=True)),
                ('plant_land', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='crud.land')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=30, null=True)),
                ('Password', models.CharField(blank=True, max_length=30, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='TCost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_cost', models.IntegerField(blank=True, null=True)),
                ('water_cost', models.IntegerField(blank=True, null=True)),
                ('fertilizer_cost', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='crud.fertilizer')),
                ('labor_cost', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='crud.farmers')),
                ('land_name', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='crud.land')),
                ('medicine_cost', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='crud.medicine')),
                ('pesticides_cost', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='crud.pesticides')),
                ('seed_cost', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='crud.plant')),
            ],
        ),
        migrations.CreateModel(
            name='Sales',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('crop_weight', models.IntegerField(blank=True, null=True)),
                ('sale_price', models.IntegerField(blank=True, null=True)),
                ('land_name', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='crud.land')),
            ],
        ),
        migrations.AddField(
            model_name='pesticides',
            name='plant',
            field=models.ManyToManyField(blank=True, to='crud.plant'),
        ),
        migrations.AddField(
            model_name='fertilizer',
            name='fertilizer_land',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='crud.land'),
        ),
        migrations.AddField(
            model_name='fertilizer',
            name='fertilizer_plant',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='crud.plant'),
        ),
        migrations.AddField(
            model_name='farmers',
            name='farmer_land',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='crud.land'),
        ),
        migrations.AddField(
            model_name='disease',
            name='disease_plant',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='crud.plant'),
        ),
    ]
