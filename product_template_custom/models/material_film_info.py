from odoo import models, fields, api
from odoo.exceptions import ValidationError

class MaterialFilmInfo(models.Model):
    _name = 'material.film.info'
    _description = 'Material Film Info'

    name = fields.Char(string="Name", required=True)
    density_gcm3 = fields.Float(string="Density (g/cm3)",store=True, tracking=True)
    thickness_micron = fields.Float(string="Thickness (micron)", tracking=True)
    is_material = fields.Boolean(string='Is Material/Film?')
    is_active = fields.Boolean(string='is Active?')

    # untuk membatasi nilai density supaya tidak 0
    @api.constrains('density_gcm3','thickness_micron')
    def _check_density_gcm3(self):
        for record in self:
            if record.density_gcm3 <= 0:
                raise ValidationError("Density (g/cm3) must be greater than zero.")
            if record.thickness_micron <= 0:
                raise ValidationError("Thickness (micron) must be greater than zero.")

