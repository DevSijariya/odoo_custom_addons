from odoo import models ,fields

from .model import CommonDetails

class StudentDetail(models.Model):
    """
    Description: Student Class which is used to store student information
    """
    _name = "student.information" # Set the name of the new model
    _description = "This Model is used to store the information of the student "
    _inherit = "common.details" #Inherit the Abstract model

    roll_number = fields.Integer("Roll Number")
    branch = fields.Char("Branch")
    admission_date=fields.Date('Admission Date')
    leaving_date=fields.Date('leaving Date')