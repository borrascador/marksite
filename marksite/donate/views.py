# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import random

from django.views.generic.base import TemplateView

class DonateView(TemplateView):

    template_name = "donate.html"
    
    def loop_times(self):
        return range(1,21)
    
    def choose_candle(self):
        candles = [
            '/images/candle-blue.png',
            '/images/candle-red.png',
        ]
        return random.choice(candles)
