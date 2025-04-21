from django.forms.widgets import ClearableFileInput
from django.utils.safestring import mark_safe

class DragAndDropWidget(ClearableFileInput):
    class Media:
        css = {
            'all': ('css/custom_dropzone.css',)
        }
        js = ('js/custom_dropzone.js',)

    def render(self, name, value, attrs=None, renderer=None):
        input_html = super().render(name, value, attrs)
        
        preview_html = ''
        if value and hasattr(value, 'url'):
            preview_html = f'''
                <div class="existing-preview">
                    <img src="{value.url}" alt="Current Image" class="preview-image w-100"/>
                </div>
            '''

        return mark_safe(f"""
            <div class="custom-dropzone-wrapper">
                {preview_html}
                <div class="custom-dropzone-box">Drag & Drop an image or click to upload</div>
                {input_html}
                <div class="image-preview-container"></div>
            </div>
        """)