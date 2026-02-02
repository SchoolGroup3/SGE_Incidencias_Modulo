from odoo import fields, models

class ProjectTask(models.Model):
    _inherit = "project.task"

    #Campos que se van a insertar en la vista heredada
    incidencias_id = fields.One2many(comodel_name="incidencias.incidencia",inverse_name="proyecto",string="Incidencias")

    name = fields.Text(string="Nombre", related="incidencias_id.name")
    descripcion = fields.Text(string="Descripcion", related="incidencias_id.descripcion")
    fecha_creacion = fields.Datetime(string="Fecha", related="incidencias_id.fecha_creacion")

    encuesta_id = fields.One2many(comodel_name="incidencias.encuesta", inverse_name="proyecto",string="Encuestas")


    comentario = fields.Text(string="Comentario", related="encuesta_id.comentario")
    puntuacion = fields.Selection(string="Puntuacion", related="encuesta_id.puntuacion")

    adjunto_id = fields.One2many(comodel_name="incidencias.adjunto", inverse_name="proyecto", string="Adjunto")

    nombre_archivo = fields.Char(string="Nombre del Archivo", related="adjunto_id.nombre_archivo")
    ruta_archivo = fields.Binary(string="Ruta del Archivo", related="adjunto_id.ruta_archivo")
