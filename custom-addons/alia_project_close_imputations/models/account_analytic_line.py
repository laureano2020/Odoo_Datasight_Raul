# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _
from odoo.exceptions import ValidationError

class AccountAnalyticLine(models.Model):
    _inherit = 'account.analytic.line'

    @api.model_create_multi
    def create(self, vals_list):
        # if 'account_id' in vals_list.keys():
        #     project = self.env['project.project'].search([('analytic_account_id','=',vals_list['account_id'])],limit=1)
        #     if project.stage_id.close_imputatations:
        #         raise ValidationError(
        #             _("No está permitido guardar esta línea analítica porque el proyecto está en una etapa que cierra imputaciones."))

        return super(AccountAnalyticLine, self).create(vals_list)

