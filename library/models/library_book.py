# -*- coding: utf-8 -*-

from odoo import models, fields


class LibraryBook(models.Model):
    _name = "library.book"

    name = fields.Char(string="Nombre", default="PRUEBA")
    description = fields.Text(string="Description")
    isbn = fields.Char("ISBN")

    category_ids = fields.One2many(
        comodel_name="library.category",
        inverse_name="book_id",
        string="Categorias")

    categ_count = fields.Integer(string="Nro categoria",
                                 compute="_count_categoria"
                                 )

#CONSTRAINT CON SQL
    _sql_constraints = [
        ('name_uniq', 'unique (name)', """Ya existe el libro !"""),
    ]

    # CONSTRAINT CON FRONTEDN
    # sapi._constraints = ("isbn")
    # def check_isbn(self):
    #    isbn = self.search([['id', '!=', self.id]]).mapped("isbn")
    #   if self.isbn and self.isbn in isbn:
    #      raise  exceptions.ValidationError("IDB DUPLICADO")


#INICIO CAMPOS CALCULADOS
    #def _count_categoria(self):
     #   self.categ_count = len(self.category_ids)

    def _count_categoria(self):
        for book in self:
            book.categ_count = len(book.category_ids)

#FIN CAMPOS CALCULADOS

