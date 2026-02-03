
import re
from odoo import api, fields, models
from odoo.exceptions import ValidationError

class Comentario(models.Model):
    _name = 'incidencias.comentario'
    _description = 'Guarda los comentarios'

    name = fields.Text(string = 'Titulo', required = True)
    contenido = fields.Text(string = 'Descripción', required = True)
    fecha = fields.Datetime(string = 'Fecha de hoy', required = True)

    id_incidencia = fields.Many2one(comodel_name = 'incidencias.incidencia', string = 'Incidencia', required = True, ondelete = 'cascade')
    id_empleado = fields.Many2one(comodel_name= 'hr.employee', string = "Empleado", required = True, ondelete = "cascade")

    @api.onchange('fecha')
    def _onchange_date(self):
        if self.fecha:
            if self.contenido:
                # Mira si ya tiene una fecha en el titulo para actualizarlo usando un patron
                self.contenido = re.sub(r'-\d{4}-\d{2}-\d{2}.*$', '', self.contenido)
                self.contenido += f" - {str(self.fecha)}"
            else:
                self.contenido = f" - {str(self.fecha)}"

    @api.constrains('contenido')
    def _check_contenido_length(self):
        if self.contenido and len(self.contenido) < 25:
            raise ValidationError('El contenido debe ser mas de 25 caracteres')
    
    def copy(self, default=None):
        if not default:
            default={}

        contenido = self.contenido or ''
        contenido = re.sub(
            r'^\(Copia de \d{4}-\d{2}-\d{2}(?: \d{2}:\d{2}:\d{2})?\)\s*',
            '',
            contenido
        )
        default['contenido'] = f"(Copia de {self.fecha or ''}) {contenido}"

        return super().copy(default)