# -*- coding: utf-8 -*-
# from odoo import http


# class AccionesFormativas(http.Controller):
#     @http.route('/acciones_formativas/acciones_formativas', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/acciones_formativas/acciones_formativas/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('acciones_formativas.listing', {
#             'root': '/acciones_formativas/acciones_formativas',
#             'objects': http.request.env['acciones_formativas.acciones_formativas'].search([]),
#         })

#     @http.route('/acciones_formativas/acciones_formativas/objects/<model("acciones_formativas.acciones_formativas"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('acciones_formativas.object', {
#             'object': obj
#         })

