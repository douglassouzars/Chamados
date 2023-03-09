from tkinter import *   #pip install tk
import customtkinter as ctk    #pip install customtkinter
from tkinter import ttk
import pyperclip as pc    #pip install pyperclip


root = Tk()
class Aplicacao():
    def __init__(self):
        self.root = root
        self.tela()
        self.frames()
        self.Abas()
        self.conteudo_fixo()

    def tela(self):
        self.root.title("SISTEMA DEINF")
        self.root.configure(background='#353535')
        self.root.geometry("1060x800")
        self.root.resizable(True, True)
        self.root.minsize(850,600)

    def frames(self):
        self.frame_1 = Frame(self.root)
        self.frame_1.configure(background='#5c5a58')
        self.frame_1.place(relx= 0.49, rely=0.008, relwidth= 0.505, relheight= 0.98)
        self.frame_2 = ttk.Notebook(self.root)
        ttk.Style().configure("TNotebook", background='#353535')
        self.frame_2.place(relx= 0.495, rely=0.012, relwidth= 0.496, relheight= 0.97)


    def conteudo_fixo(self):
        def copiar():
            #self.clipboard_clear()
            self.clipboard_append(detalhamento_text.get)
        def labeis_fixo():
            assunto = Label(self.root,text="Assunto")
            assunto.configure(background='#353535',fg='white',font='TimesNewRoman 12 bold')
            assunto.place(relx=0.005,rely=0.01)
            detalhamento = Label(self.root, text="Detalhamento")
            detalhamento.configure(background='#353535', fg='white', font='TimesNewRoman 12 bold')
            detalhamento.place(relx=0.005, rely=0.085)
            texto1 = Label(self.root, text="Classificação CORRETA")
            texto1.configure(background='#353535', fg='white', font='TimesNewRoman 10 bold')
            texto1.place(relx=0.005, rely=0.6)
            texto2 = Label(self.root, text="Tipo de chamado:  --")
            texto2.configure(background='#353535', fg='white', font='TimesNewRoman 10 bold')
            texto2.place(relx=0.005, rely=0.63)
            texto3 = Label(self.root, text="Nível 1:  --")
            texto3.configure(background='#353535', fg='white', font='TimesNewRoman 10 bold')
            texto3.place(relx=0.068, rely=0.66)
            texto4 = Label(self.root, text="Nível 2:  --")
            texto4.configure(background='#353535', fg='white', font='TimesNewRoman 10 bold')
            texto4.place(relx=0.068, rely=0.69)
            texto5 = Label(self.root, text="Nível 3:  --")
            texto5.configure(background='#353535', fg='white', font='TimesNewRoman 10 bold')
            texto5.place(relx=0.068, rely=0.72)
            texto6 = Label(self.root, text="Nível 4:  --")
            texto6.configure(background='#353535', fg='white', font='TimesNewRoman 10 bold')
            texto6.place(relx=0.068, rely=0.75)
            texto7 = Label(self.root, text="Atenção:  --")
            texto7.configure(background='#353535', fg='red', font='TimesNewRoman 12 bold')
            texto7.place(relx=0.045, rely=0.78)
            texto8 = Label(self.root, text="OBS: Em caso de dúvidas,consultar Líder Técnico ou Supervisor")
            texto8.configure(background='#353535', fg='red', font='TimesNewRoman 10 bold')
            texto8.place(relx=0.005, rely=0.81)
            procedimentos = Label(self.root, text="Procedimentos e Observações")
            procedimentos.configure(background='#353535', fg='white', font='TimesNewRoman 12 bold')
            procedimentos.place(relx=0.12, rely=0.84)
        def botoes_fixo():
            btn_copy = ctk.CTkButton(self.root, text='Copiar', fg_color='#c8c0b7', text_color='Black',font=('Arial', 14))
            # btn_copy.configure(background='#c8c0b7', font='TimesNewRoman 12 bold',bd='5')
            btn_copy.place(relx=0.42, rely=0.086, relwidth=0.065, relheight=0.038)
            btn_limpar = ctk.CTkButton(self.root, text='Limpar', fg_color='#c8c0b7', text_color='Black',font=('Arial', 14))
            # btn_limpar.configure(background='#c8c0b7', font='TimesNewRoman 12 bold')
            btn_limpar.place(relx=0.18, rely=0.545, relwidth=0.11, relheight=0.04)
            btn_encaminhar = ctk.CTkButton(self.root, text='Encaminhar', fg_color='#c8c0b7', text_color='Black', font=('Arial', 14))
            # btn_encaminhar.configure(background='#c8c0b7',fg='Red' , font='TimesNewRoman 12 bold')
            btn_encaminhar.place(relx=0.30, rely=0.545, relwidth=0.11, relheight=0.04)
            btn_copy2 = ctk.CTkButton(self.root, text='Copiar',command='copiar',fg_color='#c8c0b7', text_color='Black', font=('Arial', 14))
            # btn_copy2.configure(background='#c8c0b7', font='TimesNewRoman 12 bold')
            btn_copy2.place(relx=0.42, rely=0.545, relwidth=0.065, relheight=0.04)
        def entradas_fixo():
            assunto_entry = Entry(self.root)
            assunto_entry.place(relx=0.005,rely=0.045,relwidth=0.48,relheight=0.03)
            detalhamento_text = Text(self.root)
            detalhamento_text.insert(END, 'Nome:\nRamal:\nPatrimônio:\nIp:\nSetor:\nDiretoria:\n\nDados confirmados com o(a) usuário(a).')
            detalhamento_text.place(relx=0.005,rely=0.134, relwidth=0.48,relheight=0.4)
            procedimentos_entry = Text(self.root)
            procedimentos_entry.place(relx=0.005,rely=0.87, relwidth=0.48,relheight=0.12)
    #Chamar as funções
        labeis_fixo()
        botoes_fixo()
        entradas_fixo()
    def Abas(self):
        def aba_informacoes():
            self.aba1=Frame(self.frame_2)
            self.aba1.configure(background='#353535')
            self.frame_2.add(self.aba1,text="  Informações  ")
            ramais = Label(self.aba1, text="Ramais Úteis")
            ramais.configure(background='#353535', fg='red', font='TimesNewRoman 12 bold')
            ramais.place(relx=0.005, rely=0.01)
            self.frame_3 = Frame(self.aba1)
            self.frame_3.configure(background='#7c7976')
            self.frame_3.place(relx=0.01, rely=0.05, relwidth=0.98, relheight=0.46)
            inf = Label(self.aba1, text="Informações Importante")
            inf.configure(background='#353535', fg='red', font='TimesNewRoman 12 bold')
            inf.place(relx=0.005, rely=0.52)
            self.frame_3 = Frame(self.aba1)
            self.frame_3.configure(background='#7c7976')
            self.frame_3.place(relx=0.01, rely=0.56, relwidth=0.98, relheight=0.5)


        def aba_atalhos():
            self.aba2=Frame(self.frame_2)
            self.aba2.configure(background='#7c7976')
            self.frame_2.add(self.aba2,text="  Atalhos  ")
            at = Label(self.aba2, text="EM PRODUÇÃO")
            at.configure(background='#7c7976', fg='black', font='TimesNewRoman 20 bold')
            at.place(relx=0.30, rely=0.5)

        def aba_n1():
            self.aba3 = Frame(self.frame_2)
            self.aba3.configure(background='#7c7976')
            self.frame_2.add(self.aba3, text="  Nível 1  ")
        def aba_n2():
            self.aba4 = Frame(self.frame_2)
            self.aba4.configure(background='#7c7976')
            self.frame_2.add(self.aba4, text="  Nível 2  ")
        def aba_n3():
            self.aba5 = Frame(self.frame_2)
            self.aba5.configure(background='#7c7976')
            self.frame_2.add(self.aba5, text="  Nível 3  ")
        def aba_chamados():
            self.aba6 = Frame(self.frame_2)
            self.aba6.configure(background='#7c7976')
            self.frame_2.add(self.aba6, text="  Chamados Filhos  ")
            cf = Label(self.aba6, text="EM PRODUÇÃO")
            cf.configure(background='#7c7976', fg='black', font='TimesNewRoman 20 bold')
            cf.place(relx=0.30, rely=0.5)
    #Chamar as funções
        aba_informacoes()
        aba_atalhos()
        aba_n1()
        aba_n2()
        aba_n3()
        aba_chamados()

Aplicacao()
root.mainloop()