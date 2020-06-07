# -*- coding: utf-8 -*-
# from odoo import http


# class Many2many(http.Controller):
#     @http.route('/many2many/many2many/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/many2many/many2many/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('many2many.listing', {
#             'root': '/many2many/many2many',
#             'objects': http.request.env['many2many.many2many'].search([]),
#         })

#     @http.route('/many2many/many2many/objects/<model("many2many.many2many"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('many2many.object', {
#             'object': obj
#         })
