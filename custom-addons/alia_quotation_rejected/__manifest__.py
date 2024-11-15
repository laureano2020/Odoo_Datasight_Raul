# Copyright 2015-${DATE} Alia Technologies, S.L. - http://www.alialabs.com
# @author: Alia Technologies
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

{
  'name': 'Alia Quotation Rejected - Quotation Extension',
  'summary': '',
  'version': '16.0.1.1.0',
  'author': 'Alia Technologies',
  'website': 'http://www.alialabs.com',
  'category': 'Proyecto Datasight Addons',
  'license': 'AGPL-3',
  'description': '''
       Alia Technologies: Quotation Rejected.
   ''',
  'depends': [
    # Project Dependencies
    # Base Dependencies
    'sale',
    'sale_management',
  ],
  'data': [
    # Security
    'security/ir.model.access.csv',
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
