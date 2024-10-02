from venv import logger
from odoo import models, fields, api


class SaleOrderLineCustom(models.Model):
    _inherit = "sale.order.line"

    @api.model
    def get_filtered_attribute_values(self, partner_id):
        partner_id = self.env['res.partner'].browse([partner_id])
        
        attribute_values = self.env['product.attribute.value'].search([('id','in',  partner_id.attribute_value_ids.ids)])
        filtered_names = attribute_values.mapped('name')

        logger.debug("Filtered Attribute Values for Partner %s: %s", partner_id, filtered_names)
        # Return the filtered attribute values to the frontend
        return filtered_names
        