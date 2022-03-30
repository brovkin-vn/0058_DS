import os
import sys
print(os.path.dirname(sys.executable))
import albumentations
print(albumentations.__file__)
import albumentations.pytorch as pt
print(pt.__file__)
from albumentations.pytorch import ToTensor

