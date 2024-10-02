from odoo import models, fields, api
from odoo.exceptions import ValidationError


class PunchHole(models.Model):
    _name = "product.template.punch.hole"
    _description = "Punch Hole"

    name = fields.Char(string="Name", required=True)

    product_template_ids = fields.One2many(
        "product.template", "punch_hole_id", "Products"
    )
