# -*- coding: utf-8 -*-

{
    'name': 'Sale Order Approve from List View',
    'version': '16.0.1.0.0',
    'category': 'Sales/Sales',
    'license': 'LGPL-3',
    'summary': """Approve your sales orders from list views""",
    'depends': [
        'base',
        'sale',
        'sale_management',
    ],
    'author': 'SugarClone ERP',
    'support': 'sugarcloneerp@gmail.com',
    'description': """ Updates Below
    - Approve and cancel sale order from list view
    """,
    'data': [
        'views/sale_order_views.xml',
    ],
    'images': ['static/description/banner.png'],
    'installable': True,
    'auto_install': False,
    'application': False,
}
