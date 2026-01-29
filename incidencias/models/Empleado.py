from odoo import models, fields, api

class Empleado(models.Model):
    _inherit = "hr.employee"

    nombre = fields.Char(string = "Nombre", related = "name")
    descripcion = fields.Text(string = 'Introduce la descripción')
    email = fields.Char(string = "Email", related = "work_email")

    id_estadisticas = fields.Many2many(
        comodel_name = 'incidencias.estadisticas',
        field_name = 'id_estadisticas',
        required=True, 
        ondelete = 'cascade'
    )