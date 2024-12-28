from odoo import models, fields

class Empleados(models.Model):
    _inherit = 'hr.employee'

    acciones_formativas_id = fields.Many2many('acciones_formativas', string='Acciones Formativas')