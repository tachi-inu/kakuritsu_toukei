import numpy as np
import matplotlib.pyplot as plt
from scipy import stats as st
rng = np.random.default_rng()

n=100000
u = st.uniform.rvs(size=n)
xx = [] #結果の格納用配列
x = 2   #初期値

def gamma(x):
    ans = (x**3) * np.exp(-x) / 6
    return ans


for t in range(n):
    v = x + st.uniform.rvs() - 0.5
    a = gamma(v)/gamma(x)
    if u[t] <= a:
        x = v
    xx.append(x)

x_plt = np.linspace(0, 20, 10000)
pdf = gamma(x_plt)
plt.plot(x_plt, pdf, label="gamma(4,1)")
plt.hist(xx[1000:], bins=200, density=True, alpha=0.3, label="Generated Data")
plt.legend()
plt.show()