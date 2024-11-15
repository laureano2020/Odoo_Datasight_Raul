# Copyright 2015-${DATE} Alia Technologies, S.L. - http://www.alialabs.com
# @author: Alia Technologies
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

{
  'name': 'Alia Reports - Sale Order',
  'summary': 'Layout for Alia Reports: Sale Order',
  'version': '16.0.0',
  'author': 'Alia Technologies',
  'website': 'http://www.alialabs.com',
  'category': 'ALIA - Tools',
  'license': 'AGPL-3',
  'contributors': [
    'Brais Saco <braissaco@alialabs.com>',
    'Cástor Sánchez <castorsanchez@alialabs.com>',
  ],
  'maintainers': [
    'Brais Saco <braissaco@alialabs.com>',
  ],
  'description': '''
       Alia Technologies reports add-on: Sale Order Layout.
   ''',
  'depends': [
    # Project Dependencies
    'alia_reports_base',

    # Base Dependencies
    'sale_management',
    'product',
    'account_payment_partner'
  ],
  'data': [
    # Security
    # Data
    'report/report.xml',
    # Views
    'views/sale_order_views.xml',
    'report/main.xml',
    'report/blocks/basic-info.xml',
    'report/blocks/basic-info/report-title.xml',
    'report/blocks/basic-info/order-info.xml',
    'report/blocks/basic-info/order-info/report-date.xml',
    'report/blocks/concepts-table.xml',
    'report/blocks/terms-and-other-info.xml',
    'report/blocks/terms-and-other-info/other-info.xml',
    'report/blocks/terms-and-other-info/author-info.xml',
    'report/blocks/payment-info.xml',
    'report/blocks/extras.xml',
  ],
  "assets": {
    "web.report_assets_common": [
      # SASS variables Assets
      "alia_reports_sale_order/static/src/sass/variables.scss",
      # SASS files Assets
      "alia_reports_sale_order/static/src/sass/directives.scss",
      "alia_reports_sale_order/static/src/sass/main.scss",
    ],
  },
  'demo': [],
  'test': [],
  'installable': True,
  'auto_install': False,
  'application': False,
  'sequence': 121,
}
