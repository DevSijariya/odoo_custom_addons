#Importing the odoo Basic Modules
from odoo import models, fields



class CommonDetails(models.AbstractModel):
    """
    Description : Creating the Abstract model which contain the common feilds for both the students and the teacher
    
    """
    _name = "common.details" # Set the name of the new model
    _description = "Contain Common Informations"

    name = fields.Char("Name")
    age = fields.Integer("Age")
    # dob = fields.Date("Date of Birth")
    date_of_birth = fields.Date("Date of Birth")





class TransientMode(models.TransientModel):
    _name = 'transient.mode'

    boolean = fields.Boolean()
    integer = fields.Integer()
    float = fields.Float()
    char = fields.Char()
    selection = fields.Selection([('one', 'One'), ('two', 'Two')])
    partner = fields.Many2one('res.partner')

