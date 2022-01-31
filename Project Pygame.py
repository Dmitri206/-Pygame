import sys
import pygame

pygame.init()

screen = pygame.display.set_mode((1080, 540))
pygame.display.set_caption('Мифические загадки')
fm1 = pygame.mixer.music
fm1.load("zvuk-kapli1.mp3")
fm1.play(-1)
sp1 = pygame.image.load('Вид спереди.png')
sp1.set_colorkey((255, 255, 255))
sp2 = pygame.image.load('Вид спереди1.png')
sp2.set_colorkey((255, 255, 255))
sp3 = pygame.image.load('Вид спереди2.png')
sp3.set_colorkey((255, 255, 255))
sp4 = pygame.image.load('Вид сбоку1.png')
sp4.set_colorkey((255, 255, 255))
sp5 = pygame.image.load('Вид сбоку2.png')
sp5.set_colorkey((255, 255, 255))
sp6 = pygame.image.load('Вид сзади.png')
sp6.set_colorkey((255, 255, 255))
sp7 = pygame.image.load('Вид сбоку шаг1.png')
sp7.set_colorkey((255, 255, 255))
sp8 = pygame.image.load('Вид сбоку шаг2.png')
sp8.set_colorkey((255, 255, 255))
sp9 = pygame.image.load('Вид сбоку шаг3.png')
sp9.set_colorkey((255, 255, 255))
sp10 = pygame.image.load('Вид сбоку шаг4.png')
sp10.set_colorkey((255, 255, 255))
sp11 = pygame.image.load('Вид сзади шаг1.png')
sp11.set_colorkey((255, 255, 255))
sp12 = pygame.image.load('Вид сзади шаг2.png')
sp12.set_colorkey((255, 255, 255))
spf = pygame.image.load('fen.png')
spf.set_colorkey((255, 255, 255))
spf = pygame.transform.scale(spf, (spf.get_size()[0] / 4, spf.get_size()[1] / 4))
txt1 = pygame.image.load('text1.png')
lok = pygame.image.load('lok1.png')
dlg = pygame.image.load('dialog1.png')
var1 = pygame.image.load('var1.png')
var2 = pygame.image.load('var2.png')
var3 = pygame.image.load('var3.png')
var4 = pygame.image.load('var4.png')
bonk = pygame.mixer.Sound('bonk.mp3')
death = pygame.mixer.Sound('death.mp3')
lok2 = pygame.image.load('Поляна.jpg')
lok2 = pygame.transform.scale(lok2, (lok2.get_size()[0] * 1.5, lok2.get_size()[1] * 1.2))
win1 = pygame.mixer.Sound('win1.mp3')
chs = pygame.mixer.Sound('сры.mp3')
troll = pygame.image.load('тролль.jpg')
troll.set_colorkey((255, 255, 255))
troll = pygame.transform.scale(troll, (troll.get_size()[0] / 4, troll.get_size()[1] / 4))
dlg2 = pygame.image.load('dialog1_2.png')
var1_2 = pygame.image.load('var1_2.png')
var2_2 = pygame.image.load('var2_2.png')
var3_2 = pygame.image.load('var3_2.png')
var4_2 = pygame.image.load('var4_2.png')
dlg3 = pygame.image.load('dialog1_3.png')
var1_3 = pygame.image.load('var1_3.png')
var2_3 = pygame.image.load('var2_3.png')
var3_3 = pygame.image.load('var3_3.png')
var4_3 = pygame.image.load('var4_3.png')
lok3 = pygame.image.load('Пустошь.jpg')
sfks = pygame.image.load('Сфинкс.jpg')
sfks.set_colorkey((255, 255, 255))
sfks = pygame.transform.scale(sfks, (sfks.get_size()[0] / 4, sfks.get_size()[1] / 4))
rect1 = sp1.get_rect(
    bottomright=(350, 300))
