# -*- coding: utf-8 -*-
from odoo import models, fields, api


class visit(models.Model):
    _name = 'custom_crm.visit' # Model name
    _description = 'Visit' # Model description

    name = fields.Char(string='Descripción') # Field name suele pintarse en el formulario en el encabezado de la vista
    customer = fields.Many2one(string='Cliente', comodel_name='res.partner') # Field customer
    date = fields.Datetime(string='Fecha')
    type = fields.Selection([('P', 'Presencial'), ('W', 'WhatsApp'), ('T', 'Telefónico')], string='Tipo', required=True)
    done = fields.Boolean(string='Realizada', readonly=True)

    def button_toggle_state(self):
        self.done = not self.done


# class custom_crm(models.Model):
#     _name = 'custom_crm.custom_crm'
#     _description = 'custom_crm.custom_crm'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
