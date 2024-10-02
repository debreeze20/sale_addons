from odoo import models, fields, _, api
from odoo import exceptions
from odoo.exceptions import ValidationError


class ProductTemplateCustom(models.Model):
    _inherit = "product.template"

    categ_film_id = fields.Many2one(
        "material.film.info", readonly=False, string="Film Category"
    )
    density_gcm3 = fields.Float(
        string="Density (g/cm3)",
        compute="_compute_density_gcm3",
        store=True,
    )
    thickness_micron = fields.Float(
        string="Thickness (micron)", compute="_compute_thickness_micron", store=True
    )
    film_material_width = fields.Integer(
        string="Material Width", tracking=True, store=True
    )
    is_active = fields.Boolean("Is Active", compute="_compute_is_active", store=True)
    is_material = fields.Boolean(
        "Is Material", compute="_compute_is_material", store=True
    )

    @api.depends("categ_film_id")
    def _compute_density_gcm3(self):
        for record in self:
            record.density_gcm3 = (
                record.categ_film_id.density_gcm3 if record.categ_film_id else 0.0
            )

    @api.depends("categ_film_id")
    def _compute_thickness_micron(self):
        for record in self:
            record.thickness_micron = (
                record.categ_film_id.thickness_micron if record.categ_film_id else 0.0
            )

    @api.depends("categ_film_id")
    def _compute_is_material(self):
        for record in self:
            record.is_material = bool(
                record.categ_film_id and record.categ_film_id.is_material
            )

    @api.depends("categ_film_id")
    def _compute_is_active(self):
        for record in self:
            record.is_active = bool(
                record.categ_film_id and record.categ_film_id.is_active
            )

    @api.constrains("film_material_width", "is_material")
    def _check_film_material_width(self):
        for record in self:
            if record.is_material and record.film_material_width <= 0:
                raise ValidationError("Material Width must be greater than zero.")

    #  PRODUCT INFO

    show_product_info = fields.Boolean(
        string="Show Product Info", compute="_compute_show_product_info"
    )

    @api.depends("categ_id")
    def _compute_show_product_info(self):
        finish_goods = "Finish Goods"
        for record in self:
            record.show_product_info = record.categ_id.name == finish_goods
            parent = record.categ_id.parent_id
            while not record.show_product_info and parent:
                record.show_product_info = parent.name == finish_goods
                parent = parent.parent_id

    # Bag
    is_roll = fields.Boolean(string="Is Roll?")
    is_label = fields.Boolean(string="Is Label?")
    # @api.onchange('is_roll', 'special_product_type')
    # def _onchange_is_roll(self):
    #     if self.purchase_ok and self.special_product_type in ('consumable_production', 'consumable_other', 'film'):
    #         return
    #     if self.is_roll and self.special_product_type not in ('custom', 'standard'):
    #         self.is_roll = False

    bag_type = fields.Selection(
        [
            ("3_side_seal", "Sachet/3 Side Seal"),
            ("standing_pouch", "Standing Pouch"),
            ("center_seal", "Center Seal"),
        ],
        string="Bag Type",
        index=True,
        tracking=True,
    )
    bag_width_mm = fields.Integer(string="Bag Width (mm)")
    bag_height_mm = fields.Integer(string="Bag Height (mm)")
    bag_bottom_width_mm = fields.Integer(string="Bag Bottom Width (mm)")
    bag_open_size_width_mm = fields.Integer(string="Open Width (mm)", tracking=True)
    bag_open_size_height_mm = fields.Integer(string="Open Height (mm)", tracking=True)
    zipper_type = fields.Selection(
        [
            ("standard", "Zipper 13mm"),
            # ("small", "Zipper 7mm"),
            ("nonzipper", "Non Zipper"),
        ],
        string="Zipper Type",
        index=True,
        default="nonzipper",
    )
    # moved to design workorder
    zipper_center_position_from_top_mm = fields.Integer(
        string="Zipper Center Position from Top (mm)", default=26
    )
    is_degassing_valve = fields.Boolean(string="With Degassing Valve?")
    # moved to design workorder
    round_corner = fields.Boolean(string="Round Corner")
    # should be removed
    bottom_seal = fields.Boolean(string="Bottom Seal")

    coating_finishing_type = fields.Selection(
        [
            ("non_coated", "Non Coated"),
            ("glossy", "Glossy"),
            ("matte", "Matte"),
            ("super_glossy", "Super Glossy"),
        ],
        "Coating Type",
    )
    # moved to design workorder
    punch_hole_id = fields.Many2one("product.template.punch.hole", "Punch Hole")

    product_uom_id_real = fields.Many2one(
        "uom.uom",
        string="Unit of Measure",
        default=lambda self: self.env["uom.uom"].search([("name", "=", "g")], limit=1),
    )
    weight_real = fields.Float(string="Weight")

    is_hidden_from_customer = fields.Boolean("Hidden from Customer")
