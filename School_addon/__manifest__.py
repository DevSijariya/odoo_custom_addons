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
        'views/school_views.xml', 
        'security/ir.model.access.csv',
    ],
    # data files containing optionally loaded demonstration data
    'demo': [
        # 'demo/demo_data.xml',
    ],
    'installable':'True',
    'license' : 'LGPL-3',
    'application':'False',
}
