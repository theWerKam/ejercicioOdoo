from odoo import models, fields

class Acciones_formativas(models.Model):
    _inherit = 'acciones_formativas'

    formacion_continua_id = fields.One2many('formacion.continua', 'acciones_formativas_id', string='Accion formativa a evaluar')