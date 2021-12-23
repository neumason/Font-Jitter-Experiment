from PIL import Image
from PIL import ImageFilter

im = Image.open('./image/yong.png')
im = im.filter(ImageFilter.GaussianBlur(radius=8))

im.save('./image/output1.png')