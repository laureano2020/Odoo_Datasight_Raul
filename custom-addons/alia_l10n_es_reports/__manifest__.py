# Copyright 2015-${DATE} Alia Technologies, S.L. - http://www.alialabs.com
# @author: Alia
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).
{
  'name': 'Alia Reports Inter. [Spain]',
  'summary': 'Theme layout overrides for Alia Reports (Spanish internationalization)',
  'version': '16.0.0',
  'author': 'Alia Technologies',
  'website': 'http://www.alialabs.com',
  'category': 'ALIA - Tools',
  'license': 'AGPL-3',
  'contributors': [
    'Brais Saco <braissaco@alialabs.com>',
  ],
  'maintainers': [
    'Brais Saco <braissaco@alialabs.com>'
  ],
  'description': '''
       Alia Technologies reports addon. Overrides default external_layout. Defines report's common blocks (Spanish internationalization).
   ''',
  'depends': [
    # Project Dependencies
    'alia_reports_invoice',
    # Base Dependencies
    # 'l10n_es_account_invoice_sequence',
    'l10n_es_toponyms',
    'l10n_es_partner_mercantil',
  ],
  'demo': [],
  'data': [
    # Security
    # Data
    # Views
    'report/external-layout/footer.xml',
  ],
  "assets": {
    "web.report_assets_common": [
      # SASS variables Assets
      "alia_l10n_es_reports/static/src/sass/variables.scss",
      # SASS files Assets
      "alia_l10n_es_reports/static/src/sass/directives.scss",
      "alia_l10n_es_reports/static/src/sass/main.scss",
      "alia_l10n_es_reports/static/src/sass/external-layout/footer.scss",
    ],
  },
  'demo': [],
  'test': [],
  'installable': True,
  'auto_install': False,
  'application': False,
  'sequence': 123,
}
