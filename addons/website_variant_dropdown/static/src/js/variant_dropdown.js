document.addEventListener("DOMContentLoaded", function () {
    console.log("variant dropdown module loaded");

    const attributes = document.querySelectorAll(".variant_attribute");

    attributes.forEach(function(attribute){

        const radios = attribute.querySelectorAll("input.js_variant_change");

        if(!radios.length) return;

        const label = attribute.querySelector(".attribute_name");

        const selectWrapper = document.createElement("div");
        selectWrapper.classList.add("variant-dropdown");

        const select = document.createElement("select");
        select.classList.add("form-select");

        radios.forEach(function(radio){

            const option = document.createElement("option");

            option.value = radio.value;

            const text = radio.closest("label").innerText.trim();

            option.textContent = text;

            if(radio.checked){
                option.selected = true;
            }

            select.appendChild(option);

        });

        selectWrapper.appendChild(select);

        attribute.appendChild(selectWrapper);


        /* dropdown change → trigger radio */

        select.addEventListener("change", function(){

            const radio = attribute.querySelector(
                'input[value="' + this.value + '"]'
            );

            if(radio){

                radio.checked = true;

                radio.dispatchEvent(new Event("change", {
                    bubbles:true
                }));

            }

        });

    });

});