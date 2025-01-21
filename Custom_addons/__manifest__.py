{
    'name': "student",
    'version': '18.0',
    'depends': ['base'],
    'author': "My Company",
    'category': 'Uncategorized',
    'description': """
    This is the custom student module   
    """,
    # data files always loaded at installation
    # xml file and security file are imported in data
    'data': [
        'views/student_views.xml', 
        'security/ir.model.access.csv',
    ],
    # data files containing optionally loaded demonstration data
    'demo': [
        # 'demo/demo_data.xml',
    ],
}
