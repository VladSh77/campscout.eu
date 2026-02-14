{
    'name': 'CampScout: Core Management',
    'version': '1.1',
    'category': 'Operations',
    'summary': 'Базовий модуль для управління таборами та інтеграція з картою дитини',
    'author': 'CampScout Team (Volodymyr Shevchenko)',
    'website': 'https://campscout.eu',
    'license': 'LGPL-3',
    'depends': ['base', 'product', 'event', 'sale', 'website_sale'],
    'data': [
        'views/campscout_menus.xml',
        'views/website_sale_templates.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
