# -*- coding: utf-8 -*-
# from odoo import http


# class TercerModulo(http.Controller):
#     @http.route('/tercer_modulo/tercer_modulo/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/tercer_modulo/tercer_modulo/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('tercer_modulo.listing', {
#             'root': '/tercer_modulo/tercer_modulo',
#             'objects': http.request.env['tercer_modulo.tercer_modulo'].search([]),
#         })

#     @http.route('/tercer_modulo/tercer_modulo/objects/<model("tercer_modulo.tercer_modulo"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('tercer_modulo.object', {
#             'object': obj
#         })
