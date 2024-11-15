# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

from odoo import models, fields, api

class AccountMove(models.Model):
    _inherit = "account.move"

    move_analytic_distribution = fields.Json("Analytic Distribution")
    analytic_precision = fields.Integer(
        store=False,
        default=lambda self: self.env['decimal.precision'].precision_get("Percentage Analytic"),
    )

    @api.onchange('move_analytic_distribution')
    def _match_analytic_distribution_move(self):
        for line in self.invoice_line_ids:
            line.analytic_distribution = self.move_analytic_distribution


class AccountMoveLine(models.Model):
    _inherit = 'account.move.line'

    @api.onchange('product_id', 'move_id', 'move_id.move_analytic_distribution')
    def _match_analytic_distribution_line(self):
        for line in self:
            line.analytic_distribution = line.move_id.move_analytic_distribution



