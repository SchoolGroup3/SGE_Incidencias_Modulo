import re
from odoo import api, fields, models
from odoo.exceptions import ValidationError

class Incidencia(models.Model):
    _name = 'incidencias.incidencia'
    _description = 'Guarda las incidencias'

    name = fields.Text(string = 'Titulo', required = True)
    descripcion = fields.Text(string = 'Descripción', required = True)
    fecha_creacion =fields.Datetime(string = 'Fecha de creación', required = True)
    estado_actual = fields.Selection([
        ('cancelado', 'Cancelado'),
        ('en_progreso', 'En Progreso'),
        ('terminado', 'Terminado'),
    ], string='Estado Actual', default='en_progreso')

    id_departamento = fields.Many2one(comodel_name = 'hr.department', string = 'Departamento', required = True, ondelete = 'cascade')
    id_empleado_origen = fields.Many2one(comodel_name= 'hr.employee', string = "Empleado", required = True, ondelete = "cascade")

    proyecto = fields.Many2one(comodel_name='project.task', string='Tarea de Proyecto', required=False, ondelete='cascade')
    ids_comentarios = fields.One2many(comodel_name='incidencias.comentario', inverse_name='id_incidencia', string='Comentarios')

    @api.onchange('fecha_creacion')
    def _onchange_date(self):
        if self.fecha_creacion:
            self.name = re.sub(r'-\d{4}-\d{2}-\d{2}.*$', '', self.name)
            self.name += f"-{str(self.fecha_creacion)}"

    @api.constrains('name')
    def _check_titulo_length(self):
        if self.name and len(self.name) < 5:
            raise ValidationError('El titulo debe ser mas de 5 caracteres')
    
    @api.model
    def create(self, vals):
        if 'name' in vals:
            vals['name'] = vals['name'].replace(" ", "-")
        
        return super(Incidencia, self).create(vals)
    def copy(self, default=None):
        if not default:
            default={}
        default['name'] = f"Copia de {self.name}"
        return super(Incidencia, self).copy(default)
