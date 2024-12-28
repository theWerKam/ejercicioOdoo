from odoo import models, fields

class Employee(models.Model):
    _inherit = 'hr.employee'

    formacion_continua_id = fields.One2many('formacion.continua','trabajador_id', string='Trabajador')