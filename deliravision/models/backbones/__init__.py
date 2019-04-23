from delira import  get_backends as __get_backends

if "TORCH" in __get_backends():

    from .resnet import ResNetTorch
    from .vgg import VGGTorch
    from .alexnet import AlexNetTorch
    from .squeezenet import SqueezeNetTorch
    from .densenet import DenseNetTorch
    from .mobilenet import MobileNetV2Torch
    from .resnext import ResNeXtTorch
    from .seblocks import SEBasicBlockTorch, SEBottleneckTorch, \
        SEBottleneckXTorch
