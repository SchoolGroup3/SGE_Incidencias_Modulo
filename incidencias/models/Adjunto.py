from odoo import fields, models, api
from odoo.exceptions import ValidationError

class Adjunto(models.Model):
    _name = "incidencias.adjunto"
    _description = "Archivos adjuntos relacionados con comentarios"

    # Campos simples
    name = fields.Char(string="Nombre", required=True)
    nombre_archivo = fields.Char(string="Nombre del Archivo", required=True)
    ruta_archivo = fields.Binary(string="Ruta del Archivo", required=True)
    fecha_subida = fields.Datetime(string="Fecha de Subida", default=fields.Datetime.now)
    #Campos relacionados
    proyecto = fields.Many2one(comodel_name="project.task")

    @api.onchange('nombre_archivo')
    def _onchange_nombre_archivo(self):
        if self.nombre_archivo:
            self.name = self.nombre_archivo
        else:
            self.name = ''
    @api.constrains('nombre_archivo')
    def _check_name(self):
        if self.nombre_archivo and len(self.nombre_archivo) < 10:
            raise ValidationError('El Nombre del Archivo debe tener minimo 10 digitos')

    @api.model
    def create (self, vals):
        if vals.get('name') and len(vals['name'])<10:
            raise ValidationError('No se puede crear el adjunto: el Nombre debe tener minimo 10 caracteres.')
        return super(Adjunto, self).create(vals)
    def write(self, vals):
        if 'name' in vals and len(vals['name']) <10:
            raise  ValidationError('No se puede modificar: el Nombre debe tener minim 10 caracteres.')
        return super(Adjunto, self).create(vals)
    def copy(self, default=None):
        if default is None:
            default = {}
        default['name'] = f"Copia de {self.name}"
        default['nombre_archivo'] = f"Copia de {self.nombre_archivo}"
        default['fecha_subida'] = fields.Datetime.now()
        return super(Adjunto, self).copy(default)
