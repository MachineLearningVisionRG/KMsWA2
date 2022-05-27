from insertion_KMs import insertion_KMs
import numpy as np
from PIL import Image


# ------------------- Parameters -----------------------------
p1 = 0.1
p2 = 0.5
delta = 500  # Embedding Strength
numbits = 200  # Numbers of bits inserted in watermarked image
order = 32
# -------------------------------------------------------------
image = np.array(Image.open('images/Pneumonia.png'))
bits = np.random.choice([0, 1], size=(1000,))
insertion_KMs(image, bits, order, delta, p1, p2, numbits)

