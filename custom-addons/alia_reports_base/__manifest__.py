# Copyright 2015-${DATE} Alia Technologies, S.L. - http://www.alialabs.com
# @author: Alia Technologies
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).
{
  'name': 'Alia Reports - Base',
  'summary': 'External layout and Common features for Alia Reports',
  'version': '16.0.0',
  'author': 'Alia Technologies',
  'website': 'http://www.alialabs.com',
  'category': 'ALIA - Tools',
  'license': 'AGPL-3',
  'contributors': [
    'Brais Saco <braissaco@alialabs.com>',
  ],
  'maintainers': [
    'Brais Saco <braissaco@alialabs.com>',
  ],
  'description': '''
       Alia Technologies reports add-on:
        - Overrides default web reports' external_layout.
        - Defines report's common blocks.
   ''',
  'depends': [
    # Project Dependencies
    # Base Dependencies
    'base',
    'web',
  ],
  'data': [
    # Security
    'security/res_groups.xml',
    # Data
    'report/paperformat.xml',
    # Views
    'report/main.xml',
    'report/external-layout/header.xml',
    'report/external-layout/footer.xml',
    'report/external-layout/pager.xml',
    'report/external-layout/header/company-info.xml',
    'report/external-layout/footer/contact-info.xml',
    'report/external-layout/footer/company-info.xml',
    'report/blocks/basic-info/client-info.xml',
    'report/blocks/basic-info/author-info.xml',
    'report/blocks/payment-info/totals.xml',
    'report/blocks/extras.xml',
  ],
  "assets": {

    "web.report_assets_common": [
      # SASS variables Assets
      "alia_reports_base/static/src/sass/variables.scss",
      # SASS common Assets
      "alia_reports_base/static/src/sass/common/_bootstrap-extend.scss",
      "alia_reports_base/static/src/sass/common/_functions.scss",
      "alia_reports_base/static/src/sass/common/_mixins.scss",
      "alia_reports_base/static/src/sass/common/_placeholders.scss",
      "alia_reports_base/static/src/sass/common/_classes.scss",
      # SASS files Assets
      "alia_reports_base/static/src/sass/directives.scss",
      "alia_reports_base/static/src/sass/fonts.scss",
      "alia_reports_base/static/src/sass/main.scss",
      "alia_reports_base/static/src/sass/external-layout/header.scss",
      "alia_reports_base/static/src/sass/external-layout/footer.scss",
      "alia_reports_base/static/src/sass/external-layout/pager.scss",
      "alia_reports_base/static/src/sass/blocks/basic-info/company-info.scss",
      "alia_reports_base/static/src/sass/blocks/basic-info/client-info.scss",
      "alia_reports_base/static/src/sass/blocks/basic-info/author-info.scss",
      "alia_reports_base/static/src/sass/blocks/payment-info/totals.scss",
      "alia_reports_base/static/src/sass/blocks/extras.scss",
    ],
  },
  'demo': [],
  'test': [],
  'installable': True,
  'auto_install': False,
  'application': False,
  'sequence': 120,
}
