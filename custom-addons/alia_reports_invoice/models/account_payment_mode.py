# Copyright 2015-3/5/21 Alia Technologies, S.L. - http://www.alialabs.com
# @author:alia
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

from odoo import fields, models, api, _


class AccountPaymentTerm(models.Model):
  _inherit = 'account.payment.term'

  report_label = fields.Boolean(string="Show Invoice Dues Label")
  report_invoice_dues = fields.Boolean(string="Show Invoice Dues Table", default=True)
