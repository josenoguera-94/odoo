# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request, Response
import json

class VisitController(http.Controller):
    @http.route('/api/visits', auth='public', method=['GET'], csrf=False)
    # @http.route('/api/visits', type='http', auth='user', website=True) averiguar metodos de autenticacion con token
    def get_visits(self, **kw):

        try:
            # visits = http.request.env['custom_crm.visit'].sudo().search([]) # sudo() es para que no se requiera autenticacion
            # visits = visits.read()
            visits = http.request.env['custom_crm.visit'].sudo().search_read([], ['id', 'name', 'customer', 'done']) # hay que serializar datetime
            response = json.dumps(visits, ensure_ascii=False).encode('utf-8') # ensure_ascii=False es para que no se codifique en ascii, sino en utf8
            return Response(response, content_type='application/json; charset=utf-8', status=200) # content_type es para que sepa que es un json, sino lo toma como texto plano
        except Exception as e:
            return Response(json.dumps({'error': str(e)}), content_type='application/json;charset=utf-8', status=505)
        # return http.request.render('custom_crm.visit', {
        #     'visit': json.dumps(kw)
        # })


# class CustomCrm(http.Controller):
#     @http.route('/custom_crm/custom_crm/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/custom_crm/custom_crm/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('custom_crm.listing', {
#             'root': '/custom_crm/custom_crm',
#             'objects': http.request.env['custom_crm.custom_crm'].search([]),
#         })

#     @http.route('/custom_crm/custom_crm/objects/<model("custom_crm.custom_crm"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('custom_crm.object', {
#             'object': obj
#         })
