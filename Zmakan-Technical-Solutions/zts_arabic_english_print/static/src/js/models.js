odoo.define('zts_arabic_english_print.models', function (require) {
    "use strict";

    var models = require('point_of_sale.models');
 
    models.load_fields('product.product',['arab_name']);


});
