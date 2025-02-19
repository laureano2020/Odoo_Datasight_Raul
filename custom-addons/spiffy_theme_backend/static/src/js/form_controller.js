/** @odoo-module **/

// # Part of Odoo Module Developed by Bizople Solutions Pvt. Ltd.
// # See LICENSE file for full copyright and licensing details.

var { patch } = require("web.utils");
import {FormController} from "@web/views/form/form_controller";
import {FormStatusIndicator} from "@web/views/form/form_status_indicator/form_status_indicator";
var session = require("@web/session");
const { onMounted, onPatched } = owl;

patch(FormController.prototype, "spiffy_theme_backend.SpiffyFormController", {
    setup(){
        this._super();
        onMounted(() => {
            $('div.o_attachment_preview').length > 0 ? $('body').addClass('hasAttachment') : $('body').removeClass('hasAttachment');
        });

        onPatched(() => {
            $('div.o_attachment_preview').length > 0 ? $('body').addClass('hasAttachment') : $('body').removeClass('hasAttachment');
        });
    },
    
    async onPagerUpdate({ offset, resIds }) {
        await this.model.root.askChanges(); // ensures that isDirty is correct
        let canProceed = true;
        if (this.model.root.isDirty) {
            if ($('body').hasClass('prevent_auto_save')){
                return this.model.root.discard();
            } else {
                canProceed = await this.model.root.save({
                    stayInEdition: true,
                    useSaveErrorDialog: true,
                });
            }
        }
        if (canProceed) {
            return this.model.load({ resId: resIds[offset] });
        }
    },

    async beforeLeave() {
        if (this.model.root.isDirty) {
            if ($('body').hasClass('prevent_auto_save')){
                return this.model.root.discard();
            } else {
                return this.model.root.save({
                    noReload: true,
                    stayInEdition: true,
                    useSaveErrorDialog: true,
                });
            }
        }
    }
});

patch(FormStatusIndicator.prototype, "spiffy_theme_backend.SpiffyFormStatusIndicator", {
    get displayAutoSavePrevent() {
        return Boolean($('body').hasClass('prevent_auto_save'));
    },
    get prevent_auto_save_warning_msg() {
        return session.session.prevent_auto_save_warning_msg
    },
});