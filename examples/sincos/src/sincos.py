"""sincos"""
import math
import time
from kogu import Kogu

# defaults are not really necessary
# but allows to skip their definition in parameters
iterations = 10
step_size = 0.5
amplitude = 2
phase = 0

Kogu.load_parameters()

print("Hyperparameters")
print("===============")
print("iterations:", iterations)
print("step_size:", step_size)
print("amplitude:", amplitude)
print("phase:", phase)

Kogu.send_hyperparameters(
    ["iterations", "step_size", "amplitude", "phase"],
    [iterations, step_size, amplitude, phase])

Kogu.plot(plot_type="line", y_label="sin", series=["sin"], name="Sine")

for i in range(iterations):
    angle = step_size*i
    cos = amplitude*math.cos(angle + phase)
    sin = amplitude*math.sin(angle + phase)
    score = sin + cos
    Kogu.metrics(
        ["angle", "sin", "cos"],
        [angle, sin, cos], i)
    time.sleep(0.1)

Kogu.metrics("score", score)
