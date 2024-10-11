# -*- coding: utf-8 -*-

import base64
from odoo import models, fields
from datetime import datetime
from num2words import num2words


class IrActionsReport(models.Model):
    _inherit = 'ir.actions.report'

    create_log = fields.Boolean("Create log when report is printed", default=True)
    log_attachment = fields.Boolean()

    def _render_qweb_pdf(self, report_ref, res_ids=None, data=None):

        report_template_name = self.env['ir.actions.report'].search([('report_name', '=', str(report_ref))])

        originated_model_name = report_template_name.model
        originated_record_id = res_ids

        log = self.env['report.log']

        if report_template_name.create_log:
            log_values = {
                'report_id': report_template_name.id,
                'res_model': report_template_name.model,
                'user_id': report_template_name.env.user.id,
                'date': fields.Datetime.now(),
                'state': 'fail',  # default is failed, updated when report is generated
            }

            if res_ids:
                log_values['res_ids'] = f'[{res_ids}]' if isinstance(res_ids, int) else str(res_ids)
            log = self.env['report.log'].sudo().create(log_values)
            self.env.cr.commit()

        try:
            pdf_content, res = super(IrActionsReport, self)._render_qweb_pdf(report_ref, res_ids=res_ids, data=data)
            if report_template_name.create_log:
                log_update_values = {
                    'state': 'success'
                }
                # Add report content if log_attachment is set
                if report_template_name.log_attachment:
                    log_update_values.update({'report_content': base64.b64encode(pdf_content), 'report_file_name': f'{self.name}.pdf'})
                log.write(log_update_values)

                try:
                    for record_id in originated_record_id:
                        total_log = self.env['report.log'].search([
                            ('res_model', '=', str(originated_model_name)),
                            ('res_ids', 'like', str(record_id)),
                            ('report_id', '=', report_template_name.id),
                        ])

                        report_print_count = num2words(len(total_log or 1), lang='id')

                        model_record = self.env[str(originated_model_name)].search([('id', '=', record_id)])
                        now = datetime.strftime(fields.Datetime.context_timestamp(self, datetime.now()), "%d-%m-%Y %H:%M:%S")
                        message_body = str(report_template_name.env.user.name) + ' telah mencetak ' + str(report_template_name.name) + ' pada tanggal ' + str(now) + '.\n Report ini telah dicetak sebanyak ' + str(report_print_count) + ' kali total akumulasi'

                        model_record.message_post(body=message_body, message_type='notification')
                except:
                    pass

        except Exception as e:
            if log:
                log.write({'fail_message': e})
                self.env.cr.commit()
            raise e

        return pdf_content, res



        # yang ini sudah oke jangan diapa2in
        # pdf_content, res = super(IrActionsReport, self)._render_qweb_pdf(report_ref, res_ids=res_ids, data=data)
        # report_template_name = self.env['ir.actions.report'].search([('report_name', '=', str(report_ref))])
        #
        # log = self.env['report.log']
        # if report_template_name.create_log == True:
        #     try:
        #         log_values = {
        #                 'report_id': report_template_name.id,
        #                 'res_model': report_template_name.model,
        #                 'user_id': report_template_name.env.user.id,
        #                 'date': fields.Datetime.now(),
        #                 'state': 'success',  # default is failed, updated when report is generated
        #         }
        #
        #         if res_ids:
        #             log_values['res_ids'] = f'[{res_ids}]' if isinstance(res_ids, int) else str(res_ids)
        #         log = self.env['report.log'].sudo().create(log_values)
        #         self.env.cr.commit()
        #
        #         if report_template_name.log_attachment:
        #             log_update_values = {}
        #             log_update_values.update(
        #                 {'report_content': base64.b64encode(pdf_content), 'report_file_name': f'{self.name}.pdf'})
        #             log.write(log_update_values)
        #
        #     except Exception as e:
        #         if log:
        #             log.write({'fail_message': e})
        #             self.env.cr.commit()
        #         raise e
        # return res


        # Yang ini codingan lama
        # log = self.env['report.log']
        # Create & commit log record
        # if self.create_log:
        #     log_values = {
        #         'report_id': self.id,
        #         'res_model': self.model,
        #         'user_id': self.env.user.id,
        #         'date': fields.Datetime.now(),
        #         'state': 'fail',  # default is failed, updated when report is generated
        #     }
        #     if res_ids:
        #         log_values['res_ids'] = f'[{res_ids}]' if isinstance(res_ids, int) else str(res_ids)
        #     log = self.env['report.log'].sudo().create(log_values)
        #     self.env.cr.commit()
        #
        # try:
        #     pdf_content, type = super(IrActionsReport, self)._render_qweb_pdf(report_ref, res_ids=res_ids, data=data)
        #
        #     if self.create_log:
        #         log_update_values = {
        #             'state': 'success'
        #         }
        #         # Add report content if log_attachment is set
        #         if self.log_attachment:
        #             log_update_values.update({'report_content': base64.b64encode(pdf_content), 'report_file_name': f'{self.name}.pdf'})
        #         log.write(log_update_values)
        # except Exception as e:
        #     if log:
        #         log.write({'fail_message': e})
        #         self.env.cr.commit()
        #     raise e
        #
        # return pdf_content, type

    def action_view_report_logs(self):
        return {
            'type': 'ir.actions.act_window',
            'name': "Logs",
            'res_model': 'report.log',
            'view_type': 'list',
            'view_mode': 'list',
            'views': [[False, 'list']],
            'domain': [('report_id', '=', self.id)],
        }
