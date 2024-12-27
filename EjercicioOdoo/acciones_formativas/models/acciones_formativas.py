from odoo import models, fields, api

class Acciones_formativas(models.Model):
    _name = 'acciones_formativas'
    _description = 'Acciones formativas'
    
    name = fields.Char(string='Nombre de la accion formativa', required=True)
    curso_id = fields.Many2one('formaciones.cursos', string='Curso')
    formador_id = fields.Many2one('res.partner', string='Formador')
    participantes_id = fields.Many2many('res.partner', string='Participantes')
    horas_curso = fields.Integer(string='Total de horas del curso', readonly=True)
    horas = fields.Integer(string='Numero de horas de la accion formativa')
    sesion_horas = fields.Integer(string='Horas por sesion')
    sesiones = fields.Integer(string='Numero de sesiones', readonly=True)

    @api.depends('formador_id')
    def _compute_formadores(self):
        for record in self:
            formadores = self.env['res.partner'].search([('formador', '=', True)])
            record.formador_id = formadores
    