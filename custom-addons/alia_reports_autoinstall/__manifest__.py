# Copyright 2015-${DATE} Alia Technologies, S.L. - http://www.alialabs.com
# @author: Alia
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).
{
   'name': 'Alia Reports AutoInstall',
   'summary': '',
   'version': '16.0.0',
   'author': 'Alia Technologies',
   'website': 'http://www.alialabs.com',
   'category': 'ALIA - Tools',
   'license': 'AGPL-3',
   'contributors': [
       'Alejandro Leonard <alejandro.leonard@alialabs.com>',
   ],
   'maintainers': [
       'Alejandro Leonard <alejandro.leonard@alialabs.com>',
   ],
   'description': '''
       Alia Technologies Addon.
   ''',
   'depends': [
       # Project Dependencies
       # Base Dependencies
       'base',
       'alia_reports_base',
       'alia_reports_invoice',
       'alia_reports_purchase_order',
       'alia_reports_sale_order',
       'alia_reports_stock',
       'alia_reports_agreement',
       'alia_l10n_es_reports',

   ],
   'demo': [],
   'data': [
       # Security
       # Data
       # Views
   ],
   'qweb': [],
   'demo': [],
   'test': [],
   'installable': True,
   'auto_install': False,
   'application': False,
   'sequence': 10,
}
