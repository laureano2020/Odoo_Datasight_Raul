# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

from odoo import models, fields, api

class PurchaseOrder(models.Model):
    _inherit = "purchase.order"

    customer_contract_id = fields.Many2one(comodel_name='contract.contract', string="Customer contract")