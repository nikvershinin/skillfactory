from django import template

register = template.Library()  # если мы не зарегистрируем наши фильтры, то Django никогда не узнает, где именно их искать и фильтры потеряются


@register.filter(name='censor')
def censor(value):
    arg = [
        'Какие то нецензурные слова',
        'Полипропилен'
    ]
    if isinstance(value, str):
        value = value.split(' ')
        new_value = []
        for i in value:
            if i in arg:
                j = len(i)-1
                i = '*' * j
            new_value.append(i)
        return str(" ".join(new_value))
