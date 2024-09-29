import configurator
class basehard():
    def time(self,_pass,fail,score):return 1
time_max_spawn="time max spawn"
time_min_spawn="time min spawn"
speed_max_to_min="speed max to min"
multiplier_pass ="multiplier pass"
multiplier_fail ="multiplier fail"
multiplier_score="multiplier score"
class hyperbole(basehard):
    def __init__(self,conf:configurator.configurator):
        self.min=1-conf.get(time_min_spawn,0.5)
        self.max=conf.get(time_max_spawn,2)+self.min
        self.max_to_min=conf.get(speed_max_to_min,0.5)

        self.multiplier_pass =conf.get(multiplier_pass ,1)
        self.multiplier_fail =conf.get(multiplier_fail ,1)
        self.multiplier_score=conf.get(multiplier_score,0.05)
    def time(self,_pass,fail,score):
        _pass=self.multiplier_pass*_pass
        fail=self.multiplier_fail*fail
        score=score*self.multiplier_score
        er=(_pass+fail+score)**(self.max_to_min)/4
        result=(er+self.max)/(er+1)-self.min
        return result
def get_type_colculate_of_text(text,conf) ->basehard:
    if text==hyperbole.__name__:
        return hyperbole(conf)
