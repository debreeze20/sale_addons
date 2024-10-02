# -*- coding: utf-8 -*-
# from odoo import http


# class SaleConfigurator(http.Controller):
#     @http.route('/sale_configurator/sale_configurator', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/sale_configurator/sale_configurator/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('sale_configurator.listing', {
#             'root': '/sale_configurator/sale_configurator',
#             'objects': http.request.env['sale_configurator.sale_configurator'].search([]),
#         })

#     @http.route('/sale_configurator/sale_configurator/objects/<model("sale_configurator.sale_configurator"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('sale_configurator.object', {
#             'object': obj
#         })

