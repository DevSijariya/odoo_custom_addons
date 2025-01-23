{
    'name': "Sales",
    'version': '18.0',
    'depends': ['base','sale'],
    'author': "My Company",
    'category': 'Uncategorized',
    'description': """
    This is the custom sales model which extending the existing sale functionality 
    """,
    # data files always loaded at installation
    # xml file and security file are imported in data
    'data': [
        'security/ir.model.access.csv',
        'views/sales_views.xml'
    ],
    # data files containing optionally loaded demonstration data

    'installable':True,
    'application':True,
}
