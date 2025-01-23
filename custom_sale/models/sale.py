from odoo import models, fields
 
class CustomSalesModel(models.Model):
    _inherit = "sale.order"

    custom_field=fields.Char(string="Custom Field")