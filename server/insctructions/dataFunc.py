from TimeTracker.models import Sites
from django.db.models.functions import ExtractWeekDay
from django.db.models import Avg
import datetime
import json
class DataInstruct():

    def get_minute(self, seconds):
        if seconds == 0:
            return 0
        else:
            min = (seconds / 60)
            return round(min, 1)

    def get_sec(self, time):
        """Get Seconds from time."""
        if time == 0:
            return int('0')
        else:
            h, m, s = time.split(':')
            return int(h) * 3600 + int(m) * 60 + int(s)

    def get_percentage(self, item, time_list):
        total = sum(time_list)
        return int((item*100)/total)

    def url_strip(self, url):
        if "http://" in url or "https://" in url:
            url = url.replace("https://", '').replace("http://",
                                                      '').replace('\"', '')
        if "/" in url:
            url = url.split('/', 1)[0]
        return url

    def convert_to_time(self, sec):
        try:       
            return str(datetime.timedelta(seconds=sec))
        except Exception as identifier:
            pass

    def get_week_days_data(self):
        data = Sites.objects.annotate(weekday=ExtractWeekDay('date')).values('weekday').annotate(avg=Avg('time')).values('weekday', 'avg')
        data = json.dumps(list(data))
        data  = json.loads(data)
        return data

    def CalculateTimeInstructions(self, mainUrl, userId, Time):
        userSites = Sites.objects.filter(user_id=userId).all()
        try:
            q = userSites.get(url__exact=mainUrl)
            q.time = q.time + int(Time)
            q.save()
        except Exception as err:
            newsite = Sites(
                url=mainUrl,
                user_id=userId,
                time=int(Time)
            )
            newsite.save()
