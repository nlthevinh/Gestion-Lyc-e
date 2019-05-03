# -*- coding: utf-8 -*-

from odoo import models, fields, api
from dateutil.relativedelta import *

class eleve(models.Model):
    _name = 'iut.student'

    firstname = fields.Char(string="Prénom de l'élève",required=True)
    lastname = fields.Char(string="Nom de l'élève",required=True)
    birthdate = fields.Date(string="Date de naissance")
    age = fields.Integer(string="Age de l'élève", compute='_compute_age')
    
    class_id = fields.Many2one('iut.class')
    
    @api.depends('birthdate')
    def _compute_age(self):
        for record in self:
            if record.birthdate and record.birthdate <= fields.Date.today():
                record.age = relativedelta(fields.Date.from_string(fields.Date.today()),fields.Date.from_string(record.birthdate)).years 
            else: 
                record.age = 0