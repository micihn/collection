from odoo import models, fields, api, _

class SaleValidationApproval(models.Model):
    _inherit = 'sale.order'

    state = fields.Selection(selection_add=[('approve', 'Approve')])

    def approve(self):
        return super(SaleValidationApproval, self).action_confirm()

    def action_confirm(self):
        is_approve = self.env['ir.config_parameter'].sudo().search([('key', '=', 'is_double_check')])
        validaiton_amount = self.env['ir.config_parameter'].sudo().search([('key', '=', 'double_val_amount')])
        approve = is_approve.value
        val_amount = validaiton_amount.value
        if approve:
            if self.amount_total >= int(val_amount):
                # print("val_amount-------------------",val_amount)
                self.state = 'approve'
                return None
        return super(SaleValidationApproval, self).action_confirm()

class SaleValidationApprovalSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    is_double_check = fields.Boolean('SO Approval', default=False)
    double_val_amount = fields.Char('Double Validation Amount')

    @api.model
    def get_values(self):
        res = super(SaleValidationApprovalSettings, self).get_values()
        search = self.env['ir.config_parameter']

        res['is_double_check'] = search.sudo().get_param('is_double_check')
        res['double_val_amount'] = search.sudo().get_param('double_val_amount')
        return res

    @api.model
    def set_values(self):
        self.env['ir.config_parameter'].sudo().set_param('is_double_check', self.is_double_check)
        self.env['ir.config_parameter'].sudo().set_param('double_val_amount', self.double_val_amount)
        res = super(SaleValidationApprovalSettings, self).set_values()
        return res
