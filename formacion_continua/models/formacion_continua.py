from odoo import models, fields, api
from odoo.exceptions import ValidationError

class Formacion_continua(models.Model):
    _name = 'formacion.continua'
    _description='Formacion continua'

    name = fields.Char(string='Nombre', default='Sin nombre')
    trabajador_id = fields.Many2one('hr.employee', string='Nombre del trabajador', domain="[('id', 'in', trabajador_con_acciones_id)]",required=True)
    trabajador_con_acciones_id = fields.Many2many('hr.employee', string='Alumnos con acciones formativas', compute='_compute_alumnos_con_acciones', store=False)
    acciones_formativas_id = fields.Many2one('acciones_formativas',string='Nombre de la accion formativa',required=True)
    notas = fields.Integer(string='Nota de la accion formativa', required=True)

    @api.depends('acciones_formativas_id')
    def _compute_alumnos_con_acciones(self):
        for record in self:
            if record.acciones_formativas_id:
                alumnos = record.acciones_formativas_id.mapped('participantes_id').ids
                record.trabajador_con_acciones_id = [(6, 0, alumnos)]
            else:
                record.trabajador_con_acciones_id = [(6, 0, [])]
    
    @api.constrains('trabajador_id', 'acciones_formativas_id', 'notas')
    def errores_validacion(self):
        for record in self:
            existe_formacion = self.search([('trabajador_id','=',record.trabajador_id.id ), ('acciones_formativas_id','=', record.acciones_formativas_id.id)])
            if len(existe_formacion)>1:
                raise ValidationError("El trabajador ya tiene esta acción formativa puntuada.")
            elif record.notas > 10 or record.notas<0:
                raise ValidationError('La nota ha de ser entre 0 a 10')