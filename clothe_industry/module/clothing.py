from odoo import models, fields, api

class ClothingProduct(models.Model):
    _name = 'clothing.product'
    _description = 'Clothing Product'

    name = fields.Char(string='Product Name', required=True)
    code = fields.Char(string='Product Code')
    description = fields.Text(string='Description')
    material_ids = fields.Many2many(
        'clothing.material', 
        string='Materials Used'
    )
    size = fields.Selection([
        ('xs', 'XS'),
        ('s', 'S'),
        ('m', 'M'),
        ('l', 'L'),
        ('xl', 'XL'),
        ('xxl', 'XXL')
    ], string='Size')
    price = fields.Float(string='Price')
    image = fields.Binary(string='Product Image')
    active = fields.Boolean(string='Active', default=True)