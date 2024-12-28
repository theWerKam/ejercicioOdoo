from odoo import models, fields, api

class Formacion_continua(models.Model):
    _name = 'formacion.continua'
    _description='Formacion continua'

    name = fields.Char(string='Nombre', default='Sin nombre')
    trabajador_id = fields.Many2one('hr.employee', string='Nombre del trabajador', required=True)
    acciones_formativas_id = fields.Many2one('acciones_formativas',string='Nombre de la accion formativa', required=True)
    notas = fields.Integer(string='Nota de la accion formativa', required=True)

