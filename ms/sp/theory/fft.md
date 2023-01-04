# 快速傅里叶变换

## $\C[G]$，$G$为有限群
```{prf:definition}
:label: def_finite_group_ftc
对于$f\in\C[G]$，我们定义其傅里叶系数为
\begin{equation}
c_f(\chi)\defeq<f,\chi>,\quad\forall\chi\in\hat{G}
\end{equation}
由此我们定义了以下的一个映射，$c$:

$$
c:\left\{
    \begin{array}{ccc}
    \C[G]&\longrightarrow&\C[\hat{G}]\\
    f&\longmapsto&c_f
    \end{array}
\right.
$$

```

通常，我们更习惯傅里叶变换而不仅仅是系数，其术语作相应的调整：
```{prf:definition} 傅里叶变换
:label: def_finite_group_ft
傅里叶变换$\mathcal{F}$定义为：
\begin{equation}
\mathcal F:\left\{
    \begin{array}{ccc}
    \C[G]&\longrightarrow&\C[\hat{G}]\\
    f&\longmapsto&\hat{f}
    \end{array}
\right.
\end{equation}
其中$\hat{f}$为$\hat{G}$的一个函数，即$\hat{f}\in\C[\hat{G}]$:
\begin{equation}
\hat{f}(\chi)\defeq|G|c_f(\bar{\chi})=\sum_{x\in G}f(x)\chi(x)
\end{equation}
```

态射$c$和$\mathcal{F}$明显是线性的，事实上，他们是从线性空间$\C[G]$到$\C[\hat{G}]$的一个同构态射：
```{prf:proposition} 傅里叶逆变换
对于$f\in\C[G]$，我们有以下的逆变换：
\begin{equation}
f=\sum_{\chi\in\hat{G}}c_f(\chi)\chi=\frac{1}{|G|}\sum_{\chi\in\hat{G}}\hat{f}(\chi)\chi^{-1}
\end{equation}
```

```{prf:proposition} 帕塞瓦尔恒等式
对于$f, g\in\C[G]$，我们有以下恒等式：
\begin{equation}
<f,g>=|G|<c_f,c_g>=\frac{1}{|G|}<\hat{f},\hat{g}>
\end{equation}
```

## 函数空间$\L^2(\R)$的傅里叶变换

## 连续与离散傅里叶变换的关系

There are two basic techniques for influencing how one can calculate, using the discrete transform, different values of the continuous transform.
- We can sample the signal with more or less precision. We have seen that the more precise the sampling is (that is to say the more points we take to represent the analyzed function), the wider the spectrum of the transform. Thus, if one wishes to cover a spectrum twice as large, it suffices to divide the interpolation interval by two. Of course, this also extends the time needed to do the math.
- You can add zeros at the end of the vector. If we are satisfied with the spectrum on which we calculate the transform (more precisely the maximum and minimum frequencies that we can calculate), we may then want to calculate the transform with more precision, for example if we want to draw a curve to graphically represent the transform. In this case, the procedure is simple: it suffices to add zeros at the end of the vector, to add as many calculated intermediate frequencies.

By playing on these two parameters (interpolation precision and addition of zeros), we can calculate “custom” discrete transforms, to have a certain fixed vector size (this can be used to create filters, see Section 4.2), but also for the representation of the transform. The figure 4.1 shows the different results that can be obtained by adjusting both the number of sampling points and the addition of zeros. The functions represented are the modules of the DFT of the indicator function of [0.5, 1], sampled on [0, 1] at regular intervals. Each row uses the same number of sample points, but with more or less zeros added. The exercise 41 is instructive in this regard, since it reinvests all of this in order to create and test a low-pass filter.


