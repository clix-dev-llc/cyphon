# -*- coding: utf-8 -*-
# Copyright 2017 Dunbar Cybersecurity.
#
# This file is part of Cyphon Engine.
#
# Cyphon Engine is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Cyphon Engine is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Cyphon Engine. If not, see <http://www.gnu.org/licenses/>.
#
# Generated by Django 1.11.2 on 2017-11-02 20:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('requisitions', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FieldCoupling',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('field_name', models.CharField(help_text='The name of the data field that will supply a value for the parameter.', max_length=64, verbose_name='field name')),
                ('parameter', models.ForeignKey(help_text='The target parameter in the REST API request.', on_delete=django.db.models.deletion.CASCADE, related_name='field_couplings', related_query_name='field_coupling', to='requisitions.Parameter', verbose_name='parameter')),
            ],
            options={
                'ordering': ['supply_link', 'parameter'],
                'verbose_name': 'field coupling',
                'verbose_name_plural': 'field couplings',
            },
        ),
        migrations.CreateModel(
            name='SupplyChain',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True, verbose_name='name')),
            ],
            options={
                'verbose_name': 'supply chain',
                'verbose_name_plural': 'supply chains',
            },
        ),
        migrations.CreateModel(
            name='SupplyLink',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True, verbose_name='name')),
                ('position', models.IntegerField(default=0, help_text='An integer representing the order of this Supply Link in the Supply Chain.', verbose_name='position')),
                ('requisition', models.ForeignKey(help_text='The Requisition that defines the REST API request being made.', on_delete=django.db.models.deletion.CASCADE, to='requisitions.Requisition', verbose_name='requisition')),
                ('supply_chain', models.ForeignKey(help_text='The Supply Chain to which this Supply Link belongs.', on_delete=django.db.models.deletion.CASCADE, related_name='supply_links', related_query_name='supply_link', to='supplychains.SupplyChain', verbose_name='supply chain')),
                ('time_unit', models.CharField(choices=[('s', 'Seconds'), ('m', 'Minutes'), ('h', 'Hours'), ('d', 'Days')], default='m', help_text='Units for the wait time.', max_length=3, verbose_name='time unit')),
                ('wait_time', models.IntegerField(default=0, help_text='An integer representing the time to wait before executing the Requisition following execution of the previous step in the Supply Chain.', verbose_name='wait interval')),
            ],
            options={
                'ordering': ['supply_chain', 'position'],
                'verbose_name': 'supply link',
                'verbose_name_plural': 'supply links',
            },
        ),
        migrations.AddField(
            model_name='fieldcoupling',
            name='supply_link',
            field=models.ForeignKey(help_text='The Supply Link that uses this Field Coupling.', on_delete=django.db.models.deletion.CASCADE, related_name='field_couplings', related_query_name='field_coupling', to='supplychains.SupplyLink', verbose_name='supply link'),
        ),
        migrations.AlterUniqueTogether(
            name='supplylink',
            unique_together=set([('supply_chain', 'position')]),
        ),
        migrations.AlterUniqueTogether(
            name='fieldcoupling',
            unique_together=set([('supply_link', 'parameter')]),
        ),
    ]
