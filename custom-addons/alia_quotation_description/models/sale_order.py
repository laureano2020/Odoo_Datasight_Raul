from odoo import fields, models, api


class SaleOrder (models.Model):
    _inherit = 'sale.order'

    description = fields.Html(string="Descripción")