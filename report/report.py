from odoo import models, fields, api, _


class BOMXlsReport(models.AbstractModel):
    _name = 'report.mrp_overview_xlsx.report_bom_overview'
    _inherit = 'report.report_xlsx.abstract'
    _description = "Excel Report Abstract Class"

    def generate_xlsx_report(self, workbook, data, lines):
        print('------->', lines, data)
        format1 = workbook.add_format({'bold': True, 'align': 'center'})
        format2 = workbook.add_format({'align': 'center'})

        sheet = workbook.add_worksheet('Excel Report')
        row = 0
        col = 0
        print("heloo.............")

        headers = ['Product', 'Quantity',
                   'Lead Time', 'Route',
                   'BoM Cost', 'Product Cost']

        for col, header in enumerate(headers):
            sheet.write(row, col, header, format1)
        print('hi.....')

        sheet.set_column('A:C', 30)
        sheet.set_column('D:D', 40)
        sheet.set_column('E:F', 30)

        row = 1
        for i in lines:
            lead_time = 0
            cost = 0
            sheet.write(1, 0, i.product_tmpl_id.display_name, format2)
            sheet.write(1, 1, str(i.product_qty) + ' ' + i.product_uom_id.name, format2)
            sheet.write(1, 3, 'Manufacturing :' + i.product_tmpl_id.display_name, format2)

            if not i.bom_line_ids:
                bom_line_cur = '$'

            for line in i.bom_line_ids:
                print(line)
                bom_line_cur = str(line.product_id.variant_seller_ids[0].currency_id.symbol)
                row += 1
                cost += float(line.product_tmpl_id.standard_price)
                lead_time += int(line.product_tmpl_id.variant_seller_ids[0].delay)
                sheet.write(row, 0, line.product_tmpl_id.display_name, format2)
                sheet.write(row, 1, str(line.product_qty) + ' ' + line.product_uom_id.name, format2)
                sheet.write(row, 2, str(line.product_tmpl_id.variant_seller_ids[0].delay) + ' Days', format2)
                sheet.write(row, 3, line.product_tmpl_id.route_ids[0].name + ':' +
                            line.product_tmpl_id.variant_seller_ids[0].partner_id.name, format2)
                sheet.write(row, 4, bom_line_cur + str(line.product_tmpl_id.standard_price), format2)
                sheet.write(row, 5, bom_line_cur + str(line.product_tmpl_id.standard_price), format2)

            row += 1
            sheet.write(1, 2, str(lead_time) + ' Days', format2)
            sheet.write(1, 4, bom_line_cur + str(cost), format2)
            sheet.write(1, 5, bom_line_cur + str(i.product_tmpl_id.standard_price), format2)

            sheet.write(row, 1, 'Unit Cost' + ' ' + i.product_uom_id.name, format1)
            sheet.write(row, 4, bom_line_cur + str(cost), format1)
            sheet.write(row, 5, bom_line_cur + str(i.product_tmpl_id.standard_price), format1)
