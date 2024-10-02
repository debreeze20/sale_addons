from odoo import api, fields, models, _
from odoo import exceptions
from odoo.exceptions import UserError, ValidationError 

# pop up for form
class ProductAttributeValueCustom(models.Model):
    _inherit = 'product.attribute.value'

    partner_id = fields.Many2one(
        comodel_name='res.partner', 
        string='Customer', 
        store=True,
        index=True,
        readonly=False
    )

    product_tmpl_id = fields.Many2one('product.template', store=True, index=True, copy=True, )
    attribute_name = fields.Char(related='attribute_id.name')

    @api.constrains('partner_id', 'attribute_id')
    def _check_partner_id(self):
        for record in self:
            if record.attribute_name == 'Design Customer' and not record.partner_id:
                raise exceptions.ValidationError("Customer must be set when the attribute is 'Design Customer'.")