# Copyright 2015-${DATE} Alia Technologies, S.L. - http://www.alialabs.com
# @author: Alia Technologies
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

{
  'name': 'Alia Reports - Redefine Mail Template Files',
  'summary': 'Module that redefines the report to send on emails.',
  'version': '14.0.1.1.0',
  'author': 'Alia Technologies',
  'website': 'http://www.alialabs.com',
  'category': 'ALIA - Tools',
  'license': 'AGPL-3',
  'contributors': [
    'Alejandro Leonard <alejandroleonard@alialabs.com>',
  ],
  'maintainers': [
    'Alejandro Leonard <alejandroleonard@alialabs.com>',
  ],
  'description': '''
       Alia Technologies reports add-on: Sale Order Layout.
   ''',
  'depends': [
    # Project Dependencies
    'sale',
    'alia_reports_sale_order',
    'alia_reports_invoice',
    'alia_reports_purchase_order',
    'alia_reports_stock',
    # 'alia_reports_autoinstall', #dependency add so all the templates are loaded

    # Base Dependencies
  ],
  'data': [
    # Security
    # Data
    'data/mail_template_data.xml',

  ],
  'qweb': [],
  'demo': [],
  'test': [],
  'installable': True,
  'auto_install': False,
  'application': False,
  'sequence': 121,
}
