from odoo import models, fields

class Partner(models.Model):
    _inherit = 'res.partner'

    acciones_formativas_formador_id = fields.One2many('acciones_formativas', 'formador_id', string='Formador')