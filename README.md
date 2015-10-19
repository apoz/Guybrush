# Guybrush script
This is just an attempt to make an script for generating Monkey Island style images with custom text on them.


# Dependencies

* We will use Pillow python library. It requires the following dependencies:
```
brew install libtiff libjpeg webp little-cms

Then install Pillow with:

$ pip install Pillow

```
Brew is having issues to install libpng, I've got to check further...

More information can be found in the following link: https://pillow.readthedocs.org/en/3.0.x/installation.html#os-x-installation


# Example of use

```
python ./guybrush/guybrush.py -i imgs/Sample_1.jpg -o imgs/test33.png "Yo soy cola, tu pegamento"
´´´
Which outputs to:


# TO DO

* Multi-line text support
* Additional fonts
* Animated gifs?