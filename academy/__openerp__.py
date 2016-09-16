# -*- coding: utf-8 -*-
{
    'name': "academy",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Training Module September 2016
    """,

    'author': "Nicola",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': [
        'base',
        'crm',
        'board',
        'website',
    ],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'data/course.xml',

        'views/course.xml',
        'views/session.xml',
        'views/partner.xml',
        'views/session_populate.xml',

        'workflow/session.xml',

        'reports/session.xml',
        'reports/board.xml',

        'templates/session.xml',
        'templates/course.xml',

        'security/security.xml',
        'security/ir.model.access.csv',
    ],
    # only loaded in demonstration mode
    'demo': [
    ],
}