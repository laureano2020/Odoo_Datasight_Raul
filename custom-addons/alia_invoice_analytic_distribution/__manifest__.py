# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.
{
    'name': 'Alia Invoice Analytic Distribution',
    'version': '16.0.1.0.1',
    'category':'Datasight Project Addons',
    'license':'OPL-1',
    'summary': 'Adds analytic distribution field to invoices, matches invoice and invoice lines analytic distribution.',
    'description':"""This module adds an analytic distribution field to invoices. Also, defines two methods so that
    the analytic distribution field of invoice lines matches the analytic distribution field of the invoice so the user
    doesn't have to manually introduce the same analytic distribution several times (one time for each invoice line).""",
    'author': 'Alia Technologies S.L.',
    'depends':['account'],
    'data':[
        'views/invoice_analytic_distribution_view.xml',
        ],
    'installable': True,
    'auto_install': False,
}

