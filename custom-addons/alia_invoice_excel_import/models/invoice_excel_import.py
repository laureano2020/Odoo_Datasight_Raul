# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _

from xlrd import open_workbook
import base64

from datetime import datetime, timedelta


class UploadFile(models.TransientModel):
    _name = 'invoice.excel.import'

    uploaded_file = fields.Binary(string='Subir archivo', required=True)
    file_name = fields.Char(string='Nombre del archivo', )
    journal_id = fields.Many2one('account.journal',string="Journal")
    invoice_type = fields.Selection([('out_invoice','Facturas de cliente'),('in_invoice','Facturas de proveedor')], string='Tipo de factura', required=True)

    def import_file(self):
        file_data = base64.b64decode(self.uploaded_file)
        workbook = open_workbook(file_contents=file_data)
        sheet = workbook.sheet_by_index(0)
        move_name_prev = str(0)

        analytic_distribution_vector = []

        for row_index in range(1, sheet.nrows):
            row = sheet.row_values(row_index)
            if str(row[0]) != move_name_prev or row_index == 1:
                row_date = row[1]
                if isinstance(row_date, float):
                    converted_date = datetime(1899,12,30) + timedelta(days=int(row[1]))
                    invoice_date = converted_date.strftime('%Y-%m-%d')
                else:
                    invoice_date = datetime.strptime(row[1],'%m/%d/%Y')

                account_move_data = {
                    'journal_id': self.journal_id.id,
                    'partner_id': int(row[2]),
                    # 'currency_id': 1, # euro
                    'state': 'draft',
                    'move_type': self.invoice_type,
                    # 'auto_post': 'no',
                    'invoice_date': invoice_date,
                    'ref': str(row[0])

                }
                self.env['account.move'].create(account_move_data)
                move_name_prev = str(row[0])

            max_account_move_id = self.env['account.move'].search([], order='id desc', limit=1).id
            account_move_id = int(max_account_move_id)


            if row_index > 1:
                if account_move_id != account_move_id_prev:
                    analytic_lines_equal = all(analytic_distribution_line == analytic_distribution_vector[0] for analytic_distribution_line in analytic_distribution_vector)
                    analytic_distribution_vector = []

                    if analytic_lines_equal:
                        self.env['account.move'].browse(account_move_id_prev).write({'analytic_distribution':analytic_distribution})


            analytic_distribution = {str(int(row[6])): 100, str(int(row[7])): 100, str(int(row[8])): 100}
            analytic_distribution_vector.append(analytic_distribution)

            account_move_line_data = {
                'move_id': account_move_id,
                'price_unit': row[3],
                'tax_ids': [int(row[4])],
                'product_id': int(row[5]),
                'analytic_distribution': analytic_distribution,
                'quantity': 1,
            }
            self.env['account.move.line'].create(account_move_line_data)

            analytic_distribution_prev = analytic_distribution
            account_move_id_prev = account_move_id
