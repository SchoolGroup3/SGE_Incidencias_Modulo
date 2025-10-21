from odoo import fields, models

class Adjunto(models.Model):
    _name = "incidencias.adjunto"
    _description = "Archivos adjuntos relacionados con comentarios"

    # Campos simples
    nombre_archivo = fields.Char(string="Nombre del Archivo", required=True)
    ruta_archivo = fields.Binary(string="Ruta del Archivo", required=True)
    fecha_subida = fields.Datetime(string="Fecha de Subida", default=fields.Datetime.now)
