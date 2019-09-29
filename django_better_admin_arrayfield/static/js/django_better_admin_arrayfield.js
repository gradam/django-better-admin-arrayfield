// I am to lazy to add js transpiler and compressor to this. just use https://jscompress.com

window.addEventListener('load', function () {
    let item_count = 1;

    function addRemoveEventListener(widgetElement) {
        widgetElement.querySelectorAll('.remove').forEach(element => {
            element.addEventListener('click', () => {
                element.parentNode.remove();
            });
        });
    }

    document.querySelectorAll('.dynamic-array-widget').forEach(widgetElement => {

        const initialElement = widgetElement.querySelector('.array-item');
        const elementTemplate = initialElement.cloneNode(true);
        const parentElement = initialElement.parentElement;

        if (initialElement.getAttribute('data-isNone')) {
            initialElement.remove();
            elementTemplate.removeAttribute('data-isNone');
            elementTemplate.removeAttribute('style');
        }
        addRemoveEventListener(widgetElement);

        widgetElement.querySelector('.add-array-item').addEventListener('click', () => {
            item_count++;
            const newElement = elementTemplate.cloneNode(true);
            const id_parts = newElement.querySelector('input').getAttribute('id').split('_');
            const id = id_parts.slice(0, -1).join('_') + '_' + String(item_count - 1);
            newElement.querySelector('input').setAttribute('id', id);
            newElement.querySelector('input').value = '';

            addRemoveEventListener(newElement);
            parentElement.appendChild(newElement);
        });
    });
});
