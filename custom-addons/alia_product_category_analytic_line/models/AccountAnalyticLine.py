# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _

class AccountAnalyticLine(models.Model):
    _inherit = 'account.analytic.line'

    product_category_id = fields.Many2one('product.category',string="Categoria de Producto",related='product_id.categ_id',store=True)

