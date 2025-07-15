from tkinter import *
import pyautogui

class Aplication :
    def __init__(self, master=None):
        self.mensagem = Frame(master)
        self.mensagem.pack()
        self.msg = Label(self.mensagem, text = "AFK Senior")
        self.msg.pack()

        self.fontePadrao = ("Arial", "10")
        self.primeiroContainer = Frame(master)
        self.primeiroContainer["padx"] = 10
        self.primeiroContainer["pady"] = 10
        self.primeiroContainer.pack()

        self.segundoContainer = Frame(master)
        self.segundoContainer["padx"] = 10
        self.segundoContainer["pady"] = 10
        self.segundoContainer.pack()

        self.iniciar = Button(self.primeiroContainer)
        self.iniciar["text"] = "Iniciar"
        self.iniciar["font"] = ("Calibri", "8")
        self.iniciar["width"] = 12
        self.iniciar["command"] = self.Automação
        self.iniciar.pack()

        self.sair = Button(self.segundoContainer)
        self.sair["text"] = "Parar"
        self.sair["font"] = ("Calibri", "8")
        self.sair["width"] = 12
        self.sair["command"] = self.sair.quit
        self.sair.pack()

    def Automação(self):
                pyautogui.press('win')
                pyautogui.sleep(1)
                pyautogui.write('aplicativo: bloco de notas')
                pyautogui.sleep(1)
                pyautogui.press('enter')
                while True:
                    pyautogui.sleep(5)
                    pyautogui.write('Trabalhando ')
                    pyautogui.sleep(2)
                    pyautogui.moveTo(100, 200)
                    pyautogui.sleep(2)
                    pyautogui.moveTo(200,100)

                 
            

                  


root = Tk()
Aplication(root)
root.mainloop() 