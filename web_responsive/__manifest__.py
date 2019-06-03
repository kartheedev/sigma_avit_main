

{
    "name": "Web Responsive",
    "summary": "Responsive web client, community-supported",
    "version": "12.0.1.1.0",
    "category": "Website",
    "author": "Indglobal digital",
    'company': 'Indglobal digital pvt ltd',
    'website': "https://indglobal.in/",
    "license": "LGPL-3",
    "installable": True,
    "depends": [
        'web',
        'mail',
    ],
    "data": [
        'views/assets.xml',
        'views/res_users.xml',
        'views/web.xml',
    ],
    'qweb': [
        'static/src/xml/apps.xml',
        'static/src/xml/form_view.xml',
        'static/src/xml/navbar.xml',
    ],
}
