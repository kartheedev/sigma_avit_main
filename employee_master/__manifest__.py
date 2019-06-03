{
    'name': 'Emplyee Master Data',
    'version': '1.0',
    'depends': ['base','hr'],
    'author': 'Indglobal digital',
    'company': 'Indglobal digital pvt ltd',
    'website': "https://indglobal.in/",
    'data': [
                'security/ir.model.access.csv',
                'view/employee_view.xml',
                'view/employee_core_view.xml',
                'data/ir_sequence_data.xml',
            ],

    'license': 'AGPL-3',
    'installable': True,
    'auto_install': True,
    'application': False,
}
