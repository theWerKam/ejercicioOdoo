# -*- coding: utf-8 -*-
{
    'name': "formaciones",

    'summary': "Gestion de formaciones",

    'description': """
Modulo para gestionar todas las formaciones y especialidades del formador
    """,

    'author': "Jesus Santiago",
    'website': "https://www.linkiafp.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '1.0',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/cursos_views.xml',
        'views/especialidad_views.xml',
        'views/partner_views.xml',
        'views/menu_views.xml'
    ],
    'installable': True,
    'application': True,
}

