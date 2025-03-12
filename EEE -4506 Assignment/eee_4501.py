# -*- coding: utf-8 -*-
"""EEE-4501.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Lxhwr4AyVJAogOh7qcE-DZp3FXryrLZb
"""

import numpy as np
import matplotlib.pyplot as plt

# ডেটা তৈরি
x = np.arange(0, 10.1, 0.1)
y1 = np.sin(x)
y2 = np.cos(x)
y3 = np.tan(x)
y4 = np.exp(-x)

# ফিগার তৈরি
fig, axs = plt.subplots(2, 2, figsize=(10, 8))

# প্রথম subplot (Sin(x))
axs[0, 0].plot(x, y1)
axs[0, 0].set_title('Sin(x)')

# দ্বিতীয় subplot (Cos(x))
axs[0, 1].plot(x, y2)
axs[0, 1].set_title('Cos(x)')

# তৃতীয় subplot (Tan(x))
axs[1, 0].plot(x, y3)
axs[1, 0].set_ylim(-10, 10)  # ট্যান ফাংশনের মান সীমাবদ্ধ করা
axs[1, 0].set_title('Tan(x)')

# চতুর্থ subplot (Exp(-x))
axs[1, 1].plot(x, y4)
axs[1, 1].set_title('Exp(-x)')

# গ্রাফের মধ্যে ফাঁক সংযোজন
plt.tight_layout()
plt.show()