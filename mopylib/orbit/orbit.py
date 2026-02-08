from dataclasses import dataclass

from ..utils.labels import label
from ..utils import Units

@dataclass
class Orbit:
    semimajor_axis: float
    eccentricity: float
    inclination: float
    right_ascension: float
    argument_perigee: float
    true_anomaly: float
    
    orbit_type: label.OrbitType
    
    # cartesian coordinates
    state_vector: list

    def __post_init__(self):
        pass
    
    def __str__(self):
        return f"Orbit: {self.orbit_type}"

    def constants_of_motion(self):
        self.angular_momentum = self.semimajor_axis * (1 - self.eccentricity**2)**0.5
        self.specific_mechanical_energy = 1