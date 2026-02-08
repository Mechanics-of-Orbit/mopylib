from dataclasses import dataclass
from scipy.constants import gravitational_constant, kilo

from ..utils.labels import label


@dataclass
class Time:
    """_summary_

    :raises ValueError: _description_
    """
    units: label.TimeUnits = label.TimeUnits.second
    
    minute = 60.0
    hour = 60 * minute
    day = 24 * hour
    week = 7 * day
    year = 365 * day
    julian_year = 365.25 * day
    
    
    def __post_init__(self):
        self.time_vars = [self.minute, self.hour, self.day, self.week, self.year, self.julian_year]
    
    def convert_to(self, new_units: label.TimeUnits):
        if not isinstance(new_units, label.TimeUnits):
            raise ValueError("new_units must be a label.TimeUnits")
        
        if new_units == self.units:
            return
        
        self.time_vars = [t / getattr(self, new_units.value) for t in self.time_vars]
        self.minute, self.hour, self.day, self.week, self.year, self.julian_year = self.time_vars
        self.units = new_units
        
        
        
            
        


IVECTOR = [1, 0, 0]
JVECTOR = [0, 1, 0]
KVECTOR = [0, 0, 1]

NEWTON_GRAVITATIONAL_CONSTANT = gravitational_constant * kilo**-3 #units are in km3 kg-1 s-2

