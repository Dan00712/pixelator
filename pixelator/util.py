from PIL import Image, ImageStat
from PIL.Image import Image as Img


def pixelate_image(
        img: Img,
        *,
        row_pixels=20,
        col_pixels=20
        ):
    cp_img = Image.new('RGB', size=img.size)
    
    row_pixel_jump = img.height // row_pixels
    col_pixel_jump = img.width  // col_pixels
    
    for left in range(0, img.width, col_pixel_jump):
        for top in range(0, img.height, row_pixel_jump):
            box = (left, top, left+col_pixel_jump, top+row_pixel_jump)
            region = img.crop(box)
            median = ImageStat.Stat(region).median
            r = Image.new('RGB', (col_pixel_jump, row_pixel_jump), tuple(median))
            cp_img.paste(r, (left, top))
     
    return cp_img

def pixelate_2(
    img, *, level=8
    ):
    cp_img = img.copy()
    cp_img = cp_img.resize(
        size=(img.size[0]//level, img.size[1]//level),
        resample=0
        )
    cp_img = cp_img.resize(size=img.size, resample=0)
    return cp_img