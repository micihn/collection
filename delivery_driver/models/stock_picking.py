from odoo import fields, api, models

class DeliveryDriver(models.Model):
    _inherit = 'stock.picking'

    kendaraan = fields.Many2one('fleet.vehicle', string="Kendaraan")
    sopir = fields.Many2one('hr.employee', string="Sopir")
    kenek = fields.Many2one('hr.employee', string="Kenek")
