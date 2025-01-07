# -*- coding: utf-8 -*-

from odoo import models, fields, api

class StockTrackLine(models.Model):

    _inherit = 'stock.move.line'

    nombre_stock = fields.Char(string="Nombre de stock", required=True)
    lista_stock = fields.Many2one('stock.production.lot', string="Lista de stock", index=True)

