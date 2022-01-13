from tkinter import *
from tkinter import ttk
import sqlite3
from tkcalendar import Calendar, DateEntry




root = Tk()
    

class Funcs():
    def limpa_tela(self):
        self.cod_entry.delete(0, END)
        self.data_entry.delete(0, END)
        self.nome_entry.delete(0, END)
        self.empresa_entry.delete(0, END) 
        self.hora_entry.delete(0, END)
        self.status_entry.delete(0, END)
        self.nf_entry.delete(0, END)
        self.dataNf_entry.delete(0, END)
        self.fornecedor_entry.delete(0, END)
        self.pedido_entry.delete(0, END)
        self.requisitante_entry.delete(0, END)
        self.departamento_entry.delete(0, END)          
    def conecta_bd(self):
        self.conn =sqlite3.connect("almox.bd")
        self.cursor = self.conn.cursor(); print("Conectando ao banco de dados")
    def desconecta_bd(self):
        self.conn.close(); print("Desconectando ao banco de dados")
    def montaTabelas(self):
        self.conecta_bd() 

        ###Criar tabela
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS info (
                cod INTEGER PRIMARY KEY,
                data INTEGER(10) NOT NULL,
                nome CHAR(40) NOT NULL,
                empresa CHAR(20) NOT NULL,
                hora INTEGER(10) NOT NULL,
                status TEXT NOT NULL,
                nf INTEGER NOT NULL,
                dataNf INTEGER(10) NOT NULL,
                fornecedor CHAR(20) NOT NULL,
                pedido INTEGER NOT NULL,
                requisitante CHAR(40) NOT NULL,
                departamento CHAR(20) NOT NULL
                
            ); 

        """)
        self.conn.commit(); print("Banco de dados criado")
        self.desconecta_bd()
    def variaveis(self):
        self.cod = self.cod_entry.get()
        self.data = self.data_entry.get()
        self.nome = self.nome_entry.get()
        self.empresa = self.empresa_entry.get()
        self.hora = self.hora_entry.get()
        self.status = self.status_entry.get()
        self.nf = self.nf_entry.get()
        self.dataNf = self.dataNf_entry.get()
        self.fornecedor = self.fornecedor_entry.get()
        self.pedido = self.pedido_entry.get()
        self.requisitante = self.requisitante_entry.get()
        self.departamento = self.nome_entry.get()
    def add(self):
        self.variaveis()
        self.conecta_bd()

        self.cursor.execute("""INSERT INTO info (cod,data, nome, empresa, hora, status, nf, dataNf, fornecedor, pedido, requisitante, departamento)
        VALUES (?,?,?,?,?,?,?,?,?,?,?)""", (self.cod,self.data,self.nome,self.empresa,self.hora,self.status,self.nf,self.dataNf,self.fornecedor,self.pedido,self.requisitante,self.departamento))
        self.conn.commit()
        self.desconecta_bd()
        self.select_lista()
        self.limpa_tela()
    def select_lista(self):
        self.listaCli.delete(*self.listaCli.get_children())
        self.conecta_bd()
        lista = self.cursor.execute("""SELECT cod, data, nome, empresa, hora, status, nf, dataNf, fornecedor, pedido, requisitante, departamento from info
            ORDER BY data ASC; """)
        for i in lista:
            self.listaCli.insert("", END, values=i)
        self.desconecta_bd()
    def calendario(self):
        self.calendario1 = Calendar(self.aba1, fg="gray75", bg="blue",
            font=("Times", '9', 'bold'), locale='pt_br')
        self.calendario1.place(relx=0.65, rely=0.2)
        self.calData = Button(self.aba1,text="Selecione a data", command= self.print_cal)
        self.calData.place(relx=0.65,rely=0.57, height=25,width=100)
    def print_cal(self):
        dataIni = self.calendario1.get_date()
        self.calendario1.destroy()
        self.entry_data.delete(0, END)
        self.entry_data.insert(END, dataIni)
        self.calData.destroy()
    def calendar1(self):
        self.calendar2 = Calendar(self.aba1, fg="gray75", bg="blue",
            font=("Times", '9', 'bold'), locale='pt_br')
        self.calendar2.place(relx=0.65, rely=0.2)
        self.calDatainicio = Button(self.aba1, text= "Inserir data",
            command= self.print_cal1 )
        self.calDatainicio.place(relx=0.65,rely=0.57, height=25,width=100)
    def print_cal1(self):
        dataIni1 =self.calendar2.get_date()
        self.calendar2.destroy()
        self.entry_data1.delete(0, END)
        self.entry_data1.insert(END, dataIni1)
        self.calDatainicio.destroy()      

    
class Application(Funcs):
    def __init__(self):
        self.root = root
        self.tela()
        self.frames_da_tela()
        self.abas1()
        self.abas2()
        self.montaTabelas()
        root.mainloop()
    def tela(self):              
        self.root.title("Formulário de Encaminhamento de Materiais")
        self.root.configure(background='#1e3743')
        self.root.geometry("700x500")
        self.root.resizable(True,True)
        self.root.maxsize(width=900, height=700)
        self.root.minsize(width=500,height=450)
    def frames_da_tela(self):
        self.frame_1 = Frame(self.root,bg='gray')
        self.frame_1.place(relx=0.02,rely=0.02,relwidth=0.96,relheight=0.96)
    def abas1(self):
        #criando Abas
        self.abas = ttk.Notebook(self.frame_1)
        self.aba1 = Frame(self.abas)
        self.aba2 = Frame(self.abas)
        self.aba3 = Frame(self.abas)

        self.aba1.configure(background= "gray")
        self.aba2.configure(background= "gray75")
        self.aba3.configure(background= "lightgray")

        self.abas.add(self.aba1, text = "Novo cadastro")
        self.abas.add(self.aba2, text = "lista")
        self.abas.add(self.aba3, text = "consulta")

        self.abas.place(relx=0, rely=0, relwidth=1, relheight=1)

        #botão de salvar
        self.bt_salvar = Button(self.aba1, text="Salvar",bg ='#107db2',fg='white',font=13, command=self.add)
        self.bt_salvar.place(relx=0.75,rely=0.9,relwidth=0.1,relheight=0.07)
        #botão de limpar
        self.bt_limpar = Button(self.aba1, text="Limpar",bg ='#107db2',fg='white',font=13, command= self.limpa_tela)
        self.bt_limpar.place(relx=0.87,rely=0.9,relwidth=0.1,relheight=0.07)

         #criação da label e entradado Calendario(Data)
        self.lb_calendario = Label(self.aba1, text ="Data / Date",bg ='gray',fg='white')
        self.lb_calendario.place(relx=0.03, rely=0.05)
        self.bt_calendario = Button(self.aba1, text ="...", command= self.calendario)
        self.bt_calendario.place(relx=0.35, rely=0.05,relwidth=0.03,relheight=0.05)
        self.entry_data = Entry(self.aba1, width= 20)
        self.entry_data.place(relx=0.15, rely=0.05)

         #criação da label e entradado Nome
        self.lb_nome = Label(self.aba1, text ="Nome",bg ='gray',fg='white')
        self.lb_nome.place(relx=0.03, rely=0.15)
        self.nome_entry = Entry(self.aba1)
        self.nome_entry.place(relx=0.15, rely=0.15, relwidth=0.4)

        #criação da label e entradado Empresa
        self.lb_empresa = Label(self.aba1, text ="Empresa",bg ='gray',fg='white')
        self.lb_empresa.place(relx=0.03, rely=0.25)
        self.empresa_entry = Entry(self.aba1)
        self.empresa_entry.place(relx=0.15, rely=0.25, relwidth=0.4)

        #criação da label e entrada da Nf
        self.lb_nf = Label(self.aba1, text ="NF",bg ='gray',fg='white')
        self.lb_nf.place(relx=0.03, rely=0.35)
        self.nf_entry = Entry(self.aba1)
        self.nf_entry.place(relx=0.15, rely=0.35, relwidth=0.28)

        #criação da label e entrada do Fornecedor
        self.lb_dataNf = Label(self.aba1, text ="Data da NF",bg ='gray',fg='white')
        self.lb_dataNf.place(relx=0.55, rely=0.35)
        self.bt_dataNf = Button(self.aba1, text ="...", command= self.calendar1)
        self.bt_dataNf.place(relx=0.95, rely=0.35,relwidth=0.03,relheight=0.05)
        self.entry_data1 = Entry(self.aba1,width=20)
        self.entry_data1.place(relx=0.7, rely=0.35)

        #criação da label e entrada do Fornecedor
        self.lb_fornecedor = Label(self.aba1, text ="Fornecedor",bg ='gray',fg='white')
        self.lb_fornecedor.place(relx=0.03, rely=0.45)
        self.fornecedor_entry = Entry(self.aba1)
        self.fornecedor_entry.place(relx=0.15, rely=0.45, relwidth=0.28)

        #criação da label e entrada do Pedido
        self.lb_pedido = Label(self.aba1, text ="Pedido",bg ='gray',fg='white')
        self.lb_pedido.place(relx=0.55, rely=0.45)
        self.pedido_entry = Entry(self.aba1)
        self.pedido_entry.place(relx=0.7, rely=0.45, relwidth=0.28)

        #criação da label e entrada do Requisitante
        self.lb_requisitante = Label(self.aba1, text ="Requisitante",bg ='gray',fg='white')
        self.lb_requisitante.place(relx=0.03, rely=0.55)
        self.requisitante_entry = Entry(self.aba1)
        self.requisitante_entry.place(relx=0.15, rely=0.55, relwidth=0.28)

        #criação da label e entrada do Departamento
        self.lb_departamento = Label(self.aba1, text ="Departamento",bg ='gray',fg='white')
        self.lb_departamento.place(relx=0.55, rely=0.55)
        self.departamento_entry = Entry(self.aba1)
        self.departamento_entry.place(relx=0.7, rely=0.55, relwidth=0.28)

        #criação da label e entrada da Hora de saida
        self.lb_hora = Label(self.aba1, text ="Hora de saida",bg ='gray',fg='white')
        self.lb_hora.place(relx=0.7, rely=0.05)
        self.hora_entry = Entry(self.aba1)
        self.hora_entry.place(relx=0.83, rely=0.05, relwidth=0.15)
        
        #criação da label e entrada da liberação
        style= ttk.Style()
        style.theme_use('clam')
        style.configure("TCombobox", bg="#d9d9d9")
        comboStatus = ttk.Combobox(self.aba1,font=("Times", 13), values=["Liberado","Não Liberado" ],state="readonly")
        print(dict(comboStatus)) 
        comboStatus.current(1)
        comboStatus.place(relx=0.5,rely=0.9,relwidth=0.18,relheight=0.07)
    def abas2(self):
        self.listaCli = ttk.Treeview(self.aba2, height = 3, column=("col1", "col2", "col3", "col4", "col5", "col6", "col7", "col8", "col9", "col10", "col11"))
        self.listaCli.heading("#0", text="")
        self.listaCli.heading("#1", text="Data")
        self.listaCli.heading("#2", text="Nome")
        self.listaCli.heading("#3", text="Empresa")
        self.listaCli.heading("#4", text="Hora")
        self.listaCli.heading("#5", text="Status")
        self.listaCli.heading("#6", text="NF")
        self.listaCli.heading("#7", text="DataNF")
        self.listaCli.heading("#8", text="Fornecedor")
        self.listaCli.heading("#9", text="Pedido")
        self.listaCli.heading("#10", text="Requisitante")
        self.listaCli.heading("#11", text="Departamento")

        self.listaCli.column("#0", width=1)
        self.listaCli.column("#1", width=50)
        self.listaCli.column("#2", width=125)
        self.listaCli.column("#3", width=125)
        self.listaCli.column("#4", width=50)
        self.listaCli.column("#5", width=125)
        self.listaCli.column("#6", width=125)
        self.listaCli.column("#7", width=125)
        self.listaCli.column("#8", width=125)
        self.listaCli.column("#9", width=125)
        self.listaCli.column("#10", width=125)
        self.listaCli.column("#11", width=125)

        self.listaCli.place(relx=0.01, rely=0.1, relwidth=0.95, relheight=0.85)

        self.scroolLista = Scrollbar(self.aba2, orient="vertical")
        self.listaCli.configure(yscroll=self.scroolLista.set)
        self.scroolLista.place(relx=0.97, rely=0.1, relwidth=0.02, relheight=0.85)
        #self.listaCli.bind("<Double-1>", self.OnDoubleClick) 


    
            

    

Application()