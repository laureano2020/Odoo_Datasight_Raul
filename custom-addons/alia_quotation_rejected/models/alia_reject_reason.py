from odoo import fields, models, api


class AliaRejectReasonType(models.Model):
    _name = 'alia.reject.reason.type'
    _description = 'Alia Reject Reason Type'

    name = fields.Char(string="Name")


class AliaRejectReason(models.Model):
    _name = 'alia.reject.reason'
    _description = 'Alia Reject Reason'

    name = fields.Char(string="Description")
    type = fields.Many2one('alia.reject.reason.type',string="Reason Type")
    sale_order_id = fields.Many2one('sale.order', string="Quotation ID")