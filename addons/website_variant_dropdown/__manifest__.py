{
    "name": "Website Variant Dropdown",
    "version": "19.01.03",
    "summary": "Advanced Online Door Expert",
    "category": "Website",
    "author": "Romodoor",
    'license': 'LGPL-3',
    "depends": [
            'website',
            'website_sale'
        ],
    "data": [
        "views/product_variant_templates.xml",
    ],
    "assets": {
        "web.assets_frontend": [
            "website_variant_dropdown/static/src/scss/variant.scss",
            "website_variant_dropdown/static/src/js/variant_dropdown.js",
        ],
    },
   'installable': True,
}