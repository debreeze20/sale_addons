# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class sale_configurator(models.Model):
#     _name = 'sale_configurator.sale_configurator'
#     _description = 'sale_configurator.sale_configurator'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

