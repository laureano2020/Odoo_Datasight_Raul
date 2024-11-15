# Copyright 2015-${DATE} Alia Technologies, S.L. - http://www.alialabs.com
# @author: Alia Technologies
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).
{
  'name': 'Alia Reports - Purchase Order',
  'summary': 'Layout for Alia Reports: Purchase Order',
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
       Alia Technologies reports add-on: Purchase Order Layout.
   ''',
  'depends': [
    # Project Dependencies
    'alia_reports_base',

    # Base Dependencies
    'purchase',
  ],
  'data': [
    # Security
    # Data
    'report/report.xml',
    # Views
    'views/purchase_order_views.xml',
    'report/main.xml',
    'report/blocks/basic-info.xml',
    'report/blocks/basic-info/order-info.xml',
    'report/blocks/basic-info/report-title.xml',
    'report/blocks/concepts-table.xml',
    'report/blocks/payment-info.xml',
  ],
  "assets": {
    "web.report_assets_common": [
      # SASS variables Assets
      "alia_reports_purchase_order/static/src/sass/variables.scss",
      # SASS files Assets
      "alia_reports_purchase_order/static/src/sass/directives.scss",
      "alia_reports_purchase_order/static/src/sass/main.scss",
      "alia_reports_purchase_order/static/src/sass/blocks/concepts-table.scss",
    ],
  },
  'demo': [],
  'test': [],
  'installable': True,
  'auto_install': False,
  'application': False,
  'sequence': 121,
}
