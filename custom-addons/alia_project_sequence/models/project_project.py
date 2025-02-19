# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _

class ProjectProject(models.Model):
    _inherit = 'project.project'
    _rec_name = 'name'

    sequence_name = fields.Char(string="Código",readonly=True,copy=False)

    @api.model
    def create(self,vals):
        if vals.get('sequence_name', _('New')) == _('New'):
            vals['sequence_name'] = self.env['ir.sequence'].next_by_code('project.project') or _('New')
        res = super(ProjectProject, self).create(vals)
        return res

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
