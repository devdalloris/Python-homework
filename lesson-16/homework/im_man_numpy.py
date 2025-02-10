from PIL import Image
import numpy as np
def save_img(arr, name):
    img = Image.fromarray(arr)
    img.save(f'images/{name}.jpg')
with Image.open('./images/birds.png') as img:
    img_arr=np.array(img)
    img_up = np.flipud(img)
    img_lr=np.fliplr(img)
    save_img(img_up, name='up')
    save_img(img_lr, name='lr')
    print(img_arr.shape) 
