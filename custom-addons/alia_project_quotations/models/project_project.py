# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.
from odoo import fields, models, api

class ProjectProject(models.Model):
    _inherit = 'project.project'
    _rec_name = 'name'

    project_quotation_ids = fields.Many2many('sale.order',string="Project Quotations",compute='_compute_many2many_quotations')
    project_total_quoted = fields.Float(string='Total Presupuestado', compute='_compute_many2many_quotations')


    def _compute_many2many_quotations(self):
        for record in self:
            quotation_ids = self.env['sale.order'].search([('analytic_account_id','=',[self.analytic_account_id.id])])
            record.project_quotation_ids = [(6, 0, quotation_ids.ids)]
            record.project_total_quoted = sum(x.amount_untaxed for x in quotation_ids)