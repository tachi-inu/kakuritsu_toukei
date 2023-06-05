import numpy as np
import matplotlib.pyplot as plt
from scipy import stats as st
rng = np.random.default_rng()


n = 20000  # サンプル数

#ガンマ関数の確率密度関数(k=4, theta=1)
def gamma(x):
    ans = (x**3) * np.exp(-x) / 6
    return ans


def rejection_sampling(n):
    samples = []
    while len(samples) < n:
        u = rng.uniform(0, 1)
        v = st.cauchy.rvs()
        hv = 1/(v**2 + 1)
        if u <= gamma(v)/(5*hv) and v>0:
            samples.append(v)  # 棄却法によりサンプルを受け入れる
    return samples


# ガンマ分布のサンプル生成
samples = rejection_sampling(n)


x_plt = np.linspace(0,15,10000)
pdf = gamma(x_plt)


# ヒストグラムをプロット
plt.plot(x_plt, pdf, label="gamma(4,1)")
plt.hist(samples, bins=100, density=True, alpha=0.3, label='Generated Data')
plt.xlabel('V')
plt.ylabel('Density')
plt.legend()
plt.show()