from odoo import fields, models, api


class SaleOrder (models.Model):
    _inherit = 'sale.order'

    state = fields.Selection(selection_add=[('reject', 'Rejected')])
    reject_reason_ids = fields.One2many('alia.reject.reason', 'sale_order_id', string="Reject Reasons")

    def action_reject(self):
        return self.write({
            'state': 'reject'
        })

    def action_unreject(self):
        return self.write({
            'state': 'draft'
        })