# -*- coding: utf-8 -*-

from odoo import models, fields, api

class agenda(models.Model):
    _name = 'iut.schedule'
    _order = "date_start"

    date_start = fields.Datetime(string="Heure de début de la période",required=True)
    date_stop = fields.Datetime(string="Heure de fin de la période",required=True)
    room = fields.Char(string="Salle de la période")
    
    class_id = fields.Many2one('iut.class')
    course_id = fields.Many2one('iut.course')