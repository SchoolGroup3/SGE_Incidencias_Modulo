from odoo import models, fields, api

class Empleado(models.Model):
    _inherit = "hr.employee"

    descripcion = fields.Text(string = 'Introduce la descripción')

    id_incidencia = fields.Many2many(
        comodel_name = 'incidencias.incidencia',
        field_name = 'id_incidencia',
        required=True, 
        ondelete = 'cascade'
    )