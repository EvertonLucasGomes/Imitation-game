from tkinter import *
from gameDataBase import bd
import pygame

class interface:

    def __init__(self):
        self.fontDefault = 'Courier 12'
        self.fontDefaultBold = 'Courier 15 bold'

        self.listSubtitles = []
        self.currentSlide = 0
        self.page = 'initial'

        self.bancoDados = bd()

        #INICIALIZA A LISTA DE LEGENDAS
        self.setListSubtitles()

        #TOCA O AUDIO
        self.playMusic(0)

        self.windowGame()

    def playMusic(self, numberSlide):
        pygame.init()
        pygame.mixer.music.load(f'sound{numberSlide}.mp3')
        pygame.mixer.music.play()

    def setListSubtitles(self):

        #VARRE A LISTA DE LEGENDAS E PEGA O ITEM 0 DE CADA TUPLA
        for i in self.bancoDados.getSubtitles():
            self.listSubtitles.append(i[0])

        #print(self.listSubtitles)

    def windowGame(self):

        self.windowMain = Tk()
        self.windowMain.title('The Imitation Game')
        self.windowMain.geometry('1180x600')
        self.windowMain.resizable(False, False)
        self.setBackground()
        self.setbutons()

        self.windowMain.mainloop()

    def setbutons(self):
        if self.page == 'initial':
            self.btResum = Button(self.windowMain, text='Resum', width=7, height=2, font=self.fontDefault, command=self.nextSlide)
            self.btResum.place(x=160, y=225)

            self.btPersons = Button(self.windowMain, text='Persons', width=7, height=2, font=self.fontDefault, command=self.pagePersons)
            self.btPersons.place(x=160, y=285)

        elif self.page == 'slide':
            self.btBack = Button(self.Laa, text='Back', width=4, height=2, font=self.fontDefault, command=self.reset)
            self.btBack.place(x=1120, y=490)

            #BUTTON NEXT
            self.btNext = Button(self.Laa, text='Next', width=4, height=2, font=self.fontDefault, command=self.nextSlide)
            self.btNext.place(x=1120, y=540)

            #BUTTON PREV
            self.btPrev = Button(self.windowMain, text='Prev', width=4, height=2, font=self.fontDefault, command=self.prevSlide)
            self.btPrev.place(x=10, y=540)

        else:
            self.btBack = Button(self.Laa, text='Back', width=4, height=2, font=self.fontDefault, command=self.reset)
            self.btBack.place(x=1120, y=530)

    def updateApresentation(self):
        #MODIFICA A IMAGEM E A LEGENDA
        self.setBackground()

        self.setImagem(self.currentSlide)

        self.setSubtitle(self.currentSlide)

    #AVANÇA UM SLIDE
    def nextSlide(self):
        self.page = 'slide'
        #AVANÇA O SLIDE
        self.currentSlide += 1

        #VERIFICA SE AINDA EXISTE ALGUM SLIDE
        if self.currentSlide < len(self.listSubtitles):
            
            #ATUALIZA SLIDE
            self.updateApresentation()

        else:
            #QUANDO N EXSITIR SLIDE O VALOR CORRENTE VAI PARA O ULTIMO
            self.currentSlide = len(self.listSubtitles) - 1

    #VOLTA UM SLIDE
    def prevSlide(self):
        
        #VOLTA O SLIDE
        self.currentSlide -= 1

        #VERIFICA SE AINDA EXISTE ALGUM SLIDE
        if self.currentSlide > 0:

            #ATUALIZA SLIDE
            self.updateApresentation()

        else:
            #RESETA PARA A POSIÇÃO INICIAL
            self.currentSlide = 1

    #DESTROY A IMAGEM ANTERIOR SE EXISTIR
    def destroyImage(self):
        try:
            self.lblImage.destroy()
        except:
            pass

    #ATUALIZA O SLIDE COM BASE NO numberSlide
    def setImagem(self, numberSlide):

        #DESTROY A IMAGEM PARA CRIAR OUTRA
        self.destroyImage()

        #IMAGEM

        self.img = PhotoImage(file=f'{numberSlide}.png')
        self.lblImage = Label(self.Laa, text='', image=self.img)
        self.lblImage.place(x=500, y=250)

    def alignSubtitle(self, s):
        nString = ''

        #PULA UMA LINHA A CADA 60 CARACTERE
        for i in s:

            if len(nString)%60 == 0 and len(nString) > 0:
                nString += i + '\n'

            else:
                nString += i

        return nString
    
    def setBackground(self):
        try:
            self.Laa.destroy()
        except:
            pass

        self.imag = PhotoImage(file=f"{self.page}.png")
        if self.currentSlide ==1:
            self.imag = PhotoImage(file=f"{self.page}.png")
        self.Laa = Label(self.windowMain, image = self.imag)
        self.Laa.pack()
        self.setbutons()

    def setSubtitle(self, numberSlide):

        #ATUALIZA A LEGENDA COM BASE NO NUMERO DO SLIDE
        string  = self.listSubtitles[numberSlide]

        self.lblSubtitle['text'] = self.alignSubtitle(string)

    def reset(self):
        self.currentSlide = 0
        self.page = 'initial'
        self.setBackground()

    def pagePersons(self):
        self.page = 'person'
        self.setBackground()

if __name__ == "__main__":
    interface()    