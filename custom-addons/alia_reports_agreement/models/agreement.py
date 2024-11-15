from odoo import api, fields, models


class Agreement(models.Model):
  _inherit = 'agreement'

  def print_agreement_report(self):
        return self.env.ref('alia_reports_agreement.agreement').report_action(self)

