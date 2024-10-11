from odoo import models, fields


class PurchaseOrder(models.Model):
    _inherit = "purchase.order"

    purchase_category_ids = fields.Many2many(comodel_name="purchase.category", string="Purchase Category")
