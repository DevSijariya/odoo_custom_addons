#Importing the odoo Basic Modules
from odoo import models, fields


class Student_detail(models.Model):
    """
    Description: Student Class which is used to store student information
    """
    _name = "student_information"
    _description = "This Model is used to store the information of the student "

    name= fields.Char("Name")
    Age=fields.Integer("Age")
    roll_number = fields.Integer("Roll Number")
    branch = fields.Char("Branch")


class Teacher_detail(models.Model):
    """
    Description: Student Class which is used to store Teacher information
    """
    _name = "teacher_information"
    _description = "This model is used to store the information of the teacher"
    name= fields.Char("Name")
    Age=fields.Integer("Age")
    subject = fields.Char("Subject")


