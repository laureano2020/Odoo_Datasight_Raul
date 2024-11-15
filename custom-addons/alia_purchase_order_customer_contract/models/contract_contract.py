# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

from odoo import models, fields, api

class ContractContract(models.Model):
    _inherit = "contract.contract"

    purchase_order_ids = fields.One2many(comodel_name='purchase.order', inverse_name='customer_contract_id',
                                         string="Purchase orders")