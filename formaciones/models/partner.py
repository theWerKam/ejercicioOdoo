from odoo import models, fields, api

class Partner(models.Model):
    _inherit = 'res.partner'

    formador = fields.Boolean(string='Formador', default=False)
    especialidad_id = fields.Many2many('formaciones.especialidad', string='Especialidad')
    mostrar_campos = fields.Boolean(compute='_compute_mostrar_campos', string='Mostrar campos del formador', store=True)
    
    @api.depends('commercial_partner_id')
    def _compute_mostrar_campos(self):
        for record in self:
            record.mostrar_campos = record.commercial_partner_id.id == 1
    
    