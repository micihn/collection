from odoo import models, fields


class PurchaseCategory(models.Model):
    _name = 'purchase.category'

    name = fields.Char(string="Category")
    color = fields.Integer(string="Color")
