// # Part of Odoo Module Developed by Bizople Solutions Pvt. Ltd.
// # See LICENSE file for full copyright and licensing details.
odoo.define('spiffy_theme_backend.SpiffyPageTitle', function (require) {
"use strict";

    var ajax = require('web.ajax');
    var { WebClient } = require("@web/webclient/webclient");
    var { patch } = require("web.utils");

    patch(WebClient.prototype, "spiffy_theme_backend.SpiffyPageTitle", {
        setup() {
            this._super();
            var self = this
            ajax.rpc('/get/tab/title/').then(function(rec) {
                var new_title = rec
                self.title.setParts({ zopenerp: new_title })
            })
        },
    });
});