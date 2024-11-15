# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _

class ProjectProject(models.Model):
    _inherit = 'project.project'

    project_tasks_ids = fields.One2many('project.task', 'project_id', string='Project tasks', domain=[('parent_id','=',False)]) # filtramos para quedarnos solo con las tareas y no las subtareas
    effective_hours = fields.Float(string='Horas dedicadas', compute='_compute_effective_hours')
    progress = fields.Float(string='Progreso', compute='_compute_progress')

    @api.depends('project_tasks_ids.effective_hours')
    def _compute_effective_hours(self):
        for project in self:
            hours = 0
            for task in project.project_tasks_ids:
                hours += task.effective_hours
            project.effective_hours = hours

    @api.depends('allocated_hours')
    def _compute_progress(self):
        for project in self:
            if project.allocated_hours == 0 or project.effective_hours >= project.allocated_hours:
                progress = 100
            else:
                progress = project.effective_hours / project.allocated_hours * 100
            project.progress = progress

class ProjectTask(models.Model):
    _inherit = 'project.task'

    subtask_count = fields.Integer(string='Número de subtareas', compute='_compute_subtask_count', store=True)

    def _compute_subtask_count(self):
        for task in self:
            task.subtask_count = len(task.env['project.task'].search([('parent_id','=',task.id)]))

