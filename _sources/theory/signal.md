# 信号空间
这里信号指的是时间序列，我们的目标是界定信号具体的数学模型。

我们用$G$代表时间域, 相应的值域中的一个元素（也就是我们的具体的一个时间序列样本）$f$可以看成是从$G$到$\mathbb C$的一个映射，即$f:G\longrightarrow\C$，其中$\C$是复数域。我们用符合$\C(G)$代表这个信号空间。

这个空间太过宽泛，为了便于分析，我们需要加一些结构，也就是加些法则和条件。

(signal:space:finitegroup)=
## $\C[G]$，有限群时间域$G$
信号空间模型：$\mathbb{C}(G)$，$G$为有限群。
### 基数
我们用$|G|$代表基数（cardinal），也就是$G$中元素的个数。

### 内积
内积用符合$<\cdot,\cdot>$表示：

$$<x,y>\mathrel{\overset{\scriptstyle\Delta}{=}}\frac{1}{|G|}\sum_{g\in G}x(g)\overline{y(g)}, \quad\forall x,y\in\C[G]$$

### 范数
范数$||\cdot||_2$则是

$$||x||_2^2\mathrel{\overset{\scriptstyle\Delta}{=}<x,x>}$$

### 基
```{prf:proposition}
:label: delta_representation
$\C[G]$的一组基由$\{\delta_g\}_{g\in G}$构成：

$$\delta_g(h)\mathrel{\overset{\scriptstyle\Delta}{=}\left\{
    \begin{aligned}
    1 & \quad\textrm{if}\quad h=g\\
    0 & \quad\textrm{if}\quad h\neq g
    \end{aligned}
\right.}$$

即
\begin{equation}
f=\sum_{g\in G}f(g)\delta_g,\quad\forall f\in\C[G]
\end{equation}
由此，$\C[G]$是$\C$上的一个向量空间（vector space）并且维度为$|G|$。
```

### 特征与对偶群
{prf:ref}`delta_representation`在理论上意义不大，因为这组基对符号运算有些帮助，但没有揭示群的内在结构。这就使得人们去寻找更有效的表达方式。有效性主要体现在两个方面：
1. 使用这种表达能够方便推演。
2. 这种表达能体现出群的内在结构与性质。

```{prf:definition} 特征与对偶群
$G$为一个有限群，特征（character）$\chi$是由$G$到$(\C,*)$的态射（morphism），其中$(\C,*)$是一个由复数域$\C$和乘积算子$*$构成的群（我们通常用$\C^*$表示），也就是说

$$\chi_1\chi_2:g\in G\longmapsto\chi_1(g)\chi_2(g)，\quad\forall\chi_1,\chi_2\in\hat{G}。$$

我们用符号$\hat{G}$代表特征集合，这个集合就叫做$G$的对偶。
```

以下命题彰显了对偶群的性质，也是通过代数结构对离散傅里叶变换最好的解释。
```{prf:proposition}
:label: finitegroup_dual
假设$G$的基数为$n\in\N$，即$|G|=n$，那么其对偶群的元素一定是某个单位圆的根：
\begin{equation}
\U_n=\left\{\left.\exp\left(\frac{2ik\pi}{n}\right)\right|0\leq k<n\right\}
\end{equation}
而且，

$$\forall g\in G,\quad|\chi(g)|=1,\quad\chi(g^{-1})=\chi(g)^{-1}=\overline{\chi(g)}$$

其中$|\cdot|$和$\overline{\cdot}$分别是复数的模（modulus）和共轭（conjugate）。也就是$\forall\chi\in\hat{G}, \chi\in\U_n$。
```

## 周期性信号空间$\C[\Z/n\Z]$
$G=\Z/n\Z,\quad|G|=n$是[有限群](signal:space:finitegroup)的特例，时间域的一个具体模型。这是周期信号空间的不二之选，它具备所有以上$\C[G]$的代数结构和分析工具。

在有限周期群（finite cyclic group）情况下，我们有
```{prf:proposition}
:label: finite_cyclic_group_dual

1. $G\simeq\hat{G}$，即$G$与$\hat{G}$同构。
2. $\hat{G}$是$\C[G]$的一组归一化正交基（orthonormal basis）。

```
由{prf:ref}`finitegroup_dual`，$\U_n$是$\C[\Z/n\Z]$的一组归一化正交基。

```{note}
{prf:ref}`finite_cyclic_group_dual`可以推广到有限可互换群（finite abelian group）。
```

## $\ell^2(\Z)$
因为$(\Z,+)$是一个可交换群（abelian group），从有限群的结构我们可以猜想到其对偶群是$\T\defeq\{z\in\C: |z|=1\}$

For a locally compact abelian group $G$, the *Pontryagin* dual is the group $\hat{G}$ of continuous group homomorphisms from $G$ to the circle group $\T$. That is,

$$\hat{G}\defeq \textrm{Hom}(G,\T)$$

## $\L^2(\R)$