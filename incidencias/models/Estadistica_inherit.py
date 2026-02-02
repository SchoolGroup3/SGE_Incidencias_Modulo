from odoo import fields, models

class Estadistica(models.Model):
    _inherit = "hr.employee"

    estadistica_id = fields.One2many(
        "incidencias.estadisticas",
        "employee_id",
        string="Estadísticas"
    )

    nombre=fields.Char(string="nombre", related='estadistica_id.nombre')