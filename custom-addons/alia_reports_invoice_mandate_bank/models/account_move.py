# Copyright 2015-14/1/22 Alia Technologies, S.L. - http://www.alialabs.com 
# @author:alia
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

from odoo import fields, models, api, _


class AccountMove(models.Model):
    _inherit = 'account.move'

    def get_mandate_bank_info(self):
        for move in self:
            mandate_data = ''
            if move.mandate_id.partner_bank_id:
                partner_bank_id = move.mandate_id.partner_bank_id
                acc_number = partner_bank_id.acc_number
                digits = '....' + acc_number[-5:]
                bank_name = partner_bank_id.bank_id and partner_bank_id.bank_id.name or ''
                mandate_data = bank_name + '  ' + digits
        return mandate_data
