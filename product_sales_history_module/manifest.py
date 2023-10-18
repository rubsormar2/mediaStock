{
    'name': 'Product Sales Analysis',
    'version': '1.0',
    'depends': ['base', 'stock'],
    'author': 'Tu Nombre',
    'category': 'Custom',
    'description': """
        Calcula la media diaria de ventas para productos en los últimos 60 días con stock.
    """,
    'data': [
        'views/product_sales_analysis.xml',
    ],
    'installable': True,
    'application': False,
}
