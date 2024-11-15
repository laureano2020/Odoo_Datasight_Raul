# Copyright 2015-${DATE} Alia Technologies, S.L. - http://www.alialabs.com
# @author: Alia Technologies
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

{
  'name': 'Alia Reports Invoice Envelope',
  'summary': 'Changes client info so it shows it correctly inside an envelope.',
  'version': '14.0.1.1.0',
  'author': 'Alia Technologies',
  'website': 'http://www.alialabs.com',
  'category': 'ALIA - Tools',
  'license': 'AGPL-3',
  'contributors': [
    'Brais Saco <braissaco@alialabs.com>',
  ],
  'maintainers': [
    'Brais Saco <braissaco@alialabs.com>'
    'Alejandro Leonard <alejandroleonard@alialabs.com>'
  ],
  'description': '''
       Alia Technologies reports addon. Overrides default external_layout. Defines report's common blocks so it shows the client logo correctly inside an envelope.
   ''',
  'depends': [
    # Project Dependencies
    'alia_reports_invoice',
    # Base Dependencies
  ],
  'demo': [],
  'data': [
    # Security
    # Data
    # Views
    'report/blocks/basic-info/client-info.xml',
    'report/basic-info.xml',
  ],
  'qweb': [],
  'demo': [],
  'test': [],
  'installable': True,
  'auto_install': False,
  'application': False,
  'sequence': 122,
}
