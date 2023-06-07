from django import template


register = template.Library()

'''Реализовано просто наглядно и очень специфично.
Для нежелательных слов, конечно желательно, завести список и вынести в отдельный файл 
и заменять слова по индексам и срезам'''


@register.filter()
def censor(value):
    if 'twitter' in value.lower():
        return value.replace('Twitter', 'Twitter'[0] + '******')
    elif 'instagram' in value.lower():
        return value.replace('Instagram', 'Instagram'[0] + '********')
    else:
        return value
