from odoo import fields, models, api


class HrExpense (models.Model):
    _inherit = 'hr.expense'

    partner_id = fields.Many2one('res.partner',string="Proveedor")