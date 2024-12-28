from odoo import models, fields, api
from odoo.exceptions import ValidationError
from datetime import date

class Acciones_formativas(models.Model):
    _name = 'acciones_formativas'
    _description = 'Acciones formativas'
    
    name = fields.Char(string='Nombre de la accion formativa', required=True)
    curso_id = fields.Many2one('formaciones.cursos', string='Curso', required=True)
    formador_id = fields.Many2one('res.partner', string='Formador', domain=[('formador', '=', True)], required=True)
    participantes_id = fields.Many2many('hr.employee', string='Participantes')
    horas_curso = fields.Integer(string='Total de horas del curso', readonly=True, compute='_compute_horas_curso')
    horas_pendientes = fields.Integer(string='Total de horas por asignar', readonly=True)
    sesiones = fields.Integer(string='Numero de sesiones', readonly=True, compute='_compute_horas_sesion')
    horas = fields.Integer(string='Numero de horas de la accion formativa')
    sesion_horas = fields.Integer(string='Horas por sesion')
    fecha_inicio = fields.Date(string='Fecha de inicio', required=True)
    
    @api.depends('horas', 'sesion_horas')
    def _compute_horas_sesion(self):
        for record in self:
            if record.horas == 0 or record.sesion_horas==0:
                record.sesiones = 0
            elif record.horas<record.sesion_horas:
                record.sesiones = 0
            else:
                record.sesiones = record.horas / record.sesion_horas

    @api.depends('curso_id', 'horas')
    def _compute_horas_curso(self):
        for record in self:
            if not record.curso_id:
                record.horas_curso = 0
                record.horas_pendientes = 0
            else:
                record.horas_curso = record.curso_id.duracion
                acciones_formativas = record.env['acciones_formativas'].search([('curso_id', '=', record.curso_id.id),('id', '!=', record.id)])
                total_horas = sum(acciones_formativas.mapped('horas'))
                diferencia = record.horas_curso - total_horas
                record.horas_pendientes = diferencia
        
    @api.constrains('horas', 'sesion_horas')
    def _validar_horas(self):
        for record in self:
            record._compute_horas_curso()
            record._compute_horas_sesion()
            
            if record.horas_pendientes == 0:
                raise ValidationError('Este curso no dispone de horas pendientes para asignar una accion formativa')
            elif record.horas > record.horas_pendientes:
                raise ValidationError('Las horas de la accion formativa no puede ser mayor a la cantidad de horas disponibles del curso')
            elif record.horas <=0:
                raise ValidationError('El valor de horas de la accion formativa no puede ser 0 o mas pequeño que 0')
            elif record.sesion_horas>record.horas:
                raise ValidationError('Las horas por sesion no puede ser mayor a la cantidad de horas de la accion formativa')
            elif record.sesion_horas<=0:
                raise ValidationError('El valor de horas por sesion no puede ser 0 o mas pequeño que 0')
            elif record.fecha_inicio<date.today():
                raise ValidationError('La fecha de inicio no puede ser anterior a la fecha actual')