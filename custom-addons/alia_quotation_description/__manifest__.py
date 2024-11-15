# Copyright 2015-${DATE} Alia Technologies, S.L. - http://www.alialabs.com
# @author: Alia Technologies
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

{
  'name': 'Alia Quotation Description',
  'summary': '',
  'version': '16.0.1.1.0',
  'author': 'Alia Technologies',
  'website': 'http://www.alialabs.com',
  'category': 'Proyecto Datasight Addons',
  'license': 'AGPL-3',
  'description': '''
       Alia Technologies: Quotation Description.
   ''',
  'depends': [
    # Project Dependencies
    # Base Dependencies
    'sale',
    'sale_management',
  ],
  'data': [
    # Security
    # Data
    'views/sale_order_view.xml',
  ],
  'qweb': [],
  'demo': [],
  'test': [],
  'installable': True,
  'auto_install': False,
  'application': False,
  'sequence': 121,
}
