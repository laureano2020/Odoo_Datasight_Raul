from odoo import api, fields, models


class StockPicking(models.Model):

  _inherit = 'stock.picking'

  def print_stock_picking_report(self):
        return self.env.ref('alia_reports_stock.delivery_slip').report_action(self)

