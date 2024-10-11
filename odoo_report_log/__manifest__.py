{
    'name': 'Report Log',
    'version': '1.1',
    'category': 'Others',
    'summary': 'Generates log record each time a report is printed.',
    'description': """Generates log record each time a report is printed.""",
    'depends': ['web'],
    'author': 'OdooBot, Altela Software',
    'license': 'LGPL-3',
    'website': 'www.altelasoftware.com',
    'images': [
        'static/src/img/screenshot.png',
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/ir_report_views.xml',
        'views/report_log_views.xml',
    ],
    'application': False,
}
