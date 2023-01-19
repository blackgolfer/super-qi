---
jupyter:
  jupytext:
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.3'
      jupytext_version: 1.14.1
  kernelspec:
    display_name: Python 3 (ipykernel)
    language: python
    name: python3
---

# 导言


这一部分是关于信号处理技术的工程实现。

工程实现依赖于有效的单元操作。单元操作分两大类：其一是算法的单元操作；其二是编程技巧的单元操作。

算法的单元操作也分两类，第一类是基本常见的单元操作，比如`shift`，`decimatioin`；另外一类是算法本身的单元操作，比如`lct`中的折叠算子。从某种意义上说，一个算法就是一个单元操作的集合与串通这些单元操作的逻辑。所以，算法上对单元操作的思考和掌控一般都比较严密，也因此比较到位。

编程技巧上对单元操作的梳理也是比较丰富的，遗憾的是由于只要动手，一般都会比较快地得到结果，因此在单元操作的设计比较容易被忽视，这是我们在工作中需要重视的。

在大的框架上的编程技巧有以下几类：
1. Python data model
2. Object oriented programming (oop)
   - 抽象类（abstract class）与具体类（concrete class）
   - traits和mixin
3. 对象的可变更性（mutable）与不可变更性（immutable）
4. 函数式（functional programming）
   - 容器（container）：对特定对象的一个封装。用信号的作为例子，信号是数组的一个容器，
   - functor：一种特殊的容器，其中定义了`fmap`函数，其作用是应用外部定义的函数`f`（也就是`fmap`的输入参数）作用于被封装的类，并且将作用的结果用同样的容器封装起来作为`fmap`的输出。假设被封装的对象是类型`A`，`f`作用于对象的结果类型是`B`，即，`f: A->B`，那么`fmap: f->F[B]`，`F`为functor类型，`F[B]`指的是含有类型`B`的`F`functor。
   - monad：在functor的基础上加上`bind`函数。用`M`代表一个monad的类型，跟`fmap`不同在于，`bind`要求输入参数`f`为`A->M[B]`的函数，`bind`的返回值为`M[B]`类型，而且是直接返回`f`的返回值。
   
更底层的技巧依赖于数据结构的经验，常用的有二叉树等。


## Python collections 与 data model
这段资料取自于{cite}`ramalho2015fluent`的第一章。这里简单介绍`collections`和data model，是我们常用的工具。


### collections

```python
import collections

Card=collections.namedtuple('Card', ['rank', 'suit'])
```

```python
Card('2','spades')
```

## data model
我们用一个模拟扑克牌的案例来说明data model的用法，定义一个类叫`FrenchDeck`：

```python
class FrenchDeck:
    ranks = [str(n) for n in range(2,11)]+list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()
    
    def __init__(self):
        self._cards=[Card(rank,suit) for suit in self.suits
                                    for rank in self.ranks]
        
    def __len__(self):
        return len(self._cards)
    
    def __getitem__(self,position):
        return self._cards[position]
```

`FrenchDeck`比较简单，但功能强大。这是因为用了特殊函数`__len__`和`__getitem__`。下面来说明其主要功能。


### `__len__`
`__len__`的功能是返回纸牌的个数。

`FrenchDeck`中，唯一一个成员就是`_cards`，用`list comprehension`的方法（以上程序第6行）生成，因此是collection中的一个类。`__len__`是应用`len`函数于这个成员，算出成员里面元素的个数，也就是纸牌的个数。

```python
deck=FrenchDeck()
len(deck)
```

当函数`len`作用于`deck`，系统中是委托`FrenchDeck`中的特殊函数`__len__`来实现。


### `__getitem__`
定义这个特殊类方法使得`FrenchDeck`具备以下功能：
1. 支持slicing：这是因为我们在`__getitem__`中委托算子`[]`进行对类成员`_cards`的指针操作。因为`_cards`的类型是`list`，这种简练的委托，使得`FrenchDeck`变成了像`list`数据结构。
2. 使得`FrenchDeck`成为*iterable*，这样许多python中适用于*iterable*的程序库能被应用于`FrenchDeck`。

