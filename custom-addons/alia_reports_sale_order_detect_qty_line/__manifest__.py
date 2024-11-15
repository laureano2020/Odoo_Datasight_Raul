# Copyright 2015-${DATE} Alia Technologies, S.L. - http://www.alialabs.com
# @author: Alia Technologies
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

{
  'name': 'Alia Reports - Sale Order Detect Qty on Line',
  'summary': 'If a line\'s quantity is zero, don\'t show that line. ',
  'version': '14.0.1.1.0',
  'author': 'Alia Technologies',
  'website': 'http://www.alialabs.com',
  'category': 'ALIA - Tools',
  'license': 'AGPL-3',
  'contributors': [
    'Alejandro Leonard <alejandroleonard@alialabs.com>',
  ],
  'maintainers': [
    'Brais Saco <braissaco@alialabs.com>',
    'Alejandro Leonard <alejandroleonard@alialabs.com>',
  ],
  'description': '''
       Alia Technologies reports add-on: Sale Order Layout.
   ''',
  'depends': [
    # Project Dependencies
    'alia_reports_sale_order',

    # Base Dependencies
  ],
  'data': [
    # Security
    # Data
    'report/report_sale_order.xml',

  ],
  'qweb': [],
  'demo': [],
  'test': [],
  'installable': True,
  'auto_install': False,
  'application': False,
  'sequence': 121,
}
