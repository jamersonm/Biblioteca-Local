import customtkinter as ctk
from PIL import Image
import os

class TelaHome(ctk.CTkScrollableFrame):
    def __init__(self, master, db):
        super().__init__(master,
                         fg_color="transparent",
                         scrollbar_button_color="#2E3440",
                         scrollbar_button_hover_color="#4C566A",
                         )
        self.db = db
       

        # Bind do scroll do mouse para sistemas Linux/Arch
        # Botão 4 é Scroll Up, Botão 5 é Scroll Down no Linux
        self.bind_all("<Button-4>", lambda e: self._parent_canvas.yview_scroll(-1, "units"))
        self.bind_all("<Button-5>", lambda e: self._parent_canvas.yview_scroll(1, "units"))

        self.alpha = 0.0
        self.exibir_com_suavidade()

        # Configuração de grid para centralizar o conteúdo na tela
        self.grid_columnconfigure(0, weight=1)
        
        self.setup_ui()


    def exibir_com_suavidade(self):
        if self.alpha < 1.0:
            self.alpha += 0.1
            # Simulamos o fade mudando a cor do texto para tons de cinza do Nord
            # Ou simplesmente usamos o after para um delay de entrada
            self.after(20, self.exibir_com_suavidade)

               

    def setup_ui(self):
        # 1. Títulos
        self.label_titulo = ctk.CTkLabel(self, text="Biblioteca Local", font=("JetBrains Mono", 42, "bold"))
        self.label_titulo.grid(row=0, column=0, pady=(60, 5))

        self.label_subtitulo = ctk.CTkLabel(self, text="Seu gerenciador de acervo de livros fora da linha", 
                                           font=("JetBrains Mono", 16), text_color="#81A1C1")
        self.label_subtitulo.grid(row=1, column=0, pady=(0, 40))

        # 2. Card Principal (Container)
        self.card_principal = ctk.CTkFrame(self, fg_color="#3B4252", corner_radius=10)
        self.card_principal.grid(row=2, column=0, padx=40, pady=(0, 60)) 
        self.card_principal.grid_columnconfigure((0, 1), weight=0) # Mantém eles "juntos" no centro

        # Tamanho Base (Seguro para a maioria das telas)
        LADO = 320
        
        # 3. Quadrado da Logo
        self.frame_logo_bg = ctk.CTkFrame(self.card_principal, fg_color="#2E3440", 
                                         corner_radius=10, width=LADO, height=LADO)
        self.frame_logo_bg.grid(row=0, column=0, padx=(15, 7), pady=15)
        self.frame_logo_bg.grid_propagate(False) 
        
        try:
            self.img_logo = ctk.CTkImage(Image.open("assets/icons/chess-rook.png"), size=(180, 180))
            self.label_logo = ctk.CTkLabel(self.frame_logo_bg, image=self.img_logo, text="")
            self.label_logo.place(relx=0.5, rely=0.5, anchor="center")
        except:
            self.label_logo = ctk.CTkLabel(self.frame_logo_bg, text="LOGO", font=("JetBrains Mono", 24))
            self.label_logo.place(relx=0.5, rely=0.5, anchor="center")
        
        # 4. Quadrado da Citação
        self.frame_citacao_bg = ctk.CTkFrame(self.card_principal, fg_color="#434C5E", 
                                            corner_radius=10, width=LADO, height=LADO)
        self.frame_citacao_bg.grid(row=0, column=1, padx=(7, 15), pady=15)
        self.frame_citacao_bg.grid_propagate(False) 
        
        self.label_texto_citacao = ctk.CTkLabel(
            self.frame_citacao_bg, 
            #text='"A leitura de todos os bons livros é como uma conversa com as melhores mentes dos séculos passados."', 
            text='"Devemos, pois, evitar as palavras inúteis sem cair no laconismo exagerado, incompatível com a delicadeza."',
            font=("JetBrains Mono", 18, "italic"),
            text_color="#D8DEE9",
            wraplength=LADO - 60, # Define o limite inicial para não cortar
            justify="center"
        )
        self.label_texto_citacao.place(relx=0.5, rely=0.45, anchor="center")
        
        #self.label_autor = ctk.CTkLabel(self.frame_citacao_bg, text="- René Descartes", 
        #                               font=("JetBrains Mono", 14, "bold"), text_color="#81A1C1")
        self.label_autor = ctk.CTkLabel(self.frame_citacao_bg, text="- Beremiz Samir", 
                                       font=("JetBrains Mono", 14, "bold"), text_color="#81A1C1")

        self.label_autor.place(relx=0.5, rely=0.75, anchor="center") 

    
