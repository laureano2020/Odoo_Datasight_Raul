# Copyright 2015-${DATE} Alia Technologies, S.L. - http://www.alialabs.com
# @author: Alia Technologies
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).
{
  'name': 'Alia Reports - Stock',
  'summary': 'Layout for Alia Reports: Stock',
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
       Alia Technologies reports add-on: Stock Reports Layout.
   ''',
  'depends': [
    # Project Dependencies
    'alia_reports_base',

    # Base Dependencies
    'stock',
  ],
  'data': [
    # Security
    # Data
    'report/report.xml',
    # Views
    'views/stock_picking_views.xml',
    'report/delivery-slip/main.xml',
    'report/delivery-slip/blocks/basic-info.xml',
    'report/delivery-slip/blocks/basic-info/report-title.xml',
    'report/delivery-slip/blocks/basic-info/report-info.xml',
    'report/delivery-slip/blocks/order-table.xml',
    'report/delivery-slip/blocks/concepts-table.xml',
    'report/delivery-slip/blocks/concepts-done-table.xml',
    'report/delivery-slip/blocks/shipping-warning.xml',
  ],
  "assets": {
    "web.report_assets_common": [
      # SASS variables Assets
      "alia_reports_stock/static/src/sass/variables.scss",
      # SASS files Assets
      "alia_reports_stock/static/src/sass/directives.scss",
      "alia_reports_stock/static/src/sass/main.scss",
      "alia_reports_stock/static/src/sass/delivery-slip/main.scss",
      "alia_reports_stock/static/src/sass/delivery-slip/blocks/order-table.scss",
      "alia_reports_stock/static/src/sass/delivery-slip/blocks/concepts-table.scss",
      "alia_reports_stock/static/src/sass/delivery-slip/blocks/concepts-done-table.scss",
      "alia_reports_stock/static/src/sass/delivery-slip/blocks/shipping-warning.scss",
    ],
  },
  'demo': [],
  'test': [],
  'installable': True,
  'auto_install': False,
  'application': False,
  'sequence': 121,
}
