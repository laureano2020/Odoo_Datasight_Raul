# Copyright 2015-${DATE} Alia Technologies, S.L. - http://www.alialabs.com
# @author: Alia Technologies
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

{
  'name': 'Alia HR Employee Github User',
  'summary': '',
  'version': '16.0.1.1.0',
  'author': 'Alia Technologies',
  'website': 'http://www.alialabs.com',
  'category': 'Proyecto Datasight Addons',
  'license': 'AGPL-3',
  'description': '''
       Alia Technologies: IRPF in Contracts
   ''',
  'depends': [
    # Project Dependencies
    # Base Dependencies
    'hr',
  ],
  'data': [
    # Security
    # Data
    # Views
    'views/hr_employee_view.xml',
  ],
  'qweb': [],
  'demo': [],
  'test': [],
  'installable': True,
  'auto_install': False,
  'application': False,
  'sequence': 121,
}
