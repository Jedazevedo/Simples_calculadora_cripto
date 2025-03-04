import tkinter as tk
import tkinter.font as tkfont
import tkinter.ttk as ttk
from PIL import ImageTk, Image
from pathlib import Path

'''clique sob a pasta img e copie o caminho da pasta para PATH_IMG abaixo '''
PATH_IMG = "C:\\Users\\tec-s\OneDrive\\Área de Trabalho\\app_calculadora\\calculadora\Simples_calculadora_cripto\\img\\"

caminho = Path(__file__).parent/f"{PATH_IMG}cripto.ico"
cima    = Path(__file__).parent/f"{PATH_IMG}alta.ico"
baixo   = Path(__file__).parent/f"{PATH_IMG}baixa.ico"
percent = Path(__file__).parent/f"{PATH_IMG}percent.ico"
preco   = Path(__file__).parent/f"{PATH_IMG}preco.ico"
invest  = Path(__file__).parent/f"{PATH_IMG}invest.ico"
cotas   = Path(__file__).parent/f"{PATH_IMG}cotas.ico"
lucro   = Path(__file__).parent/f"{PATH_IMG}lucro.ico"

moeda       = Path(__file__).parent/f"{PATH_IMG}moeda.ico"
investimento= Path(__file__).parent/f"{PATH_IMG}investimento.ico"
software    = Path(__file__).parent/f"{PATH_IMG}software.ico"


janela = tk.Tk()
janela.title("Calculadora Invest")
janela.geometry("650x300")
janela.iconbitmap(caminho)


stellar_img= ImageTk.PhotoImage(Image.open(caminho))
cima_img   = ImageTk.PhotoImage(Image.open(cima))
baixo_img  = ImageTk.PhotoImage(Image.open(baixo))
percent_img= ImageTk.PhotoImage(Image.open(percent))
preco_img  = ImageTk.PhotoImage(Image.open(preco))
invest_img = ImageTk.PhotoImage(Image.open(invest))
cotas_img  = ImageTk.PhotoImage(Image.open(cotas))
lucro_img  = ImageTk.PhotoImage(Image.open(lucro))
moeda_img  = ImageTk.PhotoImage(Image.open(moeda))
investimento_img  = ImageTk.PhotoImage(Image.open(investimento))
software_img  = ImageTk.PhotoImage(Image.open(software))


# LABEL ENTRADA XLM
frame_labels = tk.Frame(janela, bg='#EDE7F6')
frame_labels.place(x=0, y=0, height=300, width=330)

fonte = tkfont.Font(family="Helvetica", size=12, weight="bold")
apresentacao = tk.Label(frame_labels,
                                text="Entrada de valores Cripto",
                                background='#673AB7',
                                height=3,fg='white',
                                font=fonte)
apresentacao.place(x=0, y=0, width=330)


fonte_labs = tkfont.Font(family="Helvetica", size=8, weight="bold")
software_logo = tk.Label(frame_labels,
                        image=software_img,
                        bg='#673AB7')
software_logo.place(x=10, y=13)
valor_xlm = tk.Label(frame_labels,
                                text="Valor atual Moeda: ",
                                bg='#ececdd',
                                font=fonte_labs,
                                background='#EDE7F6')
valor_xlm.place(x=5, y=75)
VALOR_XLM = ttk.Entry(frame_labels)
VALOR_XLM.place(x=10, y=92)


valor_investido = tk.Label(frame_labels,
                                text="Valor Investido :",
                                font=fonte_labs,
                                background='#EDE7F6')
valor_investido.place(x=5, y=125)
VALOR_INVESTIDO = ttk.Entry(frame_labels)
VALOR_INVESTIDO.place(x=10, y=142)


valor_predendido_ganho = tk.Label(frame_labels,
                                text="Lucro desejado :",
                                font=fonte_labs,
                                background='#EDE7F6')
valor_predendido_ganho.place(x=5, y=175)
GANHO = ttk.Entry(frame_labels)
GANHO.place(x=10,y=192)


# MOEDA
plota_img_moeda = tk.Label(frame_labels,
                                image=moeda_img,
                                bg="#E8EAF6" )
plota_img_moeda.place(x=140, y=155)
valor_lucro_desejado = tk.Label(frame_labels,
                                text= f'Valor da Moeda R$: ',
                                background='#EDE7F6',
                                font=fonte_labs )
valor_lucro_desejado.place(x=160, y=155)

# INVESTIMENTO
plota_img_investemento = tk.Label(frame_labels,
                                image=investimento_img,
                                bg="#E8EAF6" )
plota_img_investemento.place(x=140, y=175)
valor_lucro_desejado = tk.Label(frame_labels,
                                text= f'Valor  Investido R$: ',
                                background='#EDE7F6',
                                font=fonte_labs )
valor_lucro_desejado.place(x=160, y=175)

# LUCRO DESEJADO
plota_img_lucro = tk.Label(frame_labels,
                                image=lucro_img,
                                bg="#E8EAF6" )
plota_img_lucro.place(x=140, y=195)
valor_lucro_desejado = tk.Label(frame_labels,
                                text= f'Lucro Desejado R$: ',
                                background='#EDE7F6',
                                font=fonte_labs )
