import pygame as pg
import random
import time

words = [
    "cannon", "button", "kill", "vigorous", "third", "field", "introduce",
    "changeable", "stream", "swanky", "macho", "tony choi", "precede", "fuzzy",
    "moldy", "monkey", "fax", "elegant", "drain", "humdrum", "chunky",
    "territory", "tame", "disappear", "alert", "pointless", "hug", "party",
    "nauseating", "dizzy", "malicious", "curl", "balance", "street", "tank",
    "riddle", "nice", "remarkable", "difficult", "noise", "heat", "approval",
    "ocean", "acrid", "duck", "correct", "incandescent", "thunder", "ball",
    "skillful", "yaoqi", "mingxao", "junyi", "hanqi", "finley ellis",
    "british", "gorilla", "dopa", "permarandom", "poggers", "chungus"
]


def main_menu():
    screen = pg.display.set_mode((640, 480))
    mainfont = pg.font.Font(None, 80)
    promptfont = pg.font.Font(None, 60)
    color = pg.Color('white')
    clock = pg.time.Clock()
    clock = pg.time.Clock()

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_RETURN:
                    main()

        screen.fill((30, 30, 30))

        menu_surface = mainfont.render("Main Menu ", True, color)
        screen.blit(menu_surface, (180, 0))

        start_prompt = promptfont.render("Click Enter to start!", True,
                                         pg.Color('blue'))
        screen.blit(start_prompt, (140, 400))

        pg.display.flip()
        clock.tick(60)


def main():
    screen = pg.display.set_mode((640, 480))
    font = pg.font.Font(None, 32)
    biggerfont = pg.font.Font(None, 80)
    clock = pg.time.Clock()
    color = pg.Color('white')
    color2 = pg.Color('white')
    text = ''
    rand = random.randrange(0, 61)
    wordType = words[rand]
    move_word = pg.USEREVENT + 1
    x = 0
    xpos = 0
    t = 250
    ypos = random.randrange(99, 301)
    ms = 1
    pg.time.set_timer(move_word, t)
    xd_surface = []

    while True:
        for event in pg.event.get():
            if event.type == move_word:
                xd_surface = font.render(text, True, color)
                xpos = xpos + ms
                screen.blit(xd_surface, ((xpos), ypos))
            elif xpos > 640:
                end_surface = biggerfont.render("Final Score: " + str(x), True,
                                                color)
                screen.blit(end_surface, (50, 240))
                pg.display.update()
                time.sleep(2)
                main_menu()
            elif event.type == pg.QUIT:
                return
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_RETURN:
                    if text == words[rand]:
                        color2 = pg.Color('green')
                        xd_surface = font.render(wordType, True, color2)
                        screen.blit(xd_surface, (xpos, ypos))
                        pg.display.update()
                        time.sleep(1)
                        color2 = pg.Color('white')
                        x = x + 1
                        ms = ms + 1
                        text = ''
                        rand = random.randrange(0, 61)
                        wordType = words[rand]
                        xpos = 0
                        ypos = random.randrange(50, 380)
                    else:
                        color2 = pg.Color('red')
                        xd_surface = font.render(wordType, True, color2)
                        screen.blit(xd_surface, (xpos, ypos))
                        pg.display.update()
                        print("Wrong!")
                        text = ''
                elif event.key == pg.K_BACKSPACE:
                    text = text[:-1]
                else:
                    text += event.unicode

        screen.fill((30, 30, 30))
        txt_surface = font.render(text, True, color)
        screen.blit(txt_surface, (280, 400))

        xd_surface = font.render(wordType, True, color2)
        screen.blit(xd_surface, (xpos, ypos))

        score_surface = font.render("Words Correct: " + str(x), True, color)
        screen.blit(score_surface, (430, 0))

        pg.display.flip()
        clock.tick(60)


if __name__ == '__main__':
    pg.init()
    pg.display.set_caption('Typing game')
    main_menu()
    main()
    pg.quit()

