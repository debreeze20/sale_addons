from odoo import api, fields, models, _, tools
from odoo.exceptions import ValidationError, UserError
import logging

# from xendit import Xendit
import json
import requests
import re
_logger = logging.getLogger(__name__)

AVAILABLE_PRIORITIES = [
    ('0', 'Very Low'),
    ('1', 'Low'),
    ('2', 'Normal'),
    ('3', 'High'),
    ('4', 'Very High'),
    ('5', 'Ultra High')]

class Partner(models.Model):
    _inherit = 'res.partner'
    
    attribute_value_ids = fields.One2many(
        'product.template.attribute.value', 'partner_id', string="Attribute Values", store=True, copy=True)