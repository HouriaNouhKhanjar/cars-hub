from django import template
import re

register = template.Library()


@register.filter
def cloudinary_optimize_car(url):
    """
    Inserts f_auto,q_auto right after 'upload/' in the Cloudinary URL.
    """
    return re.sub(r'/upload/', '/upload/c_fill,w_400,h_300/f_auto,q_auto/', url.replace("http://", "https://"))


@register.filter
def cloudinary_optimize_category(url):
    """
    Inserts f_auto,q_auto right after 'upload/' in the Cloudinary URL.
    """
    return re.sub(r'/upload/', '/upload/c_fill,w_300,h_200/f_auto,q_auto/', url.replace("http://", "https://"))
