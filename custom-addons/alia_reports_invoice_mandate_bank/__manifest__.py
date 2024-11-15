# Copyright 2015-${DATE} Alia Technologies, S.L. - http://www.alialabs.com
# @author: Alia
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).
{
   'name': 'Alia Report Invoice Mandate Bank',
   'summary': '',
   'version': '14.0.1.0.0',
   'author': 'Alia Technologies',
   'website': 'http://www.alialabs.com',
   'category': 'ALIA - Tools',
   'license': 'AGPL-3',
   'contributors': [
       'Sidro Vázquez <sidro.vazquez@alialabs.com>',
   ],
   'maintainers': [
       'Sidro Vázquez <sidro.vazquez@alialabs.com>',
   ],
   'description': '''
       Alia Technologies Addon.
   ''',
   'depends': [
       # Project Dependencies
       'alia_reports_invoice',
       # Base Dependencies
       'base',
       'account',
       'account_banking_mandate',
   ],
   'demo': [],
   'data': [
       # Security
       # Data
       # Views
       'report/payment-type.xml',

   ],
   'qweb': [],
   'demo': [],
   'test': [],
   'installable': True,
   'auto_install': False,
   'application': False,
   'sequence': 10,
}
