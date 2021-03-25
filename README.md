# Binary-Image-Classifier

This project demonstrates **transfer learning** using a pretrained ResNet18 CNN model that can distinguish between two tank models: M24 Chaffee and the M551 Sheridan. These are both tanks used during the Korean and Vietnam Wars respectively. By changing ResNet18's final classification layer to support classification of thr M24 Chaffee and M551 Sheridan, creating and formatting a dataset consisting of over 1500 photos, and experimenting with various optimizer and scheduler parameters, I was able to reach an accuracy of about 99%. 

# Results
The model is able to achieve a 99% validation accuracy after training with a Google Colaboratory provided GPU using 10 epochs. Multiple iterations of the model were tested with different optimizer and scheduler parameters set.

## Best Results
The best results were as follows. Note the test accuracy converges to about 99%-98% in epochs 5 to 10.
![](https://github.com/chrischang5/Binary-Image-Classifier/blob/main/README%20Images/best%20results.png)

## Optimizer and Scheduler Experimentation 
![## Experimentation with Optimizer and Scheduler parameters](https://github.com/chrischang5/Binary-Image-Classifier/blob/main/README%20Images/parameter_experiment.png)


# Dataset Creation

A full dataset was created using a [Bing Images Scraper](https://github.com/gurugaurav/bing_image_downloader) and augmented through Pytorch's `transforms.RandomHorizontalFlip` and `transforms.RandomRotation*degrees=(-35,35))`. In total, the dataset consisted of a training dataset consisting of over 1200 images and validation dataset consisting of over 300 images. 

## Sample Entry

![](https://github.com/chrischang5/Binary-Image-Classifier/blob/main/README%20Images/dataset_demonstration.png)
