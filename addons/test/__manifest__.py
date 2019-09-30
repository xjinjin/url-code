# -*- coding: utf-8 -*-
{
    'name': "url2code",

    'summary': """
        url2code""",

    'description': """
        url2code
    """,

    'author': "jinjin xu",
    'website': "https://github.com/xjinjin/url-code",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'yct/analysis',
    'version': '1.0',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        # 'views/test.xml',
        'views/test1.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}