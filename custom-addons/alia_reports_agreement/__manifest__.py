# Copyright 2015-${DATE} Alia Technologies, S.L. - http://www.alialabs.com
# @author: Alia Technologies
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).
{
  'name': 'Alia Reports - Agreement',
  'summary': 'Layout for Alia Reports: Agreement',
  'version': '14.0.1.1.0',
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
       Alia Technologies reports add-on: Agreement Layout.
   ''',
  'depends': [
    # Project Dependencies
    'alia_reports_base',

    # Base Dependencies
    'agreement_legal',
  ],
  'data': [
    # Security
    # Data
    'report/report.xml',
    # Views
    'views/agreement_views.xml',
    'report/main.xml',
    'report/blocks/basic-info.xml',
    'report/blocks/parties-info.xml',
    'report/blocks/parties-info/company-info.xml',
    'report/blocks/parties-info/partner-info.xml',
    'report/blocks/recitals-info.xml',
    'report/blocks/recitals-info/recitals-list.xml',
    'report/blocks/recitals-info/sections-list.xml',
    'report/blocks/recitals-info/sections-list/clauses-list.xml',
    'report/blocks/special-terms.xml',
    'report/blocks/signatures.xml',
    'report/blocks/appendix.xml',
  ],
  "assets": {
    "web.report_assets_common": [
      # SASS variables Assets
      "alia_reports_agreement/static/src/sass/variables.scss",
      # SASS files Assets
      "alia_reports_agreement/static/src/sass/directives.scss",
      "alia_reports_agreement/static/src/sass/main.scss",
      "alia_reports_agreement/static/src/sass/blocks/basic-info.scss",
      "alia_reports_agreement/static/src/sass/blocks/parties-info.scss",
      "alia_reports_agreement/static/src/sass/blocks/recitals-info.scss",
      "alia_reports_agreement/static/src/sass/blocks/recitals-info/clauses-list.scss",
      "alia_reports_agreement/static/src/sass/blocks/signatures.scss",
    ],
  },
  'demo': [],
  'test': [],
  'installable': True,
  'auto_install': False,
  'application': False,
  'sequence': 121,
}
