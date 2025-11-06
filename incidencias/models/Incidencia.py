from odoo import fields, models

class Incidencia(models.Model):
    _name = 'incidencias.incidencia'
    _description = 'Guarda las incidencias'

    titulo = fields.Text(string = 'Introduce el titulo')
    descripcion = fields.Text(string = 'Introduce la descripción')
    fecha_creacion =fields.Datetime(string = 'Fecha de creación')
    estado_actual = fields.Text(string = 'Introduce el estado actual')

    id_departamento = fields.Many2one(comodel_name = 'hr.department', string = 'Incidencia', required = True, ondelete = 'cascade')
    id_empleado_origen = fields.Many2one(comodel_name= 'hr.employee', string = "Empleado", required = True, ondelete = "cascade")
