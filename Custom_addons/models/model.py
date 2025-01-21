# from odoo18.odoo import fields,models
from odoo import fields,models
class  Students(models.Model):
    """
    Description : Creating a Student Model  Which takes it information and store it in Database
    
    """
    _name = "students" # Define the Name for the model in odoo system
    _description = "This is a Student profile" # Define the Description of the student model

    name = fields.Char("Name")
    Age = fields.Integer('Age')
    dob = fields.Date(string="Date Of Birth")
    