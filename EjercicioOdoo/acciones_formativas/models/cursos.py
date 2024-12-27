from odoo import models, fields

class Partner(models.Model):
    _inherit = 'formaciones.cursos'

    acciones_formativas_id = fields.One2many('acciones_formativas', 'curso_id', string='Acciones formativas')

    
