{
    "name": "Website Variant Dropdown",
    "version": "19.0.1.0",
    "summary": "Convert product variants to dropdown",
    "category": "Website",
    "author": "Romodoor",
    "license": "LGPL-3",
    "depends": [
        "website",
        "website_sale"
    ],

    "data": [
        'views/store_categories.xml',
        "views/variant_scripts.xml",
    ],

    "assets": {
        "web.assets_frontend": [],
    },

    "installable": True,
    "application": False,
}