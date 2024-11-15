# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _

class ProjectProjectStage(models.Model):
    _inherit = 'project.project.stage'

    close_imputatations = fields.Boolean(string="Cerrar imputaciones")

