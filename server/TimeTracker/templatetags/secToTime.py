from django import template

import datetime

register = template.Library()


def convert_to_time(sec):
    return str(datetime.timedelta(seconds=sec))

register.filter(convert_to_time)