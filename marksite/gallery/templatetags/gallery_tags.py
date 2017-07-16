from django import template
from photologue.models import Photo, Gallery

register = template.Library()

@register.inclusion_tag('tags/next_in_gallery.html')
def next_in_gallery(photo, gallery):
    photo = photo.get_next_in_gallery(gallery)
    return {'photo': photo, 'gallery': gallery}

@register.inclusion_tag('tags/prev_in_gallery.html')
def previous_in_gallery(photo, gallery):
    photo = photo.get_previous_in_gallery(gallery)
    return {'photo': photo, 'gallery': gallery}    
