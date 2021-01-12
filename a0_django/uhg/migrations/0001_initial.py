# Generated by Django 3.1.4 on 2021-01-02 02:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Buddy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='EquipmentType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('equType', models.CharField(max_length=20, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='EquipmentUsed',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Friend',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('friendedBack', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Hike',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('checkInDate', models.DateTimeField(auto_now_add=True)),
                ('checkOutDate', models.DateTimeField(null=True)),
                ('review', models.CharField(max_length=500, null=True)),
                ('difficulty', models.IntegerField(null=True)),
                ('enjoyability', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Hiker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('birthday', models.DateField(null=True)),
                ('city', models.CharField(max_length=50, null=True)),
                ('state', models.CharField(max_length=50, null=True)),
                ('skillLevel', models.IntegerField()),
                ('bio', models.CharField(max_length=500, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timeSent', models.DateTimeField(auto_now_add=True)),
                ('content', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='SuggestedEquipment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Trail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('prop', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=50)),
                ('isOpen', models.BooleanField()),
                ('altitudeChange', models.IntegerField()),
                ('distance', models.IntegerField()),
                ('fee', models.FloatField()),
            ],
        ),
        migrations.AddConstraint(
            model_name='trail',
            constraint=models.UniqueConstraint(fields=('name', 'prop'), name='uniqueTrail'),
        ),
        migrations.AddField(
            model_name='tag',
            name='trailID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tags', to='uhg.trail'),
        ),
        migrations.AddField(
            model_name='suggestedequipment',
            name='equipmentTypeID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='uhg.equipmenttype'),
        ),
        migrations.AddField(
            model_name='suggestedequipment',
            name='trailID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='suggestedEquipment', to='uhg.trail'),
        ),
        migrations.AddField(
            model_name='message',
            name='hikerID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='messagesSent', to='uhg.hiker'),
        ),
        migrations.AddField(
            model_name='message',
            name='recipientID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='messagesReceived', to='uhg.hiker'),
        ),
        migrations.AddField(
            model_name='hiker',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='hike',
            name='hiker',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hikes', to='uhg.hiker'),
        ),
        migrations.AddField(
            model_name='hike',
            name='trail',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hikes', to='uhg.trail'),
        ),
        migrations.AddField(
            model_name='friend',
            name='friendID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='friendedBy', to='uhg.hiker'),
        ),
        migrations.AddField(
            model_name='friend',
            name='hikerID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='friends', to='uhg.hiker'),
        ),
        migrations.AddField(
            model_name='equipmentused',
            name='equipmentID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='uhg.equipmenttype'),
        ),
        migrations.AddField(
            model_name='equipmentused',
            name='hikeID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='equipmentUsed', to='uhg.hike'),
        ),
        migrations.AddField(
            model_name='buddy',
            name='friendID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='buddies', to='uhg.hiker'),
        ),
        migrations.AddField(
            model_name='buddy',
            name='hikeID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='buddies', to='uhg.hike'),
        ),
        migrations.AddConstraint(
            model_name='tag',
            constraint=models.UniqueConstraint(fields=('trailID', 'tag'), name='uniqueTag'),
        ),
        migrations.AddConstraint(
            model_name='suggestedequipment',
            constraint=models.UniqueConstraint(fields=('trailID', 'equipmentTypeID'), name='uniqueSuggestedEquipment'),
        ),
        migrations.AddConstraint(
            model_name='message',
            constraint=models.UniqueConstraint(fields=('hikerID', 'recipientID', 'timeSent'), name='uniqueMessage'),
        ),
        migrations.AddConstraint(
            model_name='hike',
            constraint=models.UniqueConstraint(fields=('hiker', 'trail', 'checkInDate'), name='uniqueHikes'),
        ),
        migrations.AddConstraint(
            model_name='friend',
            constraint=models.UniqueConstraint(fields=('hikerID', 'friendID'), name='uniqueFriend'),
        ),
        migrations.AddConstraint(
            model_name='equipmentused',
            constraint=models.UniqueConstraint(fields=('hikeID', 'equipmentID'), name='uniqueEquipmentUsed'),
        ),
        migrations.AddConstraint(
            model_name='buddy',
            constraint=models.UniqueConstraint(fields=('hikeID', 'friendID'), name='uniqueBuddy'),
        ),
        migrations.AddConstraint(
            model_name='buddy',
            constraint=models.CheckConstraint(check=models.Q(hikeID__hikerID__id__lt=3), name='checkBuddy_notSelf'),
        ),
    ]
