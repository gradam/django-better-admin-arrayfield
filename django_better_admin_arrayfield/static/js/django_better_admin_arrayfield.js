window.addEventListener('load', function () {

    function addRemoveEventListener(widgetElement) {
        widgetElement.querySelectorAll('.remove').forEach(function (element) {
            element.addEventListener('click', function () {
                this.parentNode.remove();
            });
        });
    }

    document.querySelectorAll('.dynamic-array-widget').forEach(function (widgetElement) {

        addRemoveEventListener(widgetElement);

        widgetElement.querySelector('.add-array-item').addEventListener('click', function () {
            var first = widgetElement.querySelector('.array-item');
            var newElement = first.cloneNode(true);
            var id_parts = newElement.querySelector('input').getAttribute('id').split('_');
            var id = id_parts.slice(0, -1).join('_') + '_' + String(parseInt(id_parts.slice(-1)[0]) + 1);
            newElement.querySelector('input').setAttribute('id', id);
            newElement.querySelector('input').value = '';

            addRemoveEventListener(newElement);
            first.parentElement.appendChild(newElement);
        });

    });

});
