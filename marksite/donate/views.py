# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import random

from django.views.generic.base import TemplateView

class DonateView(TemplateView):

    template_name = "donate.html"
    
    def loop_times(self):
        return range(1, len(self.choose_candle())+1 )
    
    def choose_candle(self):
        blue = '/images/blue-candle.gif'
        red  = '/images/red-candle.gif'
        
        candles = [
            red, blue, red, red, red,
            blue, red, blue, red, blue,
            blue, red, red, red, blue,
            red, blue, blue, red, red,
            blue, red, red, red, red,
        ]
        return candles
