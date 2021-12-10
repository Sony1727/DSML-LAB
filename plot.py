import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
x=[1,2,3,4,5,6,7,8,9,10]
y=[-20,-35,-30,-34,-50,-40,-45,-50,-55,-60]
plt.scatter(x,y,c='orange',s=100)
rel=np.corrcoef(x,y)
print(rel)
