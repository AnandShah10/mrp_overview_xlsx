from odoo import models, fields, api, _


class MrpOverviewXlsx(models.Model):
    _inherit = 'mrp.bom'

    def print_bom_report_xlsx(self):
        print("herre xls.........................")
        return self.env.ref('mrp_overview_xlsx.report_bom_overview_xls').report_action(self)
