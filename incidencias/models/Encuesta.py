
from odoo import fields, models

class Encuesta(models.Model):
    _name = 'incidencias.encuesta'
    _descripcion = 'guarda las encuestas'

    #campos
    puntuacion = fields.Integer(string = 'Puntuación', required=True)
    comentario = fields.Text(string = 'Introduce la descripción')
    fecha_respuesta =fields.Datetime(string = 'Fehca de hoy')

    #campos relacionales
    #id_incidencia = fields.Many2one(comodel_name = Incidencias.incidencia, string = 'Incidencia', required = True, ondelete = 'cascade')


