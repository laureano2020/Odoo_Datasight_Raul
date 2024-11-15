from odoo import api, fields, models


class AccountMove(models.Model):
  _inherit = 'account.move'

  def _get_payments_vals(self):
    payment_ids = self.env['account.payment'].search([('ref', '=', self.payment_reference)])

    if len(payment_ids) == 0:
      return []

    payment_vals = []
    for payment in payment_ids:
      payment_vals.append(
        {
          'amount': payment.amount,
          'date': payment.date
        }
      )

    return payment_vals

  def print_invoice_report(self):
    return self.env.ref('alia_reports_invoice.invoice_order').report_action(self)
