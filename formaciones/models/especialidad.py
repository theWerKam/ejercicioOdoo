from odoo import models, fields

class Especialidad(models.Model):
    _name = 'formaciones.especialidad'
    _description = 'Especialidades'

    name = fields.Char(string='Nombre de la especialidad', required=True)
    descripcion = fields.Text(string='Descripcion', required=True)