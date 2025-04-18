from odoo import models, fields, api

class ClothingMaterial(models.Model):
    _name = 'clothing.material'
    _description = 'Clothing Material'

    name = fields.Char(string='Material Name', required=True)
    code = fields.Char(string='Material Code')
    material_type = fields.Selection([
        ('fabric', 'Fabric'),
        ('thread', 'Thread'),
        ('button', 'Button'),
        ('zipper', 'Zipper'),
        ('other', 'Other')
    ], string='Type')
    supplier = fields.Char(string='Supplier')
    cost = fields.Float(string='Cost per Unit')
    uom = fields.Char(string='Unit of Measure', default='meters')
    color = fields.Char(string='Color')