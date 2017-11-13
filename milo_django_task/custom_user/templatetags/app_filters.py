from datetime import date
from django import template


register = template.Library()


@register.filter(name='is_eligible')
def is_eligible(value):
    today = date.today()
    return 'allowed' if ((today.year-value.year)
                         - int((today.month, today.day) < (value.month, value.day))) > 13 else 'blocked'


@register.filter(name='bizzfuzz')
def bizzfuzz(value):
    if value % 3 == 0:
        return 'Bizz'
    elif value % 5 == 0:
        return 'Fuzz'
    elif value % 3 == 0 and value % 5 == 0:
        return 'BizzFuzz'
    else:
        return value
