{
    'name': 'Purchase Category',
    'version': '16.0.1.0.0',
    'category': 'Purchase',
    'summery': 'This app will purchase category.',
    'author': 'INKERP',
    'website': "http://www.inkerp.com/",
    'depends': ['purchase'],
    'data': [
            'views/purchase_order_view.xml',
            'views/purchase_category_view.xml',
            'security/ir.model.access.csv',
    ],

    'images': ['static/description/banner.png'],
    'license': "OPL-1",
    'installable': True,
    'application': True,
    'auto_install': False,
}
