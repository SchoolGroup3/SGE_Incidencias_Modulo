from odoo import models, fields, api

class Empleado(models.Model):
    _inherit = "hr.employee"

    descripcion = fields.Text(string = 'Introduce la descripción')

    id_estadisticas = fields.Many2many(
        comodel_name = 'incidencias.estadisticas',
        field_name = 'id_estadisticas',
        required=True, 
        ondelete = 'cascade'
    )