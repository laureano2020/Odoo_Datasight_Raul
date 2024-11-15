# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _

class ProjectProject(models.Model):
    _inherit = 'project.project'

    project_analytic_lines_ids = fields.Many2many('account.analytic.line',string="Project analytic lines",compute='_compute_many2many_analytic_lines')

    def _compute_many2many_analytic_lines(self):
        for project in self:
            analytic_lines = self.env['account.analytic.line'].search([('account_id','=',project.analytic_account_id.id),('employee_id','!=',False)]).ids
            project.project_analytic_lines_ids = analytic_lines
