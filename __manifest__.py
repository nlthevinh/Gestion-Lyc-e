# -*- coding: utf-8 -*-
{
    'name': "gestion_lycee",

    'summary': """
        Module de gestion de classes de lycée""",

    'description': """
        Module de gestion de classes de lycée
    """,

    'author': "Ly The Vinh NGO",
    'website': "http://www.team-dsi.fr",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/agenda.xml',
        'views/classe.xml',
        'views/cours.xml',
        'views/eleve.xml',
        'views/menu.xml',
        'views/professeur.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}