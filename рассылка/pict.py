from PIL import Image,ImageDraw,ImageFont

def picture(xy,pic, font, text,color):
    im = Image.open(pic)
    draw_text = ImageDraw.Draw(im)
    font = ImageFont.truetype(font, size=58)
    draw_text.text((xy),text,font=font,
    fill=(color))
    im.save('postcsrd.jpg')
    return 'postcsrd.jpg'



