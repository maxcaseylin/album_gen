# album_gen
 
Code for training a DCGAN to generate pictures of album art, written in Tensorflow, along with:
* scripts for preprocessing and cleaning images to fit in the neural network
* a script to combine the output images during training into a GIF

Demos
-----


Result after 1.5 hours(300 Epochs) of training, with 1.2k images and batch size 100
<p align="center">
 <img src="/output_gifs/output_1k.gif" title="output_1k" alt="output_1k">
</p>

Result after about 5 hours(186 Epochs) of training, with 10k images and batch size 128
<p align="center">
 <img src="/output_gifs/output_10k.gif" title="output_10k" alt="output_10k">
</p>

Result on celeba dataset after 1 hour (350 epochs of training), with 1k images and 128 batch size
<p align="center">
 <img src="/output_gifs/output_celeb_1k.gif" title="output_celeb_1k" alt="output_celeb_1k">
</p>

Result on celeba dataset after 5 hours (350 epochs of training), with 4.7k images and 128 batch size
<p align="center">
 <img src="/output_gifs/output_celeb_4k.gif" title="output_celeb_4k" alt="output_celeb_4k">
</p>

Due to hardware limitations I haven't been able to train the network as much as I would have liked, so in the future if I have better hardware I'll probably get better results

Prerequisites
-----
* Tensorflow

* matplotlib

* imageio(if using the GIF script)

Usage
-----
Personal usage of this repository is NOT recommended as data processing and cleaning are all separate scripts.