valor_lucro_desejado.place(x=160, y=195)


def entrada(): 
        frame_labels_saidas = tk.Frame(janela, background='#E8EAF6')
        frame_labels_saidas.place(x=335, height=300, width=310)

        # IN SAÍDA
        saida = tk.Label(frame_labels_saidas, text=f"Cripto para ganho de R$: ", fg="white",bg='#3F51B5', font=fonte)
        saida.place(x=0, width=315, height=63)

        # SAIDA ESPERE CAIR INVESTIMENTOS
        saida_baixa = tk.Label(frame_labels_saidas, text= f'Espere cair até R$: ',bg="#E8EAF6",
                               font=fonte_labs )
        saida_baixa.place(x=26, y=75)
        plota_img_baixo = tk.Label(frame_labels_saidas, image=baixo_img, bg='#E8EAF6' )
        plota_img_baixo.place(x=5, y=73)

        # SAIDA VALOR ATUAL DA CRIPTO
        valor_inserido_xlm = tk.Label(frame_labels_saidas, text= f'Valor da cripto atual R$: ',font=fonte_labs,bg="#E8EAF6" )
        valor_inserido_xlm.place(x=26, y=105)
        plota_img_baixo = tk.Label(frame_labels_saidas, image=preco_img, bg='#E8EAF6' )
        plota_img_baixo.place(x=5, y=105)
        
        # SAIDA ESPERE SUBIR ATÉ...
        saida_alta = tk.Label(frame_labels_saidas, text= f'Compre em:  e espere subir até R$: ',
                              font=fonte_labs, bg="#E8EAF6")
        saida_alta.place(x=26, y=137)
        plota_img_cima = tk.Label(frame_labels_saidas, image=cima_img, bg="#E8EAF6" )
        plota_img_cima.place(x=5, y=137)       

        # SAÍDA PORCENTAGEM        
        porcentagem_media = tk.Label(frame_labels_saidas,
                                     text= f'Porcentagem ± ',
                                     bg="#E8EAF6",
                                     font=fonte_labs )
        porcentagem_media.place(x=26, y=169) 
        plota_img_percent = tk.Label(frame_labels_saidas, image=percent_img, bg="#E8EAF6" )
        plota_img_percent.place(x=5, y=169)

            

        # VALOR SAIDA MENOS TAXA
        valor_investido = tk.Label(frame_labels_saidas, bg="#C5CAE9")
        valor_investido.place(x=0, y=225,height=280, width=315) 

        valor_investido = tk.Label(frame_labels_saidas, text=f"Valor investido menos taxa R$: ",
                                    font=fonte_labs,bg="#C5CAE9")
        valor_investido.place(x=26, y=235)
        plota_img_invest = tk.Label(frame_labels_saidas, image=invest_img, bg="#C5CAE9" )
        plota_img_invest.place(x=5, y=235)
        

        # SAIDA DE COTAS NECESSARIAS
        cotas = tk.Label(frame_labels_saidas, text=f"Cotas: Unidade(s)",
                          font=fonte_labs, bg="#C5CAE9")
        cotas.place(x=26, y=265)
        plota_img_cotas = tk.Label(frame_labels_saidas, image=cotas_img, bg="#C5CAE9" )
        plota_img_cotas.place(x=5, y=265)

        
entrada()

