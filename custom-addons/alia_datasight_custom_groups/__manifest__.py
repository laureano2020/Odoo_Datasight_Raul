# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.
{
    'name': 'Alia Datasight Custom Groups',
    'version': '16.0.0.1',
    'category':'Datasight Project Addons',
    'license':'OPL-1',
    'summary': 'Implements 2 new groups and gives to each group different access permissions.',
    'description':"""This module creates 2 new groups: one for internal users and another one for external users. 
    The external users can only see the res partner associated to the user himself while the internal user has 
    access to all res partners. Also, in the project form view, only the internal users will be able to see the 
    partner field (customer related to the project).""",
    'author': 'Alia Technologies S.L.',
    'depends':['project'],
    'data':[
        'security/groups.xml',
        'security/ir.model.access.csv',
        'security/rules.xml',
        'views/project_project_view.xml',
        ],
    'installable': True,
    'auto_install': False,
}

