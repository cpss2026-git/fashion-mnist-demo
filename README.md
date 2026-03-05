# Fashon-MNISTのウェブデモ

## 仮想環境のセットアップ

Python 3.11系を推奨。pyenvがあればそれを使う。

```sh
pyenv --install 3.11.15
pyenv global 3.11.15
```

```sh
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install --upgrade pip
python3 -m pip install tensorflow tensorflowjs
```

Macの場合は、仮想環境を作る時に`python3.11`を指定する必要がある。pyenvで指定しても良い。

```sh
python3.11 -m venv .venv
source .venv/bin/activate
python3 -m pip install --upgrade pip
python3 -m pip install tensorflow 
```

## 訓練

```sh
python3 train.py
```

出力。

```txt
Epoch 1/5
1875/1875 ━━━━━━━━━━━━━━━━━━━━ 3s 1ms/step - accuracy: 0.8266 - loss: 0.4958    Epoch 2/5
1875/1875 ━━━━━━━━━━━━━━━━━━━━ 2s 1ms/step - accuracy: 0.8658 - loss: 0.3749  
Epoch 3/5
1875/1875 ━━━━━━━━━━━━━━━━━━━━ 2s 1ms/step - accuracy: 0.8769 - loss: 0.3376  
Epoch 4/5
1875/1875 ━━━━━━━━━━━━━━━━━━━━ 2s 1ms/step - accuracy: 0.8852 - loss: 0.3126  
Epoch 5/5
1875/1875 ━━━━━━━━━━━━━━━━━━━━ 2s 1ms/step - accuracy: 0.8916 - loss: 0.2939  
313/313 ━━━━━━━━━━━━━━━━━━━━ 0s 878us/step - accuracy: 0.8716 - loss: 0.3586

Test accuracy: 0.8715999722480774

Model was saved.
```

## チェック

```sh
python3 check.py
```

出力。

```txt
0: true=Boot     pred=Boot     Correct
1: true=Pullover pred=Pullover Correct
2: true=Trouser  pred=Trouser  Correct
(snip)
98: true=Coat     pred=Coat     Correct
99: true=Pullover pred=Pullover Correct

Accuracy: 86/100 = 86.00%
```

Python側から重みをエクスポート。

```sh
$ python3 export.py

Saved artifact at 'export'. The following endpoints are available:

* Endpoint 'serve'
  args_0 (POSITIONAL_ONLY): TensorSpec(shape=(None, 28, 28), dtype=tf.float32, name='input_layer')
Output Type:
  TensorSpec(shape=(None, 10), dtype=tf.float32, name=None)
Captures:
  5170739888: TensorSpec(shape=(), dtype=tf.resource, name=None)
  5171496384: TensorSpec(shape=(), dtype=tf.resource, name=None)
  5171496208: TensorSpec(shape=(), dtype=tf.resource, name=None)
  5171496912: TensorSpec(shape=(), dtype=tf.resource, name=None)
Model was exported.
```

エクスポートされたデータをJSで読める形に変換。

```sh
tensorflowjs_converter export docs/model
```

`docs/index.html`をLive Serverで開いて確認。

## 学習データの例

| Bag | Boot | Coat | Dress | Pullover | Sandal | Shirt | Sneaker | Top |
|-----|------|------|-------|----------|--------|-------|---------|-----|
| ![](docs/img/Bag/0.png) | ![](docs/img/Boot/0.png) | ![](docs/img/Coat/0.png) | ![](docs/img/Dress/0.png) | ![](docs/img/Pullover/0.png) | ![](docs/img/Sandal/0.png) | ![](docs/img/Shirt/0.png) | ![](docs/img/Sneaker/0.png) | ![](docs/img/Top/0.png) |
| ![](docs/img/Bag/1.png) | ![](docs/img/Boot/1.png) | ![](docs/img/Coat/1.png) | ![](docs/img/Dress/1.png) | ![](docs/img/Pullover/1.png) | ![](docs/img/Sandal/1.png) | ![](docs/img/Shirt/1.png) | ![](docs/img/Sneaker/1.png) | ![](docs/img/Top/1.png) |
| ![](docs/img/Bag/2.png) | ![](docs/img/Boot/2.png) | ![](docs/img/Coat/2.png) | ![](docs/img/Dress/2.png) | ![](docs/img/Pullover/2.png) | ![](docs/img/Sandal/2.png) | ![](docs/img/Shirt/2.png) | ![](docs/img/Sneaker/2.png) | ![](docs/img/Top/2.png) |
| ![](docs/img/Bag/3.png) | ![](docs/img/Boot/3.png) | ![](docs/img/Coat/3.png) | ![](docs/img/Dress/3.png) | ![](docs/img/Pullover/3.png) | ![](docs/img/Sandal/3.png) | ![](docs/img/Shirt/3.png) | ![](docs/img/Sneaker/3.png) | ![](docs/img/Top/3.png) |
| ![](docs/img/Bag/4.png) | ![](docs/img/Boot/4.png) | ![](docs/img/Coat/4.png) | ![](docs/img/Dress/4.png) | ![](docs/img/Pullover/4.png) | ![](docs/img/Sandal/4.png) | ![](docs/img/Shirt/4.png) | ![](docs/img/Sneaker/4.png) | ![](docs/img/Top/4.png) |
| ![](docs/img/Bag/5.png) | ![](docs/img/Boot/5.png) | ![](docs/img/Coat/5.png) | ![](docs/img/Dress/5.png) | ![](docs/img/Pullover/5.png) | ![](docs/img/Sandal/5.png) | ![](docs/img/Shirt/5.png) | ![](docs/img/Sneaker/5.png) | ![](docs/img/Top/5.png) |
| ![](docs/img/Bag/6.png) | ![](docs/img/Boot/6.png) | ![](docs/img/Coat/6.png) | ![](docs/img/Dress/6.png) | ![](docs/img/Pullover/6.png) | ![](docs/img/Sandal/6.png) | ![](docs/img/Shirt/6.png) | ![](docs/img/Sneaker/6.png) | ![](docs/img/Top/6.png) |
| ![](docs/img/Bag/7.png) | ![](docs/img/Boot/7.png) | ![](docs/img/Coat/7.png) | ![](docs/img/Dress/7.png) | ![](docs/img/Pullover/7.png) | ![](docs/img/Sandal/7.png) | ![](docs/img/Shirt/7.png) | ![](docs/img/Sneaker/7.png) | ![](docs/img/Top/7.png) |
| ![](docs/img/Bag/8.png) | ![](docs/img/Boot/8.png) | ![](docs/img/Coat/8.png) | ![](docs/img/Dress/8.png) | ![](docs/img/Pullover/8.png) | ![](docs/img/Sandal/8.png) | ![](docs/img/Shirt/8.png) | ![](docs/img/Sneaker/8.png) | ![](docs/img/Top/8.png) |
| ![](docs/img/Bag/9.png) | ![](docs/img/Boot/9.png) | ![](docs/img/Coat/9.png) | ![](docs/img/Dress/9.png) | ![](docs/img/Pullover/9.png) | ![](docs/img/Sandal/9.png) | ![](docs/img/Shirt/9.png) | ![](docs/img/Sneaker/9.png) | ![](docs/img/Top/9.png) |

## LICENSE

MIT