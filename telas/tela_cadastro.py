import customtkinter as ctk
from PIL import Image
import os

class TelaCadastro(ctk.CTkScrollableFrame):
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
        
        self.setup_ui()


    def exibir_com_suavidade(self):
        if self.alpha < 1.0:
            self.alpha += 0.1
            # Simulamos o fade mudando a cor do texto para tons de cinza do Nord
            # Ou simplesmente usamos o after para um delay de entrada
            self.after(20, self.exibir_com_suavidade)

               

    def setup_ui(self):
        # --- 1. CONFIGURAÇÃO DE PESOS DA TELA ---
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=0)

        # --- 2. CABEÇALHO E DIVISOR ---
        self.label_titulo_pagina = ctk.CTkLabel(
            self, text="Cadastro de Livro", font=("JetBrains Mono", 32, "bold")
        )
        self.label_titulo_pagina.grid(row=0, column=0, columnspan=2, padx=20, pady=(25, 15), sticky="w")

        self.linha_divisora = ctk.CTkFrame(self, height=2, fg_color="#4C566A")
        self.linha_divisora.grid(row=1, column=0, columnspan=2, padx=20, pady=(0, 30), sticky="ew")

        # --- 3. COLUNA DA ESQUERDA: CARDS DE ENTRADA ---

        # CARD 1: Título, Autor e ISBN (Row 2)
        self.card_input_principal = ctk.CTkFrame(self, fg_color="#3B4252", corner_radius=12)
        self.card_input_principal.grid(row=2, column=0, padx=(30, 15), pady=(0, 20), sticky="ew")
        self.card_input_principal.grid_columnconfigure(1, weight=1)

        self.label_titulo = ctk.CTkLabel(self.card_input_principal, text="Título", font=("JetBrains Mono", 32))
        self.label_titulo.grid(row=0, column=0, padx=(20, 10), pady=(20, 5), sticky="e")
        self.entry_titulo = ctk.CTkEntry(self.card_input_principal, font=("JetBrains Mono", 24), height=45)
        self.entry_titulo.grid(row=0, column=1, padx=(10, 20), pady=(20, 5), sticky="ew")

        self.label_autor = ctk.CTkLabel(self.card_input_principal, text="Autor", font=("JetBrains Mono", 32))
        self.label_autor.grid(row=1, column=0, padx=(20, 10), pady=5, sticky="e")
        self.entry_autor = ctk.CTkEntry(self.card_input_principal, font=("JetBrains Mono", 24), height=45)
        self.entry_autor.grid(row=1, column=1, padx=(10, 20), pady=5, sticky="ew")

        self.btn_buscar_isbn = ctk.CTkButton(self.card_input_principal, text="Buscar ISBN", font=("JetBrains Mono", 12, "bold"), fg_color="#5E81AC")
        self.btn_buscar_isbn.grid(row=2, column=0, padx=(20, 10), pady=(5, 20), sticky="e")
        self.entry_isbn = ctk.CTkEntry(self.card_input_principal, placeholder_text="ISBN (apenas números)", height=35)
        self.entry_isbn.grid(row=2, column=1, padx=(10, 20), pady=(5, 20), sticky="ew")

        # CARD 2: Dados Complementares 2x2 (Row 3)
        self.card_complementar = ctk.CTkFrame(self, fg_color="#3B4252", corner_radius=12)
        self.card_complementar.grid(row=3, column=0, padx=(30, 15), pady=(0, 20), sticky="ew")
        self.card_complementar.grid_columnconfigure((1, 3), weight=1)

        # Linha 0: Páginas e Gênero
        self.lbl_paginas = ctk.CTkLabel(self.card_complementar, text="Páginas")
        self.lbl_paginas.grid(row=0, column=0, padx=(20, 10), pady=(20, 10), sticky="e")
        self.ent_paginas = ctk.CTkEntry(self.card_complementar, height=35)
        self.ent_paginas.grid(row=0, column=1, padx=(0, 20), pady=(20, 10), sticky="ew")

        self.lbl_genero = ctk.CTkLabel(self.card_complementar, text="Gênero")
        self.lbl_genero.grid(row=0, column=2, padx=(20, 10), pady=(20, 10), sticky="e")
        self.ent_genero = ctk.CTkEntry(self.card_complementar, height=35)
        self.ent_genero.grid(row=0, column=3, padx=(0, 20), pady=(20, 10), sticky="ew")

        # Linha 1: Edição e Volume
        self.lbl_edicao = ctk.CTkLabel(self.card_complementar, text="Edição")
        self.lbl_edicao.grid(row=1, column=0, padx=(20, 10), pady=(10, 20), sticky="e")
        self.ent_edicao = ctk.CTkEntry(self.card_complementar, height=35)
        self.ent_edicao.grid(row=1, column=1, padx=(0, 20), pady=(10, 20), sticky="ew")

        self.lbl_volume = ctk.CTkLabel(self.card_complementar, text="Volume")
        self.lbl_volume.grid(row=1, column=2, padx=(20, 10), pady=(10, 20), sticky="e")
        self.ent_volume = ctk.CTkEntry(self.card_complementar, height=35)
        self.ent_volume.grid(row=1, column=3, padx=(0, 20), pady=(10, 20), sticky="ew")

        # CARD 3: Descrição (Row 4)
        self.card_descricao = ctk.CTkFrame(self, fg_color="#3B4252", corner_radius=12)
        self.card_descricao.grid(row=4, column=0, padx=(30, 15), pady=(0, 20), sticky="ew")
        self.card_descricao.grid_columnconfigure(0, weight=1)

        self.lbl_desc = ctk.CTkLabel(self.card_descricao, text="Descrição / Sinopse", font=("JetBrains Mono", 16, "bold"))
        self.lbl_desc.grid(row=0, column=0, padx=20, pady=(15, 5), sticky="w")
        self.txt_descricao = ctk.CTkTextbox(self.card_descricao, height=180, fg_color="#2E3440", border_width=1, border_color="#4C566A")
        self.txt_descricao.grid(row=1, column=0, padx=20, pady=(0, 20), sticky="ew")

        # --- 4. COLUNA DA DIREITA: CONTAINER ÚNICO (Capa + URL + Ações) ---
        L_CAPA, A_CAPA = 300, 420
        
        # O sticky="ns" é vital para o container esticar verticalmente acompanhando os cards da esquerda
        self.container_capa = ctk.CTkFrame(self, fg_color="transparent")
        self.container_capa.grid(row=2, column=1, rowspan=3, padx=(15, 30), sticky="ns")
        
        # 4.1 Frame do Preview (Topo)
        self.preview_capa_frame = ctk.CTkFrame(
            self.container_capa, 
            width=L_CAPA, 
            height=A_CAPA, 
            fg_color="#4C566A", 
            corner_radius=12
        )
        self.preview_capa_frame.pack(side="top", pady=(0, 15))
        self.preview_capa_frame.grid_propagate(False)
        
        self.lbl_capa_info = ctk.CTkLabel(
            self.preview_capa_frame, 
            text="Preview da Capa\n(300x420)", 
            font=("JetBrains Mono", 14)
        )
        self.lbl_capa_info.place(relx=0.5, rely=0.5, anchor="center")
        
        # 4.2 Sub-frame para URL e Botão OK
        self.frame_url_input = ctk.CTkFrame(self.container_capa, fg_color="transparent")
        self.frame_url_input.pack(side="top", fill="x", pady=(0, 15))
        
        self.entry_url_capa = ctk.CTkEntry(
            self.frame_url_input, 
            placeholder_text="URL da Capa...", 
            width=245, 
            height=35
        )
        self.entry_url_capa.pack(side="left", padx=(0, 5))
        
        self.btn_carregar_url = ctk.CTkButton(
            self.frame_url_input, text="OK", width=50, height=35, fg_color="#5E81AC"
        )
        self.btn_carregar_url.pack(side="left")

        # --- BOTÕES DE AÇÃO (Alinhados abaixo da URL) ---

        # 4.3 Botão Salvar (Principal)
        # fill="both" e expand=True farão ele ocupar o espaço para alinhar com a esquerda
        self.btn_salvar = ctk.CTkButton(
            self.container_capa,
            text="SALVAR NO ACERVO",
            font=("JetBrains Mono", 18, "bold"),
            height=60,               # Altura maior para destaque
            fg_color="#A3BE8C",      # Nord14 (Verde)
            hover_color="#8FBCBB",   # Nord7
            text_color="#2E3440"
        )
        self.btn_salvar.pack(side="top", fill="both", expand=True, pady=(0, 5))

        # 4.4 Botão Apagar Tudo (Secundário)
        self.btn_limpar = ctk.CTkButton(
            self.container_capa,
            text="APAGAR TUDO",
            font=("JetBrains Mono", 14, "bold"),
            height=40,               # Altura menor
            fg_color="#BF616A",      # Nord11 (Vermelho)
            hover_color="#D08770",   # Nord12
            text_color="#E5E9F0",
            #command=self.limpar_campos
        )
        self.btn_limpar.pack(side="top", fill="x", pady=(0, 22)) 