screen.blit(sp1, rect1)
anim = [sp1, sp3]
anim1 = [sp7, sp5, sp8, sp5]
anim2 = [sp9, sp4, sp10, sp4]
anim3 = [sp11, sp12]
clock = pygame.time.Clock()
i = 0
flDown = False
flUp = False
flRight = False
flLeft = False
flWork = False
spd = 5
w = 430
h = 210
n1 = 1
count = 0
blsc = 0
n2 = 1
First = False
Second = False
Thrd = False
Frth = False
task = False
hall = 1
n3 = 1
dc = 0
Won = pygame.mixer.Sound('Won.mp3')
while True:
    if hall == 4:
        screen.fill((0, 0, 0))
        f2 = pygame.font.SysFont('calibri', 146)
        text2 = f2.render('Вы выиграли!', False,
                          (255, 255, 0))
        f3 = pygame.font.SysFont('calibri', 100)
        text3 = f3.render('Кол-во смертей: ' + str(dc), False,
                          (255, 255, 255))
        screen.blit(text2, (120, 130))
        screen.blit(text3, (120, 290))
        if dc == 0:
            f1 = pygame.font.SysFont('calibri', 100)
            text1 = f1.render('Вы - Молодец!', False,
                              (0, 255, 0))
            screen.blit(text1, (120, 430))
        pygame.mixer.music.pause()
        Won.play(0)
        count += 1
        if count == 30 * 8:
            pygame.quit()
            sys.exit()
    else:
        if hall == 1:
            screen.blit(spf, (1080 - spf.get_size()[0], 330))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    flDown = True
                    n1 = 1
                if event.key == pygame.K_w:
                    flUp = True
                    n1 = 2
                if event.key == pygame.K_d:
                    flRight = True
                    n1 = 4
                if event.key == pygame.K_a:
                    flLeft = True
                    n1 = 3



            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_s:
                    n1 = 1
                    flDown = False
                if event.key == pygame.K_w:
                    n1 = 2
                    flUp = False
                if event.key == pygame.K_d:
                    n1 = 3
                    flRight = False
                if event.key == pygame.K_a:
                    n1 = 4
                    flLeft = False
                if event.key == pygame.K_f:
                    if task == False:
                        flWork = True
                        First = True
                        bonk.play(0)

                if event.key == pygame.K_RIGHT:
                    if n2 < 4 and flWork == True:
                        chs.play(0)
                        n2 += 1
                        if n2 == 1:
                            First = True
                            Second = False
                            Thrd = False
                            Frth = False
                        if n2 == 2:
                            First = False
                            Second = True
                            Thrd = False
                            Frth = False
                        if n2 == 3:
                            First = False
                            Second = False
                            Thrd = True
                            Frth = False
                        if n2 == 4:
                            First = False
                            Second = False
                            Thrd = False
                            Frth = True
                if event.key == pygame.K_LEFT:
                    if n2 > 1 and flWork == True:
                        chs.play(0)
                        n2 -= 1
                        if n2 == 1:
                            First = True
                            Second = False
                            Thrd = False
                            Frth = False
                        if n2 == 2:
                            First = False
                            Second = True
                            Thrd = False
                            Frth = False
                        if n2 == 3:
                            First = False
                            Second = False
                            Thrd = True
                            Frth = False
                        if n2 == 4:
                            First = False
                            Second = False
                            Thrd = False
                            Frth = True
                if event.key == pygame.K_g:
                    if hall == 1:
                        if First == False and Second == True and Thrd == False and Frth == False and flWork == True:
                            task = True
                            flWork = False
                            count = 0
                            Second = False
                            n2 = 1
                            win1.play(0)
                            n3 += 1
                        elif flWork == False:
                            pass
                        else:
                            count = 35 * 60
                            death.play(0)
                    if hall == 2:
                        if First == False and Second == False and Thrd == True and Frth == False and flWork == True:
                            task = True
                            flWork = False
                            count = 0
                            Thrd = False
                            n2 = 1
                            n3 += 1
                            win1.play(0)
                        elif flWork == False:
                            pass
                        else:
                            count = 45 * 60
                            death.play(0)
                    if hall == 3:
                        if First == True and Second == False and Thrd == False and Frth == False and flWork == True:
                            task = True
                            flWork = False
                            count = 0
                            First = False
                            n2 = 1
                            n3 += 1
                            win1.play(0)
                        elif flWork == False:
                            pass
                        else:
                            count = 50 * 60
                            death.play(0)
        screen.fill((0, 0, 0))
        if hall == 1:
            screen.blit(lok, (-500, -300))
            screen.blit(spf, (1080 - spf.get_size()[0], 200))
        if hall == 2:
            screen.blit(lok2, (0, 0))
            screen.blit(troll, (1080 - troll.get_size()[0], 160))
        if hall == 3:
            screen.blit(lok3, (0, 0))
            screen.blit(sfks, (1080 - sfks.get_size()[0], 160))

        if flDown and h + sp1.get_size()[1] <= 540:
            i += 1
            if i == 60:
                i = 0
            screen.blit(anim[i // 30], (w, h))
            h += 3
        elif flDown == False and flLeft == False and flRight == False and flUp == False and n1 == 1:
            screen.blit(sp2, (w, h))
        elif flDown == True and flLeft == False and flRight == False and flUp == False and n1 == 1:
            screen.blit(sp2, (w, h))
        if flUp and h >= 0:
            i += 1
            if i == 60:
                i = 0
            screen.blit(anim3[i // 30], (w, h))
            h -= 3
        elif flDown == False and flLeft == False and flRight == False and flUp == False and n1 == 2:
            screen.blit(sp6, (w, h))
        elif flDown == False and flLeft == False and flRight == False and flUp == True and n1 == 2:
            screen.blit(sp6, (w, h))
        if flLeft and w >= 0:
            i += 1
            if i == 60:
                i = 0
            screen.blit(anim1[i // 15], (w, h))
            w -= 3
        elif flDown == False and flLeft == False and flRight == False and flUp == False and n1 == 3:
            screen.blit(sp4, (w, h))
        elif flDown == False and flLeft == True and flRight == False and flUp == False and n1 == 3:
            screen.blit(sp5, (w, h))
            if hall > 1:
                hall -= 1
                task = True
                w = 1080 - sp9.get_size()[0]

        if task == False:
            if flRight and w + sp9.get_size()[0] + spf.get_size()[0] <= 1080:
                i += 1
                if i == 60:
                    i = 0
                screen.blit(anim2[i // 15], (w, h))
                w += 3
            elif flDown == False and flLeft == False and flRight == False and flUp == False and n1 == 4:
                screen.blit(sp5, (w, h))
            elif flDown == False and flLeft == False and flRight == True and flUp == False and n1 == 4:
                screen.blit(sp4, (w, h))
                screen.blit(txt1, (200, 330))
        else:
            if flRight and w + sp9.get_size()[0] <= 1080:
                i += 1
                if i == 60:
                    i = 0
                screen.blit(anim2[i // 15], (w, h))
                w += 3
            elif flDown == False and flLeft == False and flRight == False and flUp == False and n1 == 4:
                screen.blit(sp5, (w, h))
            elif flDown == False and flLeft == False and flRight == True and flUp == False and n1 == 4:
                w = 0

                hall += 1
                if hall == n3:
                    task = False
        if flWork == True:
            if hall == 1:
                screen.blit(dlg, (170, 80))
                f1 = pygame.font.SysFont('javanesetext', 18)
                text1 = f1.render('35', False,
                                  (255, 0, 0))
                f2 = pygame.font.SysFont('javanesetext', 56)
                text2 = f2.render(str(count // 30), False,
                                  (255, 0, 0))
                f3 = pygame.font.SysFont('comicsansms', 14)
                text3 = f3.render('Чтобы выбрать ответ, нажмите на клавишу G', False,
                                  (255, 255, 255))
                count += 1
                screen.blit(text1, (610, 122))
                screen.blit(text2, (195, 360))
                screen.blit(text3, (540, 45 + dlg.get_size()[1]))
            if hall == 2:
                screen.blit(dlg2, (170, 80))
                f2 = pygame.font.SysFont('javanesetext', 56)
                text2 = f2.render(str(count // 30), False,
                                  (255, 0, 0))
                f3 = pygame.font.SysFont('comicsansms', 14)
                text3 = f3.render('Чтобы выбрать ответ, нажмите на клавишу G', False,
                                  (255, 255, 255))
                count += 1
                screen.blit(text2, (195, 360))
                screen.blit(text3, (540, 45 + dlg.get_size()[1]))
            if hall == 3:
                screen.blit(dlg3, (170, 80))
                f2 = pygame.font.SysFont('javanesetext', 56)
                text2 = f2.render(str(count // 30), False,
                                  (255, 0, 0))
                f3 = pygame.font.SysFont('comicsansms', 14)
                text3 = f3.render('Чтобы выбрать ответ, нажмите на клавишу G', False,
                                  (255, 255, 255))
                count += 1
                screen.blit(text2, (195, 360))
                screen.blit(text3, (540, 45 + dlg.get_size()[1]))

        if hall == 1:
            if count // 30 >= 35:
                if count == 35 * 30:
                    death.play(0)
                    dc += 1
                task = False
                First = False
                Second = False
                Thrd = False
                Frth = False
                if blsc == 10 * 60:
                    w = 430
                    h = 210
                    flWork = False
                    hall = 1
                    count = 0
                    n1 = 1
                    blsc = 0
                elif blsc < 600:
                    screen.fill((0, 0, 0))
                    f2 = pygame.font.SysFont('javanesetext', 146)
                    text2 = f2.render('GAME OVER', False,
                                      (200, 0, 0))
                    screen.blit(text2, (100, 130))
                    blsc += 1
        if hall == 2:
            if count // 30 >= 45:
                if count == 45 * 30:
                    death.play(0)
                    dc += 1
                task = False
                First = False
                Second = False
                Thrd = False
                Frth = False
                if blsc == 10 * 60:
                    w = 430
                    h = 210
                    flWork = False
                    hall = 1
                    count = 0
                    n1 = 1
                    blsc = 0
                elif blsc < 600:
                    screen.fill((0, 0, 0))
                    f2 = pygame.font.SysFont('javanesetext', 146)
                    text2 = f2.render('GAME OVER', False,
                                      (200, 0, 0))
                    screen.blit(text2, (100, 130))
                    blsc += 1
        if hall == 3:
            if count // 30 >= 50:
                if count == 50 * 30:
                    death.play(0)
                    dc += 1
                task = False
                First = False
                Second = False
                Thrd = False
                Frth = False
                if blsc == 10 * 60:
                    w = 430
                    h = 210
                    flWork = False
                    hall = 1
                    count = 0
                    n1 = 1
                    blsc = 0
                elif blsc < 600:
                    screen.fill((0, 0, 0))
                    f2 = pygame.font.SysFont('javanesetext', 146)
                    text2 = f2.render('GAME OVER', False,
                                      (200, 0, 0))
                    screen.blit(text2, (100, 130))
                    blsc += 1
        if First == True and Second == False and Thrd == False and Frth == False:
            if hall == 1:
                screen.blit(var1, (245, 10 + dlg.get_size()[1]))
            if hall == 2:
                screen.blit(var1_2, (245, 10 + dlg.get_size()[1]))
            if hall == 3:
                screen.blit(var1_3, (245, 10 + dlg.get_size()[1]))
        if First == False and Second == True and Thrd == False and Frth == False:
            if hall == 1:
                screen.blit(var2, (365, 10 + dlg.get_size()[1]))
            if hall == 2:
                screen.blit(var2_2, (365, 10 + dlg.get_size()[1]))
            if hall == 3:
                screen.blit(var2_3, (365, 10 + dlg.get_size()[1]))
        if First == False and Second == False and Thrd == True and Frth == False:
            if hall == 1:
                screen.blit(var3, (475, 10 + dlg.get_size()[1]))
            if hall == 2:
                screen.blit(var3_2, (475, 10 + dlg.get_size()[1]))
            if hall == 3:
                screen.blit(var3_3, (475, 10 + dlg.get_size()[1]))
        if First == False and Second == False and Thrd == False and Frth == True:
            if hall == 1:
                screen.blit(var4, (585, 10 + dlg.get_size()[1]))
            if hall == 2:
                screen.blit(var4_2, (585, 10 + dlg.get_size()[1]))
            if hall == 3:
                screen.blit(var4_3, (585, 10 + dlg.get_size()[1]))


    pygame.display.flip()
    clock.tick(60)
