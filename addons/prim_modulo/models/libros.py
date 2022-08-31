from odoo import models, fields, api

# fields.Many2one
# fields.Many2many
# fields.Many2oneReference
# fields.One2many


#Creando un modelo a partir de una clase

class Libros(models.Model):

    _name = "libros" # Palabra reservada de odoo , nombre de la tabla
    _inherit = ['mail.thread', 'mail.activity.mixin']

    supervisor_id = fields.Many2one(comodel_name="hr.employee", string="Supervisor") 
                                                                # tracking sirve para cuando utilicemos el modulo mail pueda ver que cambios se realizaron a un campo en especifico
    name = fields.Char(string="Nombre del libro", required=True, tracking=True) # ,required=True requerido a nivel de DB exite requerido a nievel de vista
    editorial = fields.Char(string="Editorial", required=True)
    isbn = fields.Char(string="ISBN", required=True)
    autor_id = fields.Many2one(comodel_name="autor", string="Autor", required=True)
    lastname_autor = fields.Char(related="autor_id.last_name", string="Apellido del autor") # los campos related funcionan solo con relación many2one
    image = fields.Binary(string="Image")
    categoria_id = fields.Many2one(comodel_name="categoria.libro")
    state = fields.Selection([('draft', 'Borrado'), ('published', 'Publicado')], default='draft')
    description = fields.Char(string="Description", compute="_compute_description") # para que se guarde en la DB hay que colocar store=True (pero necesita el singleton) si no se muestro solo caluclado y listo

    _sql_constraints = [("name_uniq", "unique (name)", "El nombre del libro ya existe")] # se debe eliminar desde la tabla directamente cuando ya no requiera

    # _sql_constraints Recibe 3 parámetros
    # nombre del sql constraint
    # unique, () los valores que no se quiere que se duoliquen
    # mensaje de error

    @api.depends("name", "isbn") # si no se ponde el depends el sistema lo calculara siempre. - este decorador con parametros hace que al actualizar el nombre sin darle guardar se calcule n tiempo real
    def _compute_description(self): 

        self.description = self.name + " | " + self.isbn + " | " + self.autor_id.name + " | " + self.categoria_id.name

    def boton_publicar(self):
        self.state = 'published'
        # print("Prueba boton")

    def boton_borrador(self):
        self.state = 'draft'
        # print("Prueba boton")




class CategoriaLibro(models.Model):

    _name = "categoria.libro"

    name = fields.Char(string="Nombre de la categoria") 
 