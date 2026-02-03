# -*- coding: utf-8 -*-
{
    'name': "incidencias",

    'summary': """
    Un modulo para el primer reto de SGE.
    """,

    'description': """
        Este modulo es el primero modulo que hemos creado en el reto de SGE
    """,

    'author': "Grupo 3",
    'website': "https://www.linkedin.com/in/mosi-hickman-blanco-093623349/",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Services',  # Antes Uncategorized
    'version': '0.2',

    # any module necessary for this one to work correctly
    'depends': ['project', 'hr'],

    # always loaded
    'data': [
        'security/groups.xml',
        'security/ir.model.access.csv',
        'views/actions.xml',
        'views/menu.xml',
        'views/encuestaView.xml',
        'views/adjuntoView.xml',
        'views/incidencias.xml',
        'views/comentarios.xml',
        'views/views.xml',
        #'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        #'demo/demo.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
