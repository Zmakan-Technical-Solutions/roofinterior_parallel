# -*- coding: utf-8 -*-
{
    'name': "Print Arabic and English",

    'summary': """
        This module is to print Invoice, Bills and POS receipt with arabic and english language """,

    'description': """
        This module is to print Invoice, Bills and POS receipt with arabic and english language 
    """,

    'author': "Zmakan Technical Solutions",
    'website': "http://www.zmakan.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Accounting',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','product','account','point_of_sale'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'templates.xml',
    ],
    'qweb': [
             'static/src/xml/OrderReceipt.xml',         
            ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
