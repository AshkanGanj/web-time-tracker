from django.db.models import Sum, Avg, Max, Min
from TimeTracker.models import Sites
from datetime import datetime
from .dataFunc import DataInstruct




class Aggregators():

    def __init__(self, user_id):
        self.now = datetime.now()
        self.date = self.now.strftime("%Y-%m-%d")
        self.userSites = Sites.objects.filter(
            user_id=user_id, date=self.date).all()

    def get_data(self, query, agg):
        time = DataInstruct()
        url = self.userSites.filter(time=query['time__{}'.format(agg)])
        m = ""
        for i in url:
            m = i.url

        data = {
            "url": m,
            "agg": time.convert_to_time(query['time__{}'.format(agg)])
        }
        return data

    def max(self):
        q = self.userSites.aggregate(Max('time'))
        return self.get_data(q, 'max')

    def min(self):
        q = self.userSites.aggregate(Min('time'))
        return self.get_data(q, 'min')

    def average(self):
        q = self.userSites.aggregate(Avg('time'))
        return self.get_data(q, 'avg')

    def sum(self):
        q = self.userSites.aggregate(Sum('time'))
        return self.get_data(q, 'sum')

