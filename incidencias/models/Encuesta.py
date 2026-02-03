import re
from xml.dom import ValidationErr

from odoo import fields, models, api
from odoo.exceptions import ValidationError

class Encuesta(models.Model):
    _name = 'incidencias.encuesta'
    _description = 'guarda las encuestas'

    #campos
    puntuacion = fields.Selection(
        [
            ('0', '0'),
            ('1', '1'),
            ('2', '2'),
            ('3', '3'),
            ('4', '4'),
            ('5', '5'),
        ],
        string='Puntuación',
        default='0'
    )


    name = fields.Text(string = 'Nombre de la encuesta', required = True)
    comentario = fields.Text(string = 'Introduce la descripción')
    fecha_respuesta =fields.Datetime(string = 'Fecha de hoy')
    ruta_archivo = fields.Binary(string="Ruta del Archivo")

    #campos relacionales
    x_id_incidencia = fields.Many2one(comodel_name = "incidencias.incidencia", string = 'Incidencia', required = True, ondelete = 'cascade')

    proyecto = fields.Many2one(comodel_name='project.task', string='Tarea de Proyecto', required=False,
                               ondelete='cascade')

    @api.onchange('comentario')
    def _onchange_event_id(self):
        if self.comentario == "":
            self.comentario = "No se ha introducido comentario"

    @api.constrains('name')
    def _check_name(self):
        if len(self.name) < 4:
            raise ValidationError('El nombre es demasiado corto. Mínimo 4 caracteres.')

        patron = r'^[a-zA-Z0-9áéíóúÁÉÍÓÚñÑ\s_]+$'  # PONER QUE DEJE ESPACIOS
        if not re.match(patron, self.name):
            raise ValidationError('No se permiten caracteres especiales')


    def copy(self, default=None):
        if default is None:
            default = {}

        default['name'] = f"Copia de {self.name}"

        return super(Encuesta, self).copy(default)

    @api.model
    def create(self, vals):
        if 'name' in vals:
            vals['name'] = vals['name'].replace(" ","_")

        return super(Encuesta, self).create(vals)