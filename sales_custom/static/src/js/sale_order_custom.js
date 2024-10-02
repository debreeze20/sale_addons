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
    // setup() {
    //     this._super(...arguments); // to call original setup
    //     this.orm = useService("orm") // to access Odoo ORM service

    // },
    // async willStart() {
    //     await this._super(...arguments);

    //     // to get current partner_id from so line
    //     const customerId = this.props.order.partner_id[0];
    //     // to filter product attribute values related to customer
    //     this._filterAttributeValues(relatedAttributeValues);
    // },

    // async _getRelatedAttributeValues(customerId) {
    //     // to get related  attribute values for the current partner_id
    //     // to return obj with attribute ids and allowed values for partner_id
    //     return await this.orm.call("product.template","get_related_attributes_values", [customerId]);

    // },

    // _filterAttributeValues(relatedAttributeValues) {
    //     // assum product attributes are selected dropdown
    //     // loop each attribute and filter the options
    //     const allAttributeElements = this.el.querySelectorAll(".attribute_selector_class");

    //     allAttributeElements.forEach(attributeElement => {
    //         const attributeId = attributeElement.getAttribute("data-attribute-id");

    //         const allowedValues = relatedAttributeValues[attributeId];

    //         if (allowedValues) {
    //             const allOptions = attributeElement.options;

    //             for (let i = 0; i < allOptions.length; i++) {
    //                 const optionValue = allOptions[i].value;

    //                 // hide other options
    //                 if (!allowedValues.includes(optionValue)) {
    //                     allOptions[i].style.display = "none";
    //                 } else {
    //                     allOptions[i].style.display = ""
    //                 }
    //             }
    //         }
    //     }

    //     )
    // }




    // async _onProductTemplateUpdate() {
    //     await this._super(...arguments); // to call original method

    //     const customerId = this.props.record.model.root.data.partner_id[0]; // to get current partner_id ID
    //     const filteredAttributes = await this._getFilteredAttributeValues(customerId);

    //     // to apply filter attributed to product line
    //     this.props.record.data.product_template_attribute_value_ids.records = this._filterAttributes(
    //         this.props.record.data.product_template_attribute_value_ids.records,
    //         filteredAttributes
    //     );

    //     this._onProductUpdate();
    // },

    // async _getFilteredAttributeValues(customerId) {
    //     // to get customer attribute values
    //     const attributes = await this.orm.call(
    //         "res.partner", "get_customer_specific_attribute", [customerId]
    //     );
    //     return attributes;
    // },

    // _filterAttributes (allAttributes, filteredAttributes) {
    //     // to filter attribute values
    //     return allAttributes.filter(attr => filteredAttributes.includes(attr.resId));
    // }
    
}

);