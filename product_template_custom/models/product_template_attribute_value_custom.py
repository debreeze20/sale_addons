from odoo import exceptions, models, fields, api

class ProductTemplateAttributeValueCustom(models.Model):
    _inherit = 'product.template.attribute.value'

    show_design_customer = fields.Boolean(
        string="Show Product Info", compute="_compute_show_design_customer"
    )

    @api.depends("attribute_id")
    def _compute_show_design_customer(self):
        for record in self:
            record.show_design_customer = record.attribute_id.name == "Design Customer"

    partner_id = fields.Many2one(
        comodel_name='res.partner', 
        string='Customer', 
        related='product_attribute_value_id.partner_id',
        store=True, 
        readonly=False
    )
