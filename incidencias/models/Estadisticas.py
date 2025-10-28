from odoo import fields, models

class Estadistica(models.Model):
    _name = 'incidencias.estadisticas'
    _description = "Descripcion de estadisticas"

    fecha =fields.Datetime(string = 'Fecha de creación')
    total_incidencias = fields.Integer(string="Total Incidencias")
    incidencias_finalizadas = fields.Integer(string="Incidencias Finalizadas")
    tiempo_promedio_resolucion = fields.Char(string="Tiempo Promedio Resolucion")