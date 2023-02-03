from matplotlib import gridspec
import matplotlib.pylab as plt
import numpy as np
import tensorflow as tf
import tensorflow_hub as tf_hub
from tensorflow.python.client import device_lib
import PIL

import argparse
import sys

from IMAGES import IMAGE_REF


def load_image(image_path, image_size=(512, 256)):
    img = tf.io.decode_image(
      tf.io.read_file(image_path),
      channels=3, dtype=tf.float32)[tf.newaxis, ...]
    img = tf.image.resize(img, image_size, preserve_aspect_ratio=True)
    #img = tf.image.resize(img, image_size)
    return img


def visualize(images, titles=('',)):
    noi = len(images)
    image_sizes = [image.shape[1] for image in images]
    w = (image_sizes[0] * 6) // 320
    plt.figure(figsize=(w  * noi, w))
    grid_look = gridspec.GridSpec(1, noi, width_ratios=image_sizes)
    
    for i in range(noi):
        plt.subplot(grid_look[i])
        plt.imshow(images[i][0], aspect='equal')
        plt.axis('off')
        plt.title(titles[i])
        plt.savefig("final.jpg")
    plt.show()


def export_image(tf_img):
    tf_img = tf_img*255
    tf_img = np.array(tf_img, dtype=np.uint8)
    if np.ndim(tf_img)>3:
        assert tf_img.shape[0] == 1
        img = tf_img[0]
    return PIL.Image.fromarray(img)


if __name__ == '__main__':

    print("TensorFlow version:", tf.__version__)
    print("Num GPUs Available: ", len(tf.config.list_physical_devices('GPU')))
    print("Physical Devices Available: ", tf.config.list_physical_devices())


    help_msg = ''
    parser = argparse.ArgumentParser(description=help_msg)
    parser.add_argument('--target', default='London_Bridge')
    parser.add_argument('--style', default='Nighthawks')

    args = parser.parse_args()
    print(args.target)

    print(f'Target Image: {args.target}\nResolution: {IMAGE_REF[args.target]["Res_x"]}, {IMAGE_REF[args.target]["Res_x"]}')
    print(f'Target Image: {args.style}\nResolution: {IMAGE_REF[args.style]["Res_x"]}, {IMAGE_REF[args.style]["Res_x"]}')
    
    #sys.exit()
    tgt_path = IMAGE_REF[args.target]["Path"]
    tgt_res_x = IMAGE_REF[args.target]["Res_x"]
    tgt_res_y = IMAGE_REF[args.target]["Res_y"]

    style_path = IMAGE_REF[args.style]["Path"]
    style_res_x = IMAGE_REF[args.style]["Res_x"]
    style_res_y = IMAGE_REF[args.style]["Res_y"]

    original_image = load_image(tgt_path, image_size=(tgt_res_x, tgt_res_y))

    style_image = load_image(style_path, image_size=(style_res_x, style_res_y))


    ########## London_Bridge x Nighthawks ##########
 
    ########## 3_Lake x Sunday ##########

    ########## 3_Lake x Scream ##########

    ########## Central Park Sunset x Scream ##########

    ########## Arlington x Sunday ##########

    ########## Wrigley_Sign x Ad ##########

    ########## Elephant ##########
    
    # orig_img_fp = "Images/Smithsonian_Elephant.jpg"
    # original_image = load_image(orig_img_fp, image_size=(2400, 1300))

    # style_img_fp = "Images/The_Birth_of_Venus.jpg"
    # style_image = load_image(style_img_fp, image_size=(2400,1300))
    # style_img_fp = "Images/Composition_10.png"
    # style_image = load_image(style_img_fp, image_size=(640,419))



    ########## Pepper ##########
    
    # orig_img_fp = "Images/Pepper2.jpg"
    # original_image = load_image(orig_img_fp, image_size=(1300, 2400))
    # original_image = tf.image.rot90(original_image, k=1)

    # style_img_fp = "Images/Starry_Night.jpg"
    # style_image = load_image(style_img_fp, image_size=(1135,899))


    ########## Kona3 x Pic_wwf ##########
    
    # orig_img_fp = "Images/Kona1.jpg"
    # original_image = load_image(orig_img_fp, image_size=(768, 1024))

    # style_img_fp = "Images/Mona_Lisa.jpg"
    # style_image = load_image(style_img_fp, image_size=(1024,768))

    # style_img_fp = "Images/Composition_VIII.jpg"
    # style_image = load_image(style_img_fp, image_size=(1024,1024))



    # visualize([original_image, style_image], ['Original Image', 'Style Image'])

    style_image = tf.nn.avg_pool(style_image, ksize=[3,3], strides=[1,1], padding='VALID')

    stylize_model = tf_hub.load('tf_model')

    results = stylize_model(tf.constant(original_image), tf.constant(style_image))
    stylized_image = results[0]

    #visualize([original_image, style_image, stylized_image], titles=['Original Image', 'Style Image', 'Stylized Image'])

    export_image(stylized_image).save("Test.png")

