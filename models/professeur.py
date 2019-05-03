# -*- coding: utf-8 -*-

from odoo import models, fields, api

class partner(models.Model):
    _name = 'res.partner'
    _inherit = 'res.partner'

    class_id = fields.Many2many('iut.class',string='Classe')