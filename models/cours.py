# -*- coding: utf-8 -*-

from odoo import models, fields, api

class cours(models.Model):
    _name = 'iut.course'
    _sql_constraints = {
        ('name_unique', 'unique(name)', 'Ce nom existe déjà')
    }

    name = fields.Char(string="Nom du cours",required=True)
    
    schedule_ids = fields.One2many('iut.schedule', 'course_id')
    