# 信号空间
这里信号指的是时间序列，我们的目标是界定信号具体的数学模型。

我们用$G$代表时间域, 相应的值域中的一个元素（也就是我们的具体的一个时间序列样本）$f$可以看成是从$G$到$\mathbb C$的一个映射，即$f:G\longrightarrow\mathbb C$，其中$\mathbb C$是所有复数的集合。我们用符合$\mathbb{C}(G)$代表值域，这就是我们的信号空间。这个空间太过宽泛，为了便于分析，我们需要加一些结构，也就是加些法则和条件。

（signal_space_finite_group）=
## 有限群时间域$G$
信号空间模型：$\mathbb{C}(G)$，$G$为有限群。
### 基数
我们用$|G|$代表基数（cardinal），也就是$G$中元素的个数。

### 内积
内积用符合$<\cdot,\cdot>$表示：

$$<x,y>\mathrel{\overset{\scriptstyle\Delta}{=}}\frac{1}{|G|}\sum_{g\in G}x(g)\overline{y(g)}, \quad\forall x,y\in\mathbb{C}(G)$$

### 范数
范数$||\cdot||_2$则是

$$||x||_2^2\mathrel{\overset{\scriptstyle\Delta}{=}<x,x>}$$

### 基
```{prf:proposition}
$\mathbb{C}(G)$的一组基由$\{\delta_g\}_{g\in G}$构成：

$$\delta_g(h)\mathrel{\overset{\scriptstyle\Delta}{=}\left\{
    \begin{aligned}
    1 & \quad\textrm{if}\quad h=g\\
    0 & \quad\textrm{if}\quad h\neq g
    \end{aligned}
\right.}$$
```

## 周期性信号空间$\ell^2(\mathbb{Z}/N\mathbb{Z})$
$G=\mathbb{Z}/N\mathbb Z,\quad|G|=N$是[有限群]（signal_space_finite_group）的特例，有限群的一个具体模型。

## $\ell^2(\mathbb Z)$

## $\mathbb{L}^2(\mathbb R)$