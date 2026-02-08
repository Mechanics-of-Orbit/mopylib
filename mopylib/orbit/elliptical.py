from ..utils.labels import label
from .orbit import Orbit

class Elliptical(Orbit):
    def __init__(self, semimajor_axis, eccentricity, inclination, right_ascension, argument_perigee, true_anomaly):
        super().__init__(semimajor_axis, eccentricity, inclination, right_ascension, argument_perigee, true_anomaly)
        self.orbit_type = label.OrbitType.ELLIPSE
        self.state_vector = []
        
    def __str__(self):
        return f"Orbit: {self.orbit_type}"