def calculo_valor():
    try:
        xlm = VALOR_XLM.get()
        xlm = float(xlm.replace(',','.'))
        
        valor_entrada = VALOR_INVESTIDO.get()
        valor_entrada = float(valor_entrada.replace(',','.'))
        valor_final_ganho = float(GANHO.get()) + valor_entrada

        x_baixa = f'{((valor_entrada * xlm) / valor_final_ganho):.2f}'
        porcentagem_queda = ((float(x_baixa)*100)/xlm)-100

        frame_labels_saidas = tk.Frame(janela, background='#E8EAF6')
        frame_labels_saidas.place(x=335, height=300, width=310)

        # IN SAÍDA
        saida = tk.Label(frame_labels_saidas,
                        text=f"Cripto para ganho de R$: {valor_final_ganho}",
                        fg="white",bg='#3F51B5',
                        font=fonte)
        saida.place(x=0, width=315, height=63)


        # SAIDA ESPERE CAIR INVESTIMENTOS
        saida_baixa = tk.Label(frame_labels_saidas,
                        text= f'Espere cair até R$: {x_baixa}',
                        bg="#E8EAF6",
                        font=fonte_labs )
        saida_baixa.place(x=26, y=75)
        plota_img_baixo = tk.Label(frame_labels_saidas,
                        image=baixo_img,
                        bg='#E8EAF6' )
        plota_img_baixo.place(x=5, y=73)

        # SAIDA VALOR ATUAL DA CRIPTO
        valor_inserido_xlm = tk.Label(frame_labels_saidas,
                        text= f'Valor da cripto atual R$: {xlm}',
                        font=fonte_labs,
                        bg="#E8EAF6" )
        valor_inserido_xlm.place(x=26, y=105)
        plota_img_baixo = tk.Label(frame_labels_saidas,
                        image=preco_img,
                        bg='#E8EAF6' )
        plota_img_baixo.place(x=5, y=105)
        
        # SAIDA ESPERE SUBIR ATÉ...
        saida_alta = tk.Label(frame_labels_saidas,
                        text= f'Compre em: {xlm} e espere subir até R$: {(xlm-float(x_baixa))+xlm:.2f}',
                        font=fonte_labs, bg="#E8EAF6")
        saida_alta.place(x=26, y=137)
        plota_img_cima = tk.Label(frame_labels_saidas,
                        image=cima_img,
                        bg="#E8EAF6" )
        plota_img_cima.place(x=5, y=137)       


        # SAÍDA PORCENTAGEM        
        porcentagem_media = tk.Label(frame_labels_saidas,
                        text= f'Porcentagem ± {porcentagem_queda:.2f}% ',
                        bg="#E8EAF6",
                        font=fonte_labs)
        porcentagem_media.place(x=26, y=169) 
        plota_img_percent = tk.Label(frame_labels_saidas,
                        image=percent_img,
                        bg="#E8EAF6" )
        plota_img_percent.place(x=5, y=169)

            

        # VALOR SAIDA MENOS TAXA
        valor_menos_taxa =  valor_entrada-valor_entrada*0.004 
        valor_investido = tk.Label(frame_labels_saidas, bg="#C5CAE9")
        valor_investido.place(x=0, y=225,height=280, width=315) 

        valor_investido = tk.Label(frame_labels_saidas,
                        text=f"Valor investido menos taxa R$: {valor_menos_taxa}",
                        font=fonte_labs,bg="#C5CAE9")
        valor_investido.place(x=26, y=235)
        plota_img_invest = tk.Label(frame_labels_saidas,
                        image=invest_img,
                        bg="#C5CAE9" )
        plota_img_invest.place(x=5, y=235)
        

        # SAIDA DE COTAS NECESSARIAS
        cotas = tk.Label(frame_labels_saidas,
                        text=f"Cotas: {valor_menos_taxa/xlm:.3f} Unidade(s)",
                        font=fonte_labs,
                        bg="#C5CAE9")
        cotas.place(x=26, y=265)

        plota_img_cotas = tk.Label(frame_labels_saidas,
                                    image=cotas_img,
                                    bg="#C5CAE9" )
        plota_img_cotas.place(x=5, y=265)


        # MOEDA
        plota_img_moeda = tk.Label(frame_labels,
                                        image=moeda_img,
                                        bg="#E8EAF6" )
        plota_img_moeda.place(x=140, y=155)
        valor_lucro_desejado = tk.Label(frame_labels,
                                        text= f'Valor da Moeda R$: {VALOR_XLM.get()}',
                                        background='#EDE7F6',
                                        font=fonte_labs )
        valor_lucro_desejado.place(x=160, y=155)


        # INVESTIMENTO
        plota_img_investemento = tk.Label(frame_labels,
                                        image=investimento_img,
                                        bg="#E8EAF6" )
        plota_img_investemento.place(x=140, y=175)
        valor_lucro_desejado = tk.Label(frame_labels,
                                        text= f'Valor  Investido R$: {VALOR_INVESTIDO.get()}',
                                        background='#EDE7F6',
                                        font=fonte_labs )
        valor_lucro_desejado.place(x=160, y=175)
     

        # LUCRO DESEJADO            
        plota_img_lucro = tk.Label(frame_labels,
                                image=lucro_img,
                                bg="#E8EAF6" )
        plota_img_lucro.place(x=140, y=195)
        
        valor_lucro_desejado = tk.Label(frame_labels,
                                        text= f'Lucro Desejado R$: {GANHO.get()}',         
                                        background='#EDE7F6',
                                        font=fonte_labs )
        valor_lucro_desejado.place(x=160, y=195)


        VALOR_XLM.delete(0, tk.END)
        VALOR_INVESTIDO.delete(0, tk.END)
        GANHO.delete(0, tk.END)

    except:

        saida = tk.Label(janela,
                        text=f"Impossível Calcular!! Sem parametro para calculo",
                        fg="#eb613b",
                        font="Arial, 10")
        saida.grid(row=0, column=2)

# FONTE FOOTER  
fonte_ = tkfont.Font(family="Helvetica",
                        size=7,
                        weight="bold")

desenvolvido = tk.Label(janela,
                        text="Developed by jedson",
                        font=fonte_,
                        bg='#D1C4E9')

desenvolvido.place(x=8, y=280)

# FONTE BOTÃO
fonte_btn = tkfont.Font(family="Helvetica",
                        size=10,
                        weight="bold"
                        )

# DECORAÇÃO BOTÃO
decorador_botao = tk.Label(frame_labels, bg="#D1C4E9")
decorador_botao.place(x=0, y=225,height=280, width=330) 
botao = tk.Button(frame_labels,
                 text="Calcular",
                 command = calculo_valor,
                 width=20,
                 font=fonte_btn,
                 bg='#673AB7',
                 fg='white')
botao.place(x=5, y=230)


janela.mainloop()