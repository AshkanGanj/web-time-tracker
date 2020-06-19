from django import template

import datetime

register = template.Library()


def convert_to_time(sec):
    if sec !=0:
        return str(datetime.timedelta(seconds=sec))
    else:
        pass
    
register.filter(convert_to_time)