{
    'name': "school",
    'version': '18.0',
    'depends': ['base'],
    'author': "My Company",
    'category': 'Uncategorized',
    'description': """
    This is the custom school model contain teacher and student information 
    """,
    # data files always loaded at installation
    # xml file and security file are imported in data
    'data': [
        'views/student_views.xml', 
        'views/teacher_views.xml',
        'views/temporary_view.xml',
        'security/ir.model.access.csv',
    ],
    # data files containing optionally loaded demonstration data
    'demo': [
        # 'demo/demo_data.xml',
    ],
    'installable':True,
    'application':True,
}
