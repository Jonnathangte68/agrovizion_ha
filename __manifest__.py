# -*- coding: utf-8 -*-
{
    'name': "aplicacion_ha",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        #'security/ir.model.access.csv',
        'views/report_ha.xml',
        'views/views.xml',
        'views/hapdf.xml',
        'views/commentarios.xml',
        'views/ha.xml',
        'views/evaljefe.xml',
        'views/evalproceso.xml',
        'views/fecha_corte.xml',
        'views/menu_principal.xml',

    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}