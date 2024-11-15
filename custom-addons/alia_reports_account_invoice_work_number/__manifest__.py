# Copyright 2015-${DATE} Alia Technologies, S.L. - http://www.alialabs.com
# @author: Alia Technologies
{
  'name': 'Alia Reports - Invoice With Work Number',
  'summary': 'Layout for Alia Reports: Invoice Group By Picking',
  'version': '14.0.1.1.0',
  'author': 'Alia Technologies',
  'website': 'http://www.alialabs.com',
  'category': 'ALIA - Tools',
  'license': 'AGPL-3',
  'contributors': [
    'Sidro Vázquez <sidro.vazquez@alialabs.com>',
    'Brais Saco <braissaco@alialabs.com>',
  ],
  'maintainers': [
    'Sidro Vázquez <sidro.vazquez@alialabs.com>',
    'Brais Saco <braissaco@alialabs.com>',
    'Alejandro Leonard <alejandroleonard@alialabs.com>',
  ],
  'description': '''
       Alia Technologies reports add-on: Invoice Layout.
   ''',
  'depends': [
    # Project Dependencies

    'alia_reports_account_invoice_group_by_sale_order',
    'alia_sale_order_work_number',
  ],
  'data': [
    # Security
    # Dataa
    # Views
    'report/report_invoice.xml',

  ],
  'qweb': [],
  'demo': [],
  'test': [],
  'installable': True,
  'auto_install': False,
  'application': False,
  'sequence': 121,
}
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).
