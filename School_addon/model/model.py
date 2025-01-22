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
    dob = fields.Date("Date of Birth")

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


class TeacherDetail(models.Model):
    """
    Description: Student Class which is used to store Teacher information
    """
    _name = "teacher.information" # Set the name of the new model
    _description = "This model is used to store the information of the teacher"
    _inherit = 'common.details' # Inherit the Abstract model

    subject = fields.Char("Subject")
    salary=fields.Integer("Salary")


class TemporaryData(models.TransientModel):
    """
    Description : Creating the Temporary  Transient Model
    """

    _name = "temporary.data"
    _description = "Creating the temporay model"

    
    u_id=fields.Integer("Id")