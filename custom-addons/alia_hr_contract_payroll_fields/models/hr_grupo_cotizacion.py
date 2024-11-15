from odoo import fields, models, api


class HrGrupoCotizacion(models.Model):
    _name = 'hr.grupo.cotizacion'

    name = fields.Char(string="Grupo de cotización")
