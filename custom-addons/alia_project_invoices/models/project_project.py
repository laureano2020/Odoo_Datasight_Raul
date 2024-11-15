# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _

class ProjectProject(models.Model):
    _inherit = 'project.project'
    _rec_name = 'name'

    project_invoice_ids = fields.Many2many('account.move',string="Project invoices",compute='_compute_many2many_invoices')
    project_supplier_invoice_ids = fields.Many2many('account.move',string="Project invoices",compute='_compute_many2many_invoices')
    project_total_invoiced = fields.Float(string='Total Facturado',compute='_compute_many2many_invoices')
    project_total_suppliers_invoiced = fields.Float(string='Total Facturado Proveedores', compute='_compute_many2many_invoices')

    def _compute_many2many_invoices(self):
        for project in self:
            if not project.analytic_account_id:
                project.project_invoice_ids = [(5, 0, 0)]
                project.project_total_invoiced = 0.0
                continue

            project_amls = self.env['account.move.line'].search([
                ('analytic_account_ids', 'in', project.analytic_account_id.id),
                ('move_id.move_type', 'in', ['out_invoice', 'out_refund'])
            ])

            project_supplier_amls = self.env['account.move.line'].search([
                ('analytic_account_ids', 'in', project.analytic_account_id.id),
                ('move_id.move_type', 'in', ['in_invoice', 'in_refund'])
            ])

            project_invoices = project_amls.mapped('move_id')
            project_supplier_invoices = project_supplier_amls.mapped('move_id')
            project.project_invoice_ids = [(6, 0, project_invoices.ids)]
            project.project_supplier_invoice_ids = [(6, 0, project_supplier_invoices.ids)]
            project.project_total_invoiced = sum(invoice.amount_untaxed_signed for invoice in project_invoices)
            project.project_total_suppliers_invoiced = sum(invoice.amount_untaxed_signed for invoice in project_supplier_invoices)

