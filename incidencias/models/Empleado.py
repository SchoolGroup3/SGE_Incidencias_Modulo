from odoo import models, fields, api

class Empleado(models.Model):
    _inherit = "hr.employee"

    descripcion = fields.Text(string = 'Introduce la descripción')