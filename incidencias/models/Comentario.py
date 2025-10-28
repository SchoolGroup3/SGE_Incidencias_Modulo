
from odoo import fields, models

class Comentario(models.Model):
    _name = 'incidencias.comentario'
    _description = 'Guarda los comentarios'

    contenido = fields.Text(string = 'Introduce la descripción')
    fecha = fields.Datetime(string = 'Fecha de hoy')

    id_incidencia = fields.Many2one(comodel_name = 'incidencias.incidencia', string = 'Incidencia', required = True, ondelete = 'cascade')
    id_empleado = fields.Many2one(comodel_name= 'incidencias.employee', string = "Empleado", required = True, ondelete = "cascade")