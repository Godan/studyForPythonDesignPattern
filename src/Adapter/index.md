# Pythonで学ぶ「デザインパターン入門」

## Adapter Pattern
アダプターパターンはすでに提供されているものがそのままでは使えないとき、使いづらいときに使いやす形式に直すパターンです。基本的な継承を用いた実装パターンの一つです。

ちなみにアダプターを辞書で引くと


>機械・器具を多目的に使用するための付属品。また、それを取り付けるための補助具。

>大辞林 第三版

という意味合いを持ちます。使えるようにするために変換を間に挟むイメージです。
またアダプターパターンはワッパーパターンとも呼ばれることもあります。

## 登場人物たち
今回も書籍と同様の文字列に装飾を追加するプログラムを例に書いていきます。

### Target
必要なメゾットをリストアップしているクラスです。本来はインターフェースとして実装します。今回はClassとして実装し、継承することで実現します。

```python
class Print:
    def printWeak(self):
        pass

    def printStrong(self):
        pass

```

### Client
今回の変換されたものを使うものです。後述するAdapterはClientの要望を満たすように実装しなければなりません.


```Python
from Banner import Banner
from PrintBanner import PrintBanner

def main():
    banner = PrintBanner("Hello")
    banner.printWeak()
    banner.printStrong()


if __name__ == '__main__':
    main()

```

### Adaptee
今回の変換元です。　今回必要メゾットを持っています。　　



```Python
class Banner:

    def __init__(self, string):
        self.string = string

    def showWithParen(self):
        print("(" + self.string + ")")

    def showWithAster(self):
        print("*" + self.string + "*")

```
今回のバーナークラスは以下のメゾットを持っています

* 与えられた文字列にカッコを追加して出力する
* 与えられた文字列にアスタリスクを追加して出力する


### Adapter
今回の主人公です。Adapteeを使えるようにしてClientを満たせるように実装します。今回は継承を行って実装します

```Python
from Print import Print
from Banner import Banner

class PrintBanner(Print):

    def __init__(self, strings):
        self.banner = Banner(strings)

    def printWeak(self):
        self.banner.showWithParen()

    def printStrong(self):
        self.banner.showWithAster()


```

##　アダプターパターンの利点

### 再テストの範囲が狭まる
もし既存のクラスに修正を加えた場合その変更によって動こなくなった場所がないかを確認する必要があります。アダプターパターンなら既存のものに変更はないため新しく実装したアダプター周辺だけテストすれば良くなります。

### 破壊的変更がない
既存のものには手を加えてないので既存のコードの影響を考えないで実装することができます。
