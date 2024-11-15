from odoo import fields, models, api


class ContractIRPF(models.Model):
    _inherit = 'hr.contract'

    irpf = fields.Float(string="IRPF",track_visibility='onchange')
