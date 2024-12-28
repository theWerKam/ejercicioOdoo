from odoo import models, fields

class Cursos(models.Model):
    _name = 'formaciones.cursos'
    _description = 'Cursos'

    name = fields.Char(string='Nombre del Curso', required=True)
    duracion = fields.Integer(string='Duracion del curso en horas', required=True)
    resumen = fields.Text(string='Descripcion', required=True)
    #accionFormativa_id = fields.One2many('acciones_formativas.acciones_formativas', 'curso_id', string='Acciones Formativas')