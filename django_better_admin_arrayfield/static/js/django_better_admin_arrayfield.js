window.addEventListener('load', function () {

    function addRemoveEventListener(widgetElement) {
        widgetElement.querySelectorAll('.remove').forEach(function (element) {
            element.addEventListener('click', function () {
                var array_items = this.parentNode.parentNode.childElementCount;
                if (array_items == 1) {
                    this.parentNode.querySelector('input').value = '';
                }
                else {
                    this.parentNode.remove();
                }
            });
        });
    }

    document.querySelectorAll('.dynamic-array-widget').forEach(function (widgetElement) {

        var inititalElement = widgetElement.querySelector('.array-item');
        var elementTemplate = inititalElement.cloneNode(true);
        var parentElement = inititalElement.parentElement;

        addRemoveEventListener(widgetElement);

        widgetElement.querySelector('.add-array-item').addEventListener('click', function () {
            var newElement = elementTemplate.cloneNode(true);
            var id_parts = newElement.querySelector('input').getAttribute('id').split('_');
            var id = id_parts.slice(0, -1).join('_') + '_' + String(parseInt(id_parts.slice(-1)[0]) + 1);
            newElement.querySelector('input').setAttribute('id', id);
            newElement.querySelector('input').value = '';

            addRemoveEventListener(newElement);
            parentElement.appendChild(newElement);
        });

    });

});
