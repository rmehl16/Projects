from matplotlib import gridspec
import matplotlib.pylab as plt
import numpy as np
import tensorflow as tf
import tensorflow_hub as tf_hub
import PIL


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

    ########## London Bridge ##########

    orig_img_fp = "Images/London_Bridge.jpg"
    original_image = load_image(orig_img_fp, image_size=(3180, 3180))

    style_img_fp = "Images/Nighthawks.jpg"
    style_image = load_image(style_img_fp, image_size=(2400,1300))


    ########## Third Lake ##########

    # orig_img_fp = "Images/Third_Lake_Sunset.jpg"
    # original_image = load_image(orig_img_fp, image_size=(2400, 1300))

    # style_img_fp = "Images/A_Sunday_on_La_Grande_Jatte.jpg"
    # style_image = load_image(style_img_fp, image_size=(525,353))
    # style_img_fp = "Images/The_Scream.jpg"
    # style_image = load_image(style_img_fp, image_size=(2400,1300))


    ########## Central Park Sunset ##########

    # orig_img_fp = "Images/NYC_CP.jpg"
    # original_image = load_image(orig_img_fp, image_size=(2400, 1300))

    # style_img_fp = "Images/The_Scream.jpg"
    # style_image = load_image(style_img_fp, image_size=(2400,1300))


    ########## Arlington ##########
    
    # orig_img_fp = "Images/Arlington.jpg"
    # original_image = load_image(orig_img_fp, image_size=(2400, 1300))

    # style_img_fp = "Images/A_Sunday_on_La_Grande_Jatte.jpg"
    # style_image = load_image(style_img_fp, image_size=(525,353))


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


    ########## Kona ##########
    
    # orig_img_fp = "Images/Kona2.jpg"
    # original_image = load_image(orig_img_fp, image_size=(768, 1024))

    # style_img_fp = "Images/Mona_Lisa.jpg"
    # style_image = load_image(style_img_fp, image_size=(1024,768))


    ########## Chicago ##########
    
    # orig_img_fp = "Images/Wrigley_Field_sign_night.jpg"
    # original_image = load_image(orig_img_fp, image_size=(3180, 3180))

    # style_img_fp = "Images/Ad.jpg"
    # style_image = load_image(style_img_fp, image_size=(574,750))



    # visualize([original_image, style_image], ['Original Image', 'Style Image'])

    style_image = tf.nn.avg_pool(style_image, ksize=[3,3], strides=[1,1], padding='VALID')

    stylize_model = tf_hub.load('tf_model')

    results = stylize_model(tf.constant(original_image), tf.constant(style_image))
    stylized_image = results[0]

    #visualize([original_image, style_image, stylized_image], titles=['Original Image', 'Style Image', 'Stylized Image'])

    export_image(stylized_image).save("Cubs_x_Ad.png")

