from enum import Enum


class OrbitType(Enum):
    circular = 'Circular'
    elliptical = 'Elliptical'
    parabolic = 'Parabolic'
    hyperbolic = 'Hyperbolic'
    
class OrbitDirection(Enum):
    prograde = 'Prograde'
    retrograde = 'Retrograde'
    
class OrbitPhase(Enum):
    ascending = 'Ascending'
    descending = 'Descending'
    
class OrbitInclination(Enum):
    equatorial = 'Equatorial'
    polar = 'Polar'
    inclined = 'Inclined'

class TimeUnits(Enum):
    second = 's'
    minute = 'minute'
    hour = 'hour'
    day = 'day'
    year = 'year'
    julianYear = 'julian_year'