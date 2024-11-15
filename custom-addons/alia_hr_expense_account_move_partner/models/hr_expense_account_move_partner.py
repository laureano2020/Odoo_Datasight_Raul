from odoo import fields, models, api

# primero creamos el partner_id en el informe de gastos -> que sea igual al partner_id del primer gasto con un partner_id asociado
# luego sobreescribimos el método action_sheet_move_create para igualar el partner_id del asiento contable al del informe de gastos

class HrExpenseSheet (models.Model):
    _inherit = 'hr.expense.sheet'

    expense_ids = fields.One2many('hr.expense', 'sheet_id', string="Expenses")
    partner_id = fields.Many2one('res.partner', string='Proveedor', compute='_compute_partner_id', store=True)

    @api.depends('expense_ids.partner_id')
    def _compute_partner_id(self):
        for sheet in self:
            partner = False
            for expense in sheet.expense_ids:
                if expense.partner_id:
                    partner = expense.partner_id
                    break
            sheet.partner_id = partner

    # sobreescribimos el método 'action_sheet_move_create' (crea un asiento contable desde un informe de gastos) para que, además de ejecutarse el método original, se ejecute una función que iguale el partner_id del asiento contable al partner_id del informe de gastos
    def action_sheet_move_create(self):
        result = super(HrExpenseSheet, self).action_sheet_move_create() # método 'action_sheet_move_create' original
        self.update_partner_id_on_move()
        return result

    def update_partner_id_on_move(self):
        move = self.account_move_id
        # queremos que los partner_id se igualen incluso si el partner_id del informe de gastos está vacío (para que no ponga al empleado compo proveedor del asiento contable)
        move.partner_id = self.partner_id.id

