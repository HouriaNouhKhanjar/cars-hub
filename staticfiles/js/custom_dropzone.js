document.addEventListener('DOMContentLoaded', function () {
    document.querySelectorAll('input[type="file"]').forEach(function(input) {
        const wrapper = input.closest('.custom-dropzone-wrapper');
        const dropzone = wrapper.querySelector('.custom-dropzone-box');
        const previewContainer = wrapper.querySelector('.image-preview-container');

        dropzone.addEventListener('click', () => input.click());

        const showPreview = file => {
            const reader = new FileReader();
            reader.onload = e => {
                previewContainer.innerHTML = `
                    <img src="${e.target.result}" class="preview-image"/>
                `;
            };
            reader.readAsDataURL(file);
        };

        input.addEventListener('change', () => {
            if (input.files && input.files[0]) {
                showPreview(input.files[0]);
            }
        });

        dropzone.addEventListener('dragover', e => {
            e.preventDefault();
            dropzone.classList.add('hover');
        });

        dropzone.addEventListener('dragleave', () => {
            dropzone.classList.remove('hover');
        });

        dropzone.addEventListener('drop', e => {
            e.preventDefault();
            dropzone.classList.remove('hover');
            const file = e.dataTransfer.files[0];
            input.files = e.dataTransfer.files;
            if (file) {
                showPreview(file);
            }
        });
    });
    document.querySelectorAll('.inline-related').forEach(function (inlineForm) {
        const deleteInput = inlineForm.querySelector('input[name$="-DELETE"]');

        if (deleteInput) {
            // Hide the default checkbox
            deleteInput.style.display = 'none';

            // Create a new delete button
            const btn = document.createElement('button');
            btn.type = 'button';
            btn.className = 'btn btn-sm btn-danger delete-image-btn';
            btn.innerText = 'Delete Image';

            // Confirmation and mark for delete
            btn.addEventListener('click', function () {
                if (confirm("Are you sure you want to delete this image?")) {
                    deleteInput.checked = true;
                    inlineForm.style.opacity = 0.5;
                    inlineForm.style.pointerEvents = 'none';
                }
            });

            // Append the button
            inlineForm.appendChild(btn);
        }
    });
});