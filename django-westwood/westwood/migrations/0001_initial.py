# Generated by Django 2.2.5 on 2019-10-02 23:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ability',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('games', models.IntegerField()),
                ('description', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('generation', models.IntegerField(default=0)),
                ('release_date', models.DateTimeField()),
                ('system', models.CharField(max_length=500)),
                ('region', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='LearnMethod',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Learnset',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('games', models.IntegerField()),
                ('learnset_moves', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='LearnsetMove',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('level', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Move',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('generation', models.IntegerField(default=0)),
                ('type_1', models.CharField(max_length=500)),
                ('base_power', models.CharField(max_length=500)),
                ('power_points', models.IntegerField(default=0)),
                ('accuracy', models.CharField(max_length=500)),
                ('priority', models.CharField(max_length=500)),
                ('damage_category', models.CharField(max_length=500)),
                ('effect', models.CharField(max_length=500, null=True)),
                ('effect_chance', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='PokedexNumber',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('number', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Pokemon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('pokedex_numbers', models.IntegerField()),
                ('height', models.IntegerField(default=0)),
                ('weight', models.IntegerField(default=0)),
                ('stat_sets', models.IntegerField()),
                ('type_sets', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='PokemonLearnsets',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('learnsets', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='PokemonTmSets',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('tm_sets', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='StatSet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('games', models.IntegerField()),
                ('hp', models.IntegerField(default=0)),
                ('attack', models.IntegerField(default=0)),
                ('defense', models.IntegerField(default=0)),
                ('special_attack', models.IntegerField(default=0)),
                ('special_defense', models.IntegerField(default=0)),
                ('speed', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='TmSet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('games', models.IntegerField()),
                ('tmset_moves', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='TmsetMove',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='TypeSet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('games', models.IntegerField()),
                ('type1', models.CharField(max_length=500)),
                ('type2', models.CharField(max_length=500, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='TypesListElement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('list_id', models.IntegerField()),
                ('sequence_number', models.IntegerField()),
                ('element', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='westwood.Type')),
            ],
        ),
        migrations.CreateModel(
            name='TypeSetsListElement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('list_id', models.IntegerField()),
                ('sequence_number', models.IntegerField()),
                ('element', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='westwood.TypeSet')),
            ],
        ),
        migrations.CreateModel(
            name='TmSetsListElement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('list_id', models.IntegerField()),
                ('sequence_number', models.IntegerField()),
                ('element', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='westwood.TmSet')),
            ],
        ),
        migrations.CreateModel(
            name='TmsetMovesListElement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('list_id', models.IntegerField()),
                ('sequence_number', models.IntegerField()),
                ('element', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='westwood.TmsetMove')),
            ],
        ),
        migrations.CreateModel(
            name='StatSetsListElement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('list_id', models.IntegerField()),
                ('sequence_number', models.IntegerField()),
                ('element', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='westwood.StatSet')),
            ],
        ),
        migrations.CreateModel(
            name='PokedexNumbersListElement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('list_id', models.IntegerField()),
                ('sequence_number', models.IntegerField()),
                ('element', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='westwood.PokedexNumber')),
            ],
        ),
        migrations.CreateModel(
            name='LearnsetsListElement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('list_id', models.IntegerField()),
                ('sequence_number', models.IntegerField()),
                ('element', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='westwood.Learnset')),
            ],
        ),
        migrations.CreateModel(
            name='LearnsetMovesListElement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('list_id', models.IntegerField()),
                ('sequence_number', models.IntegerField()),
                ('element', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='westwood.LearnsetMove')),
            ],
        ),
        migrations.CreateModel(
            name='LearnMethodsListElement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('list_id', models.IntegerField()),
                ('sequence_number', models.IntegerField()),
                ('element', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='westwood.LearnMethod')),
            ],
        ),
        migrations.CreateModel(
            name='GamesListElement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('list_id', models.IntegerField()),
                ('sequence_number', models.IntegerField()),
                ('element', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='westwood.Game')),
            ],
        ),
    ]
