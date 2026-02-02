from odoo import fields, models, api
from odoo.exceptions import ValidationError

class Estadistica(models.Model):
    _name = 'incidencias.estadisticas'
    _description = "Descripcion de estadisticas"

    employee_id = fields.Many2one("hr.employee", string="Empleado", required=True)

    nombre = fields.Char(related="employee_id.name", store=True)
    fecha =fields.Datetime(string = 'Fecha de creación', required=True)
    total_incidencias = fields.Integer(string="Total Incidencias")
    incidencias_finalizadas = fields.Integer(string="Incidencias Finalizadas")
    tiempo_promedio_resolucion = fields.Char(string="Tiempo Promedio Resolucion")

    @api.onchange('incidencias_finalizadas')
    def onchange_incidencias_finalizadas(self):
        if self.incidencias_finalizadas:
            self.total_incidencias = self.total_incidencias + self.incidencias_finalizadas

    @api.constrains('total_incidencias')
    def _incidenciascheck(self):
        if self.total_incidencias < 0:
            raise ValidationError("El total de incidencias no puede ser negativo.")

    @api.model
    def create(self, vals):
        if not vals.get('fecha'):
            vals['fecha'] = fields.Datetime.now()
        return super(Estadistica, self).create(vals)

    def copy(self, default=None):
        if default is None:
            default = {}
        return super(Estadistica, self).copy(default)