import numpy as np
import matplotlib.pyplot as plt
rng = np.random.default_rng()


lmd = 0.5
n = 20000

#逆関数法
u = rng.uniform(size=n)
x = -np.log(1.0 - u)/lmd

#目標の確率密度関数
def f(x):
    ans = lmd*np.exp(-lmd*x)
    return ans

x_plt = np.linspace(0,15,10000)
pdf = f(x_plt)


#プロット
bins = np.linspace(0, 15, 100)
plt.plot(x_plt, pdf, label="expon(0.5)")
plt.hist(x, bins=bins, density=True, alpha=0.3, label="Generated Data")
plt.xlabel("x")
plt.ylabel("Density")
plt.legend()
plt.show()