import os
import pict
import exel
import mim

file='test.xlsx'
picture='1920x1280_809783_www.ArtFile.ru_.jpg'
font='Wentrisor.ttf'
color=input('Выберите цвет текста в формате #000000:')
xy=(100,400)
from_email =input('Ваш email:')
post_host='mail.ru'
password = input('Пароль:')
subject='открытка с поздравлением'#input('Тема сообщения:')
body='открытка с поздравлением'#input('Текст сообщения:')
all=exel.exel(file)
text='twsdfg'#input('Текст поздравления:')


def main(from_email, password,xy,picture, font, text,subject,body,color,post_host):
    for pers in all:
        if pers[4]=='ж':
            appeal='Уважаемая '
        else:
            appeal = 'Уважаемый '
        text=(f'{appeal}{pers[0]} {pers[1]} {pers[2]}!\n {text} ')
        postcard=pict.picture(xy,picture, font, text,color)
        mim.post(from_email, password, pers[3],subject,body, postcard,post_host)
        try:
            os.path.isfile(postcard)
        except:
             print("File doesn't exists!")
        finally:   os.remove(postcard)


main(from_email, password,(xy),picture, font, text,subject,body,color,post_host)


