# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class formacion_continua(models.Model):
#     _name = 'formacion_continua.formacion_continua'
#     _description = 'formacion_continua.formacion_continua'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

