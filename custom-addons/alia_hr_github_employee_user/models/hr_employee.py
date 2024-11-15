from odoo import fields, models, api


class HrEmployee(models.Model):
    _inherit = 'hr.employee'

    github_user = fields.Char(string="Github User")


class HrEmployeePublic(models.Model):
    _inherit = 'hr.employee.public'

    github_user = fields.Char(string="Github User")