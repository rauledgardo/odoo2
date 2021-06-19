# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Website Product Description',
    'category': 'eCommerce',
    'version': '14.0',
    'author': 'SprintERP',
    'website': 'www.sprinterp.com',
    'summary': """This plugin use for display Website Product Description filed in Product form.""",
    'description': """This plugin use for display Website Product Description filed in Product form.""",
    'depends': ['website_sale'],
    'data': [
        'views/eCommerce_description_views.xml',
    ],
    'license': 'LGPL-3',
    'images': ['static/description/banner.gif'],
    'application': True,
    'installable': True,
    'price': 7,
	'currency': 'EUR',
}
