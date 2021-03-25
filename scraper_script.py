import torch, torchvision, PIL, numpy as np
from torchvision import datasets, models, transforms
import pathlib
import PIL
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from tqdm.auto import tqdm
torch.manual_seed(0)
np.random.seed(0)
from bing_image_downloader import downloader
#Used bing_image_downloader to download bulk of images

query_string = "m551 sheridan"
downloader.download(query=query_string, limit=600, output_dir='dataset')

query_string = "m24 chaffee"
downloader.download(query=query_string, limit=600, output_dir='dataset')