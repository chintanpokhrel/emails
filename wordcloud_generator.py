from os import path
from scipy.misc import imread
import matplotlib.pyplot as plt
import random

from wordcloud import WordCloud

import sys

from analyze_email import Analyzer
a = Analyzer(sys.argv[1])
top = a.filter(int(sys.argv[2]))

wordcloud = WordCloud(font_path='/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf',
			relative_scaling = 1.0,
			stopwords = {}
			).generate(' '.join(top.keys()))
plt.imshow(wordcloud)
plt.axis("off")
plt.show()
