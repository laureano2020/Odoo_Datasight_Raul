from odoo import fields, models, api


class HrCategoriaConvenio(models.Model):
    _name = 'hr.categoria.convenio'

    name = fields.Char(string="Categoría de convenio")