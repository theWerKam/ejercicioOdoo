from odoo import models, fields

class Empleados(models.Model):
    _inherit = 'hr.employee'

    acciones_formativas_ids = fields.Many2many(
        'acciones_formativas', 
        'employee_acciones_formativas_rel',  
        'employee_id',  
        'acciones_formativas_id',  
        string='Acciones Formativas'
    )