from tkinter import *
import pyautogui, threading

class Aplication :
    def __init__(self, master=None):
        self.running = False
        
        self.mensagem = Frame(master)
        self.mensagem.pack()
        self.msg = Label(self.mensagem, text = "AFK Senior", bg="white")
        self.msg["font"] = ("Arial", "20", "bold")
        self.msg["pady"] = 25
        self.msg.pack()

        self.fontePadrao = ("Arial", "10")
        self.primeiroContainer = Frame(master, bg="white")
        self.primeiroContainer["padx"] = 10
        self.primeiroContainer["pady"] = 5
        self.primeiroContainer.pack()

        self.segundoContainer = Frame(master, bg="white")
        self.segundoContainer["padx"] = 10
        self.segundoContainer["pady"] = 5
        self.segundoContainer.pack()

        self.terceiroContainer = Frame(master, bg="white")
        self.terceiroContainer["padx"] = 10
        self.terceiroContainer["pady"] = 5
        self.terceiroContainer.pack()

        self.iniciar = Button(self.primeiroContainer, bg="chartreuse3")
        self.iniciar["text"] = "Iniciar"
        self.iniciar["font"] = ("Calibri", "15", "bold")
        self.iniciar["width"] = 20
        self.iniciar["height"] = 2
        self.iniciar["command"] = self.iniciarAutomacao
        self.iniciar.pack()

        self.parar = Button(self.segundoContainer, bg="orange2")
        self.parar["text"] = "Parar"
        self.parar["font"] = ("Calibri", "15", "bold")
        self.parar["width"] = 20
        self.parar["height"] = 2
        self.parar["command"] = self.pararAutomacao
        self.parar.pack()

        self.sair = Button(self.terceiroContainer, bg="firebrick2")
        self.sair["text"] = "Sair"
        self.sair["font"] = ("Calibri", "15", "bold")
        self.sair["width"] = 20
        self.sair["height"] = 2
        self.sair["command"] = self.sair.quit
        self.sair.pack()

    def iniciarAutomacao(self):
        self.running = True
        threading.Thread(target=self.Automacao, daemon=True).start()

    def pararAutomacao(self):
        self.running = False

    def Automacao(self):
                pyautogui.press('win')
                pyautogui.sleep(1)
                pyautogui.write('aplicativo: bloco de notas')
                pyautogui.sleep(1)
                pyautogui.press('enter')
                while self.running == True:
                    pyautogui.sleep(2)
                    pyautogui.write('Trabalhando ')
                    pyautogui.sleep(2)
                    pyautogui.moveTo(300, 200)
                    pyautogui.sleep(2)
                    pyautogui.moveTo(600,200)

                 
            

                  


root = Tk()
Aplication(root)
root.geometry("240x340+550+100")
root.configure(bg="white")
root.title("AFK Senior")
root.mainloop()