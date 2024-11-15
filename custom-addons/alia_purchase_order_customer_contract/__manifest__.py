# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.
{
    'name': 'Alia Purchase Order Customer Contract',
    'version': '16.0.1.0.0',
    'category':'Datasight Project Addons',
    'license':'OPL-1',
    'summary': """Establish a relationship between purchase orders and customer contracts.
    """,
    'description':"""
    """,
    'author': 'Alia Technologies S.L.',
    'depends':[
        # Project Dependencies
        # Base Dependencies
        'purchase',
        'contract',
    ],
    'data':[
        'views/contract_contract.xml',
        'views/purchase_order.xml'
        ],
    'installable': True,
    'auto_install': False,
}

