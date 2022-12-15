# Wavelet
这里是对信号理论的教科书《The Wavelete Tour of Signal Processing: The Sparse Way, by Stephane Mallat》的导读。看了不少的材料，最终还是觉得这本书的描述比较全面和深入。其缺陷有两个，其一，是缺少了离散空间算法程序实现的设计与梳理；另外就是没有以自适应性(adaptivity)作为其中一个主要的脉络进行阐述（当然，作者本身可能是默认了自适应性的必要性，因为the spase way就是自适应性的一种系统性的方法）。这两点都可以从另外一本早期关于小波理论的书《Adapted Wavelet Analysis from Theory to Software, by Mladen Victor Wickerhauser》中得到一些补充，尤其是第一点。

总体来说，Mallat的书是关于现代信号处理从理论到实践上比较全面的介绍，而Wickerhauser的书是对算法的程序实现上不可多得的梳理。

这个导读侧重两个方面：
1. 理论上脉络的导读
2. 算法上和一些关键的概念与python的程序包的使用进行对标，其中的程序包包括pywt，scaleogram，scipy.signal等。

如果时间允许的话，我也希望能够对小波算法的程序设计与实现进行有系统的梳理，这里包括基础的算子识别与设计，用软件工程的思路来实现算法，尤其包括online算法。