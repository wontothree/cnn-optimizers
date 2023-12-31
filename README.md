# Convergence analysis of optimizers

## Empirical evaluation

Training loss, Validation accuracy

Optimizer들의 수렴성을 분석하고, Convergence analysis of optimizers에 실험을 진행합니다.

Image classification Experiment

|Datasets|CNN Models|Optimizers|
|---|---|---|
|Mnist|LeNet-5|SGD|
|Fashion MNIST|AlexNet|SGDM|
|Cifar10|VGGNet|Adagrad|
|Cifar100|GoogleNet|RMSProp|
|Imagenet|ResNet|Adam|

## Imagenet

|Mnist|Cifar10|Cifar100|Imagenet|
|---|---|---|---|
|28x28|32x32|32x32|224x224|

*스마트폰의 해상도 : 1080x1920

## CNN Architectures

||LeNet-5|AlexNet|VGGNet|GoogleNet|ResNet|
|---|---|---|---|---|---|
|Convolution layers||5|13|21|152|
|Fully connected layers||3|3|1|3(전역 평균 풀링층)|
|Parameter||67M|138M|5M|7000M|
|규제 기법||Dropout|||Batch normalization|
|특징||||Inception module, No FC layer||
