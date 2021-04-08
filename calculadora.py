#!/bin/python3

import tkinter as tk

class Botao(tk.Button):
    
    def __init__(self, funcao, parente, tela, valor=None, **kwargs):
        self.valor = valor
        self.tela = tela
        command=(lambda: funcao.gera_conta(self.tela, self.valor))
        super().__init__(parente, command = command, **kwargs)
        

class Botoes(tk.Frame):

    def __init__(self, parente=None):
        super().__init__(parente)
        self.botoes = {}
        self.parente = parente
        self.tela = tk.Label(parente, anchor='e', padx = 8, pady = 3)

    def botoes_basicos(self):
        tela = self.tela
        parente = self.parente
        funcao = Funcoes()
        values = {}
        for i in range(10):
            self.botoes['b'+str(i)] = Botao(funcao, parente, tela, str(i), text=str(i))
        labels = {'bdiv':'/','bx':'*','bmin':'-','bvir':',','bmais':'+',
                'bigual':'=','bcc':'cc'}
        for key, value in labels.items():
            self.botoes[key] = Botao(funcao, parente,tela, value, text=value)
        self._grid_botoes()
        
    def _grid_botoes(self):
        bot = self.botoes
        self.tela.grid(row=0,column=0, columnspan=5,sticky='news')
        bot['b7'].grid(row=1,column=0,sticky='news')
        bot['b8'].grid(row=1,column=1,sticky='news')
        bot['b9'].grid(row=1,column=2,sticky='news')
        bot['bdiv'].grid(row=1,column=3,sticky='news')
        bot['bcc'].grid(row=1,column=4,sticky='news')
        bot['b4'].grid(row=2,column=0,sticky='news')
        bot['b5'].grid(row=2,column=1,sticky='news')
        bot['b6'].grid(row=2,column=2,sticky='news')
        bot['bx'].grid(row=2,column=3,sticky='news')
        bot['bigual'].grid(row=2,column=4,rowspan=3,sticky='news')
        bot['b1'].grid(row=3,column=0,sticky='news')
        bot['b2'].grid(row=3,column=1,sticky='news')
        bot['b3'].grid(row=3,column=2,sticky='news')
        bot['bmin'].grid(row=3,column=3,sticky='news')
        bot['b0'].grid(row=4,column=0,columnspan=2,sticky='news')
        bot['bvir'].grid(row=4,column=2,sticky='news')
        bot['bmais'].grid(row=4,column=3,sticky='news')

    def grid(self,row=None,column=None):
        super().grid(row=row,column=column)

class Funcoes:

    def __init__(self):
        self.conta = ''
        self.apaga = True

    def gera_conta(self, tela, digito):
        if (not self.conta.endswith(('/','+','*','-')) 
            and digito in ('/','+','*','-')):
            self.conta = self.conta + digito
            self.apaga = False
        elif digito == 'cc':
            self.conta = ''
            self.apaga = False
        elif digito == '=':
            self.conta = self.conta.replace(',','.')
            self.conta = str(eval(self.conta)).replace('.',',')
            self.apaga = True
        elif digito == ',' and ',' not in self.conta:
            self.conta = self.conta + ','
        elif digito in [str(x) for x in range(10)]:
            if self.apaga:
                self.conta = ''
                self.apaga = False
            self.conta = self.conta + digito
        tela.config(text=self.conta)


janela = tk.Tk()
janela.title('Calculadora')
janela.resizable(False,False)

botoes = Botoes(janela)
botoes.botoes_basicos()
botoes.grid(row=0,column=0)

janela.mainloop()




















































