# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

from odoo import models, fields, api

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    def print_sale_order_report(self):
        return self.env.ref('alia_reports_sale_order.sale_order').report_action(self)

    def print_sale_order_proforma_report(self):
        return self.env.ref('alia_reports_sale_order.sale_order_proforma_pdf').report_action(self)

    print_as_quotation = fields.Boolean(string="Imprimir como presupuesto",default=False)
    print_without_units_and_price_unit = fields.Boolean(string="Imprimir sólo totales",default=False)





