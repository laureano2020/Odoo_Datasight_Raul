# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

from odoo import models, fields, api

class SaleOrderAnalyticDistribution(models.Model):
    _name = 'sale.order'
    _inherit = ['sale.order', 'analytic.mixin']


class SaleOrderLineAnalyticDistribution(models.Model):
    _inherit = 'sale.order.line'

    @api.depends('product_id', 'order_id.partner_id', 'order_id.analytic_distribution')
    def _compute_analytic_distribution(self):
        res = super(SaleOrderLineAnalyticDistribution, self)._compute_analytic_distribution()
        for line in self:
            distribution = False
            if not line.display_type:
                if line.order_id.analytic_distribution:
                    distribution = line.order_id.analytic_distribution
                line.analytic_distribution = distribution or line.analytic_distribution
        return res



