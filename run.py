from mopylib.mathematics import Time
from mopylib.utils.labels import label

t = Time()

print(t.time_vars)
print(t.units)
t.convert_to(label.TimeUnits.hour)
print(t.time_vars)
print(t.units)
