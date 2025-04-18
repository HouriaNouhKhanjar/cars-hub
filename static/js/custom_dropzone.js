document.addEventListener('DOMContentLoaded', function () {
    document.querySelectorAll('input[type="file"]').forEach(function(input) {
        const wrapper = document.createElement('div');
        wrapper.classList.add('dropzone-wrapper');
        const dropzone = document.createElement('div');
        dropzone.classList.add('dropzone-box');
        dropzone.innerText = 'Drag & Drop an image or click to upload';
        input.parentNode.insertBefore(wrapper, input);
        wrapper.appendChild(dropzone);
        wrapper.appendChild(input);
        input.style.opacity = 0;

        dropzone.addEventListener('click', () => input.click());

        dropzone.addEventListener('dragover', e => {
            e.preventDefault();
            dropzone.classList.add('hover');
        });

        dropzone.addEventListener('dragleave', () => {
            dropzone.classList.remove('hover');
        });

        dropzone.addEventListener('drop', e => {
            e.preventDefault();
            input.files = e.dataTransfer.files;
            dropzone.classList.remove('hover');
        });
    });

    document.querySelectorAll('.inline-related').forEach(function (inlineForm) {
        const deleteInput = inlineForm.querySelector('input[name$="-DELETE"]');

        if (deleteInput) {
            const btn = document.createElement('div');
            btn.className = 'delete-btn';
            btn.innerText = 'Delete Image';

            btn.addEventListener('click', function () {
                const confirmDelete = confirm("Are you sure you want to delete this image?");
                if (confirmDelete) {
                    deleteInput.checked = true;
                    inlineForm.style.opacity = 0.5;
                    inlineForm.style.pointerEvents = 'none';
                }
            });

            inlineForm.appendChild(btn);
        }
    });
});
  