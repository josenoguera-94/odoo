{
    'name': 'primero',
    'summary': """
        Curso de odoo 14 para programadores
    """,
    'author': 'Jose Noguera',
    'version': '0.1',
    'application': True,
    # 'category': 'Marketing',
    # 'description': """sdasdas
    # """,
    'depends': ['mail', "hr"], #el modulo depende de mail
    'data': [
        "views/menu_view.xml",
        "views/libros_view.xml",
        "security/libreria_security.xml",
        "security/ir.model.access.csv",
        "views/hr_employee_view.xml"
    ],
    # 'demo': [],
    # 'installable': True,
    # 'auto_install': False,
}
