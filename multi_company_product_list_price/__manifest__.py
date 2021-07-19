{
    'name': "Sales Price Multicompany",

    'summary': """
        Product sale and cost prices are now company-specific.
    """,

    'sequence': 404,

    'author': "Arxi",
    'website': "https://www.arxi.pt",
    'license': 'OPL-1',

    'category': 'Sales',
    'version': '14.0.1.0.1',

    'price': 50.00,
    'currency': 'EUR',

    'depends': [
        'product'
    ],

    'data': [
    ],
    'post_init_hook': '_post_init_hook',

    'images': [
        'static/description/banner.jpg',
    ],
}