值得强调的是，`FrenchDeck`的实现不是通过继承的方式，更多的是一种组合的方式来实现。这是*data model*非常重要的特征。


#### 类`list`
抽取第`n`张纸牌，`n`的方式与`list`一样，如下`deck[0]`为第一张纸牌，`deck[-1]`为最后一张纸牌：

```python
deck[0]
```

```python
deck[-1]
```

通过调用`random.choice`，使得`FrenchDeck`支持随机抽取纸牌的功能：

```python
from random import choice

choice(deck)
```

支持*slicing*:

```python
deck[0:3]
```

```python
deck[12::13]
```

#### *iterable*

```python
for i,j in zip(range(len(deck)),deck):
    if i>4:
        break
    print(j)
```

```python
for i,j in zip(range(len(deck)),reversed(deck)):
    if (i<4):
        print(j)
    else:
        break
```

```python
Card('Q', 'hearts') in deck
```

我们来看看排序功能：

```python
suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)

def spades_high(card):
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(suit_values) + suit_values[card.suit]
```

```python
for i,card in zip(range(len(deck)),sorted(deck, key=spades_high)):
    if i<6:
        print(card)
    else:
        break
```

## traits和mixin的案例
这个案例来自于文章[Higher-Order Mixin Classes, or "Traits, but not quite!"](https://web.archive.org/web/20161009062141/http://stupid-python-tricks.blogspot.com/2015/04/computed-properties-and-higher-order.html)，所用到的技巧非常漂亮。

对于颜色，定义一个trait，通过函数的形式来生成trait类。用到匿名类`Inner`，配合`setattr`以及`property`两个函数的使用来设定匿名类的参数。

```python
def HasColor(name, default=None, doc=None):
    """
    Return an anonymous class that has a color property
    named `name`, with a default value of `default` and
    a docstring of `doc`.
    """

    propname = "__color_{}".format(name)
    colors = {
        "black": 0x00000000,
        "white": 0x00ffffff,
        "red":   0x00ff0000,
        "green": 0x0000ff00,
        "blue":  0x000000ff
    }

    def getter(self):
        return getattr(self, propname, default)

    def setter(self, value):
        if isinstance(value, int):
            if isinstance(value, bool):
                raise TypeError("integer colors must be ints")

            if value < 0 or value > 0x00ffffff:
                raise ValueError("integer colors must be 24-bit")

            setattr(self, propname, value)

        elif isinstance(value, str):
            if value not in colors:
                raise ValueError("unknown color '{}'".format(value))

            setattr(self, propname, colors[value])

        else:
            raise TypeError("color specifications must be ints or strs")


    class Inner:
        pass

    setattr(Inner, name, property(getter, setter, None, doc))
    return Inner
```

使用trait来组装下面的`Canvas`和`Button`，这样的组装方式显得非常灵活，合理，这就是mixin的概念：

```python
class GraphicsObject: # The base class of our hierarchy.
    pass

class Canvas(GraphicsObject,
            HasColor("foreground"),
            HasColor("background")):
    pass

class Button(Canvas, # Inherit Canvas's foreground and background.
             HasColor("border"),
             HasColor("text")):
    pass
```

```python
c = Canvas()
c.foreground = 'red'

b = Button()
b.foreground = 'black'
b.text = 'green'

```

```python
print("canvas foreground:",hex(c.foreground))
print("button foreground:",hex(b.foreground))
print("button text:",hex(b.text))
```

## 不可变更（immutable）类
### 类的隐私参数
类的隐私参数通过在参数名加前缀`__`来实现：

```python
class foo:
    def __init__(self,v):
        self.__v=v

    def __repr__(self):
        return str(self.__v)
f1=foo(3)
```

```python
#print(f1.__v)会产生错误：AttributeError: 'foo' object has no attribute '__v'
```

```python
print(f1)
```

### 如何实现类的不可变更性
通过屏蔽掉类的`__setattr__`和`__delattr__`特殊函数，我们可以达到准不可变更类。下面的案例分析，从中可以看到我们为什么用”准“这个词。

```python
import inspect

class Immutable(object):
    """Inherit this class to make the child class immutable"""
    def __setattr__(self, *args):
        if inspect.stack()[1][3] == '__init__':
            object.__setattr__(self, *args)
        else:
            raise TypeError('Cannot modify Immutable instance')

    __delattr__=__setattr__
```

```python
class foo(Immutable):
    def __init__(self,data):
        self.__data=data
    
    def __repr__(self):
        return str(id(self.__data))
    
    def __getitem__(self,p):
        return self.__data[p]
    
    def __setitem__(self,p,v):
        self.__data[p]=v
```

```python
foo1=list(range(4))
foo2=foo(foo1)
print(foo2,id(foo1))
```

```python
foo2[1]='s'
for i in foo2:
    print(i)
```

```python
for i in foo1:
    print(i)
```

这里我们看到以下非常重要的几点：
1. 数组作为类构造函数的输入参数是按pass by reference来进行，这里的foo1就是被pass by reference，因为foo1的`id`值跟`foo`里面`__data`的`id`值是一样的；同时我们也看到`foo2`中`__data[1]`改成字符`s`后，`foo1[1]`也相应改成了`s`。
2. 虽然类`foo`继承了`Immutable`，屏蔽了对类参数的更改，这只是限制了对`__data`的更改，并不能限制`__data`内容的更改，也就是对参数的更改与对参数内容的更改是两个不同的概念。
3. 真正能够让一个继承`Immutable`类成为绝对不可更改，必须要求类参数本身也是不可更改的类。
4. 在没有声称`__setitem__`的情况下，作为`Immutable`的子类，外部对`foo`确实是没有更改的途径。对`foo`内部参数`__data`内容的更改只能在`foo`内部进行，这在一定程度上实现了不可更改性。


## Monad案例

```python
from typing import Generic, TypeVar, Callable
#from immutable import Immutable

A = TypeVar("A")
B = TypeVar("B")

class Maybe(Generic[A]):
    pass

class Just(Maybe[A],Immutable):

    def __init__(self, val: A):
        self.val = val

    def fmap(self, func: Callable[[A], B]) -> Maybe[B]:
        try:
            new_val = func(self.val)
            return Just(new_val)
        except Exception as e:
            return Nothing()

    def bind(self, func: Callable[[A], Maybe[B]]) -> Maybe[B]:
        try:
            new_val = func(self.val)
            return new_val
        except Exception as e:
            return Nothing()
    
    def __repr__(self):
        return str(self.val)

class Nothing(Maybe[A]):

    def fmap(self, func: Callable[[A], B]) -> Maybe[B]:
        return self
    
    def bind(self, func: Callable[[A], Maybe[B]]) -> Maybe[B]:
        return self
    
    def __repr__(self):
        return "Nothing...."
```

```python
Just("123").fmap(float)
```

```python
Just("123a").fmap(float)
```

```python
Just(" -10 ").fmap(int).fmap(abs)
```

```python
#Just(None)\
#    .fmap(lambda _: int(input("Insert number a: "))) \
#    .fmap(lambda x: x / int(input("Insert number b: "))) \
#    .fmap(lambda x: print(x))
```

```python
def decrease(num: int) -> Maybe[int]:
   if num >= 1:
       return Just(num-1)
   else:
       return Nothing()
```

```python
Just(5).bind(decrease)
```

```python
Just(0).bind(decrease)
```

## 常用的技巧
1. map
2. itertools
3. lambda
4. exception
5. decorator
6. generator
7. threading
8. regular expression


### itertools
我们来看看`itertools`的功能，这个程序包功能强大，对编程的方式影响深远。这里的材料主要来源于
[What are the uses of iter(callable, sentinel)?](https://stackoverflow.com/questions/38087427/what-are-the-uses-of-itercallable-sentinel)。


## 常用的数据结构

```python

```

```python

```
