from odoo import fields, models, api


class ContractIRPF(models.Model):
    _inherit = 'hr.contract'

    categoria_convenio = fields.Many2one('hr.categoria.convenio', string='Categoría de convenio')
    grupo_cotizacion = fields.Many2one('hr.grupo.cotizacion', string='Grupo de cotización')
    wage_plus = fields.Float(string='Plus de salario', track_visibility='onchange')

