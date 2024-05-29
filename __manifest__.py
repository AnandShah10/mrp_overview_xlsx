# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.


{
    'name': 'mrp_overview_xlsx',
    'version': '1.0',
    'website': 'https://www.odoo.com/app/manufacturing',
    'author': "anand",
    'category': 'Custom/Manufacturing',
    'sequence': 55,
    'summary': 'Manufacturing Orders & BOMs Xlsx Report',
    'depends': ['product', 'stock', 'resource', 'mrp'],
    'data': [
        'report/report.xml',
    ],
    'application': False,
    'assets': {
        'web.assets_backend': [
            'mrp_overview_xlsx/static/src/**/*',
        ],
    },
    'license': 'LGPL-3',
}
