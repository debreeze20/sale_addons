/** @odoo-module */

import { patch } from "@web/core/utils/patch";
import { ProductConfiguratorDialog } from "@sale_product_configurator/static/src/js/product_configurator_dialog";
import { useService } from "@web/core/utils/hooks";

patch (ProductConfiguratorDialog.prototype, "CustomConfiguratorDialogPatch", {
    // onWillStart() { 

    setup() {

                this.orm = useService("orm") // to access Odoo ORM service
        
            },

    async willStart() {    

        await this._super(...arguments);

        const customerId = this.props.order.partner_id[0];
        const filteredValues = await this._rpc({
                model: 'sale.order.line',
                method: 'get_filtered_attribute_values',
                args: [customerId],
        });
        this._filterAttributeValues(filteredValues);
    },
        // parent method
    //     return this._super(...arguments).then(() => {
    //         const customerId = this.props.order.partner_id[0]; // to get current partner_id
    //         console.log("Current Customer ID: ", customerId);
    //         // to get filtered attribute values
    //         // _rpc: to call methods defined on Odoo models directly from JS
    //         return this._rpc({
    //             model: 'sale.order.line',
    //             method: 'get_filtered_attribute_values',
    //             args: [customerId],
    //         }).then((filteredValues) => {
    //             this._filterAttributeValues(filteredValues);
    //             console.log("Filtered Values from RPC: ", filteredValues);
    //         });
    //     });
    // },

    _filterAttributeValues(filteredValues) {
        // loop attribute line in config dialog
        this.state.product_template.attribute_line_ids.forEach((line) => {
            line.value_ids = line.value_ids.filter(valueId => filteredValues.includes(this.env['product.attribute.value'].browse(valueId).name)
        ); // user id

        });
        console.log("After filtering: ", this.state.product_template.attribute_line_ids);
        this.render(); // to make sure UI only the attribute values available for current customer
    }
    
}

);