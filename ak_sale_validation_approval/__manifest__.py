# Copyright 2018 Akili Systems Pvt. Ltd. India
{
    'name': "Sale Order Approval",

    'summary': """
        With the help of this module your sale order is goes into the approve state if the subtotal is equal and higher than the 
        validation amount.""",

    'description': """
        With the help of this module your sale order is goes into the approve state if the subtotal is equal and higher than the 
        validation amount.
    """,

    'author': "Akili systems Pvt. Ltd.",
    'website': "http://www.akilisystems.in",
    'category': "tools",
    'version': "16.0.1",
    "license": "LGPL-3",

    # any module necessary for this one to work correctly
    'depends': ['sale'],

    # always loaded
    'data': [
        'views/sale_validation_approval_settings.xml',
        'views/sale_validation_approval.xml'
    ],
    'images': ['static/description/banner.jpg'],

    # only loaded in demonstration mode
    
    'autoinstall': False,
    'installable': True,
    'application': False
}
