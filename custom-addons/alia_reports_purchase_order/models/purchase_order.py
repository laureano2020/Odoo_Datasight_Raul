from odoo import api, fields, models


class PurchaseOrder(models.Model):
  _inherit = 'purchase.order'

  def print_purchase_order_report(self):
        return self.env.ref('alia_reports_purchase_order.purchase_order').report_action(self)

