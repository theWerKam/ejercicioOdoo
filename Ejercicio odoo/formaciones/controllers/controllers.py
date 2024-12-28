# -*- coding: utf-8 -*-
# from odoo import http


# class Formaciones(http.Controller):
#     @http.route('/formaciones/formaciones', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/formaciones/formaciones/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('formaciones.listing', {
#             'root': '/formaciones/formaciones',
#             'objects': http.request.env['formaciones.formaciones'].search([]),
#         })

#     @http.route('/formaciones/formaciones/objects/<model("formaciones.formaciones"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('formaciones.object', {
#             'object': obj
#         })

