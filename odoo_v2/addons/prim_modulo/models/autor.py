from odoo import models, fields


class Autor(models.Model):
    _name = "autor"

    _rec_name = "last_name" # renombrar la columna que se muestra en la relacion many2one
    
    name = fields.Char(string="Nombre")
    last_name = fields.Char(string="Apellido")