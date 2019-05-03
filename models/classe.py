# -*- coding: utf-8 -*-

from odoo import models, fields, api

class classe(models.Model):
    _name = 'iut.class'
    _sql_constraints = {
        ('name_unique', 'unique(name)', 'Ce nom existe déjà')
    }

    name = fields.Char(string="Nom de la classe",required=True)
    level = fields.Selection([('seconde', 'Seconde'), ('premiere', 'Première'), ('terminale', 'Terminale')],'Niveau')
    student_nb = fields.Integer(string="Nombre d'élève dans la classe", compute='_compute_eleve_nb')
    
    teacher_id = fields.Many2many('res.partner',string='Professeur')
    student_ids = fields.One2many('iut.student', 'class_id')
    schedule_id = fields.One2many('iut.schedule', 'class_id')
    
    course_id = fields.Char(string="Cours de la classe", related='schedule_id.course_id.name', store=True)
    
    @api.depends('student_ids')
    def _compute_eleve_nb(self):
        resultat = 0
        for record in self:
            for eleve in record.student_ids:
                resultat = resultat + 1
            record.student_nb = resultat