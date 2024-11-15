# Copyright 2015-${DATE} Alia Technologies, S.L. - http://www.alialabs.com
# @author: Alia Technologies
{
  'name': 'Alia Reports - Invoice',
  'summary': 'Layout for Alia Reports: Invoice',
  'version': '16.0.0',
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
  ],
  'description': '''
       Alia Technologies reports add-on: Invoice Layout.
   ''',
  'depends': [
    # Project Dependencies
    'alia_reports_base',

    # Base Dependencies
    'account_payment',
    #'account_invoice_report_due_list',
    'account_payment_mode',
    'account_payment_partner',
  ],
  'data': [
    # Security
    # Data
    'report/report.xml',
    # Views
    'views/account_move_views.xml',
    'views/account_payment_mode.xml',
    'report/main.xml',
    'report/blocks/basic-info.xml',
    'report/blocks/basic-info/report-title.xml',
    'report/blocks/basic-info/invoice-info.xml',
    'report/blocks/concepts-table.xml',
    'report/blocks/payment-info.xml',
    'report/blocks/payment-info/payment-type.xml',
    'report/blocks/payment-info/taxes.xml',
    'report/blocks/payment-info/payments.xml',
    'report/blocks/payment-info/dues.xml',
    'report/blocks/payment-info/totals.xml',
  ],
  "assets": {
    "web.report_assets_common": [
      # SASS variables Assets
      "alia_reports_invoice/static/src/sass/variables.scss",
      # SASS files Assets
      "alia_reports_invoice/static/src/sass/directives.scss",
      "alia_reports_invoice/static/src/sass/main.scss",
      "alia_reports_invoice/static/src/sass/blocks/concepts-table.scss",
      "alia_reports_invoice/static/src/sass/blocks/payment-info/payment-type.scss",
      "alia_reports_invoice/static/src/sass/blocks/payment-info/dues.scss",
      "alia_reports_invoice/static/src/sass/blocks/payment-info/totals.scss",
    ],
  },
  'demo': [],
  'test': [],
  'installable': True,
  'auto_install': False,
  'application': False,
  'sequence': 121,
}
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).
