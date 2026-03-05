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

    "data": [],

    "assets": {
        "web.assets_frontend": [
            "website_variant_dropdown/static/src/scss/variant.scss",
            "website_variant_dropdown/static/src/js/variant_dropdown.js",
        ],
    },

    "installable": True,
    "application": False,
}