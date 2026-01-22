import customtkinter as ctk
import requests
from tkinter import messagebox
from PIL import Image
import os

class TelaCadastro(ctk.CTkFrame):
    def __init__(self, master, db):
        super().__init__(master,
                         fg_color="transparent",
                         #scrollbar_button_color="#2E3440",
                         #scrollbar_button_hover_color="#4C566A",
                         )
        self.db = db
       

        # Bind do scroll do mouse para sistemas Linux/Arch
        # Botão 4 é Scroll Up, Botão 5 é Scroll Down no Linux
        #self.bind_all("<Button-4>", lambda e: self._parent_canvas.yview_scroll(-1, "units"))
        #self.bind_all("<Button-5>", lambda e: self._parent_canvas.yview_scroll(1, "units"))

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

        self.btn_buscar_isbn = ctk.CTkButton(self.card_input_principal, text="Buscar ISBN", font=("JetBrains Mono", 12, "bold"), fg_color="#5E81AC", command=self.buscar_por_isbn)
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
        self.lbl_editora = ctk.CTkLabel(self.card_complementar, text="Editora")
        self.lbl_editora.grid(row=1, column=0, padx=(20, 10), pady=(10, 20), sticky="e")
        self.ent_editora = ctk.CTkEntry(self.card_complementar, height=35)
        self.ent_editora.grid(row=1, column=1, padx=(0, 20), pady=(10, 20), sticky="ew")

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

        # Use o próprio widget (self.txt_descricao) em vez de procurar por parent_canvas
        self.txt_descricao.bind("<Button-4>", lambda e: self.txt_descricao.yview_scroll(-1, "units"))
        self.txt_descricao.bind("<Button-5>", lambda e: self.txt_descricao.yview_scroll(1, "units"))

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
            text="Preview da Capa", 
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
            self.frame_url_input, text="OK", width=50, height=35, fg_color="#5E81AC", command=self.carregar_capa_por_url
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
            text_color="#2E3440",
            command=self.salvar_livro
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
            command=self.limpar_campos
        )
        self.btn_limpar.pack(side="top", fill="x", pady=(0, 22))

    def buscar_por_isbn(self):
        isbn = self.entry_isbn.get().strip()
        if not isbn:
            messagebox.showwarning("Aviso", "Digite um ISBN primeiro.")
            return

        # --- 1ª TENTATIVA: Google Books ---
        url_google = f"https://www.googleapis.com/books/v1/volumes?q=isbn:{isbn}"
        
        try:
            response = requests.get(url_google)
            data = response.json()

            if "items" in data:
                info = data["items"][0]["volumeInfo"]
                
                # Preenchimento de Metadados (Google)
                titulo = info.get("title", "Não encontrado")
                autor = ", ".join(info.get("authors", ["Desconhecido"]))
                genero = ", ".join(info.get("categories", ["N/A"]))
                paginas = info.get("pageCount", "")
                editora = info.get("publisher", "")
                sinopse = info.get("description", "")
                
                self.entry_titulo.delete(0, "end")
                self.entry_titulo.insert(0, titulo)
                self.entry_autor.delete(0, "end")
                self.entry_autor.insert(0, autor)
                self.ent_genero.delete(0, "end")
                self.ent_genero.insert(0, genero)
                self.ent_paginas.delete(0, "end")
                self.ent_paginas.insert(0, str(paginas))
                self.ent_editora.delete(0, "end")
                self.ent_editora.insert(0, editora)
                self.txt_descricao.delete("1.0", "end")
                self.txt_descricao.insert("1.0", sinopse)

                # Lógica de Capa (Google -> Open Library)
                links = info.get("imageLinks", {})
                url_capa = links.get("thumbnail") or links.get("smallThumbnail")
                
                if url_capa:
                    url_capa = url_capa.replace("http://", "https://")
                    self.baixar_e_exibir_capa(url_capa, isbn)
                else:
                    # Tenta apenas a capa na Open Library
                    self.buscar_capa_open_library(isbn)
                
                return # Livro encontrado no Google

            else:
                # --- 2ª TENTATIVA: Open Library (Fallback Completo) ---
                url_ol = f"https://openlibrary.org/api/books?bibkeys=ISBN:{isbn}&format=json&jscmd=data"
                response_ol = requests.get(url_ol)
                data_ol = response_ol.json()
                key = f"ISBN:{isbn}"

                if key in data_ol:
                    livro_ol = data_ol[key]
                    
                    # Preenchimento de Metadados (Open Library)
                    titulo = livro_ol.get("title", "Não encontrado")
                    autores = ", ".join([a.get("name") for a in livro_ol.get("authors", [])])
                    paginas = livro_ol.get("number_of_pages", "")
                    editoras = ", ".join([e.get("name") for e in livro_ol.get("publishers", [])])
                    generos = ", ".join([s.get("name") for s in livro_ol.get("subjects", [])[:3]])
                    
                    self.entry_titulo.delete(0, "end")
                    self.entry_titulo.insert(0, titulo)
                    self.entry_autor.delete(0, "end")
                    self.entry_autor.insert(0, autores or "Desconhecido")
                    self.ent_paginas.delete(0, "end")
                    self.ent_paginas.insert(0, str(paginas))
                    self.ent_editora.delete(0, "end")
                    self.ent_editora.insert(0, editoras)
                    self.ent_genero.delete(0, "end")
                    self.ent_genero.insert(0, generos)

                    # Busca capa
                    if "cover" in livro_ol:
                        url_capa = livro_ol["cover"].get("large") or livro_ol["cover"].get("medium")
                        if url_capa:
                            self.baixar_e_exibir_capa(url_capa, isbn)
                    
                    return # Livro encontrado na Open Library
                
                messagebox.showinfo("Aviso", "ISBN não encontrado em nenhuma das bases de dados.")

        except Exception as e:
            messagebox.showerror("Erro", f"Erro na conexão com as APIs: {e}")

    def buscar_capa_open_library(self, isbn):
        """Função auxiliar apenas para buscar a capa se o Google não tiver"""
        try:
            url_ol = f"https://openlibrary.org/api/books?bibkeys=ISBN:{isbn}&format=json&jscmd=data"
            data_ol = requests.get(url_ol).json()
            key = f"ISBN:{isbn}"
            if key in data_ol and "cover" in data_ol[key]:
                url = data_ol[key]["cover"].get("large") or data_ol[key]["cover"].get("medium")
                if url:
                    self.baixar_e_exibir_capa(url, isbn)
        except:
            pass 

    def baixar_e_exibir_capa(self, url, isbn):
        pasta_capas = os.path.join("assets", "capas")
        os.makedirs(pasta_capas, exist_ok=True)
        caminho = os.path.join(pasta_capas, f"{isbn}.png")
        
        try:
            img_data = requests.get(url).content
            with open(caminho, 'wb') as f:
                f.write(img_data)
            
            self.caminho_capa_atual = caminho
            img_pil = Image.open(caminho)
            
            # Dimensões levemente menores que o Frame (300x420)
            # 270x380 cria uma moldura elegante de 15px
            largura_moldura, altura_moldura = 270, 380
            
            self.img_ctk = ctk.CTkImage(
                light_image=img_pil, 
                dark_image=img_pil, 
                size=(largura_moldura, altura_moldura)
            )
            
            self.lbl_capa_info.configure(
                image=self.img_ctk, 
                text="" 
            )
            
        except Exception as e:
            self.lbl_capa_info.configure(text="Erro ao carregar capa", image="")
            print(f"Erro ao baixar capa: {e}")

    def limpar_campos(self):
        #"""Limpa todos os inputs, a descrição e reseta o preview da capa"""
        
        # 1. Limpar todos os CTkEntry (Inputs de linha única)
        # Dados Principais
        self.entry_titulo.delete(0, "end")
        self.entry_autor.delete(0, "end")
        self.entry_isbn.delete(0, "end")
        
        # Dados Complementares
        self.ent_paginas.delete(0, "end")
        self.ent_genero.delete(0, "end")
        self.ent_volume.delete(0, "end")
        self.ent_editora.delete(0, "end")
        
        # Campo de URL da Capa
        self.entry_url_capa.delete(0, "end")

        # 2. Limpar o CTkTextbox (Descrição/Sinopse)
        # No Textbox, "1.0" é o início e "end" é o fim
        self.txt_descricao.delete("1.0", "end")
        
        # (Opcional) Se você estiver usando o placeholder manual que conversamos:
        # self.txt_descricao.insert("1.0", self.placeholder_desc)
        # self.txt_descricao.configure(text_color="gray")

        # 3. Resetar o Preview da Capa
        # Removemos a imagem e voltamos o texto original
        self.lbl_capa_info.configure(image="", text="Preview da Capa")
        
        # 4. Limpar variáveis de controle
        self.caminho_capa_atual = None
        
        # Feedback no console para debug (útil no seu ambiente Arch)
        #print("Log: Todos os campos foram resetados.")

    def salvar_livro(self):
        """Coleta todos os dados da UI e persiste no banco de dados SQLite"""
        
        # 1. Coleta de dados dos campos (Entries)
        # Criamos o dicionário com as chaves EXATAS que o seu database.py usa no dicionário 'valores'
        dados = {
            "titulo": self.entry_titulo.get().strip(),
            "autor": self.entry_autor.get().strip(),
            "isbn": self.entry_isbn.get().strip(),
            "genero": self.ent_genero.get().strip(),
            "paginas": self.ent_paginas.get().strip(),
            "editora": self.ent_editora.get().strip(),
            "volume": self.ent_volume.get().strip(),
            "descricao": self.txt_descricao.get("1.0", "end-1c").strip(),
            
            # Campos extras que o banco de dados espera (preenchemos com padrão/vazio)
            "ano": None,
            "idioma": None,
            "nacionalidade": None,
            "data": None,
            "preco": 0.0,
            "avaliacao": 0,
            "status": "Quero Ler",
            "comentarios": ""
        }

        # 2. Validação básica
        if not dados["titulo"] or not dados["autor"]:
            messagebox.showerror("Erro de Validação", "Os campos 'Título' e 'Autor' são obrigatórios!")
            return

        # Limpa a descrição se for apenas o texto do placeholder
        if hasattr(self, 'placeholder_desc') and dados["descricao"] == self.placeholder_desc:
            dados["descricao"] = ""

        # 3. Tratamento do caminho da capa
        # Se baixamos uma capa via ISBN, usamos o caminho salvo. Caso contrário, usamos a URL manual.
        caminho_final_capa = getattr(self, 'caminho_capa_atual', None)
        if not caminho_final_capa:
            # Se não houver arquivo baixado, pega o que estiver escrito no campo de URL
            caminho_final_capa = self.entry_url_capa.get().strip()
        
        # Adicionamos a capa ao dicionário final
        dados["capa"] = caminho_final_capa

        try:
            # 4. CHAMADA CORRIGIDA:
            # Passamos apenas o dicionário 'dados'. O database.py vai desmembrar ele lá dentro.
            sucesso = self.db.adicionar_livro(dados)

            if sucesso:
                messagebox.showinfo("Sucesso", f"Livro '{dados['titulo']}' salvo com sucesso!")
                self.limpar_campos() 
            else:
                messagebox.showerror("Erro", "Não foi possível salvar. Verifique se o ISBN já existe.")

        except Exception as e:
            messagebox.showerror("Erro Crítico", f"Erro ao processar salvamento: {e}")

    def carregar_capa_por_url(self):
        """Baixa e exibe a capa a partir de uma URL inserida manualmente"""
        url = self.entry_url_capa.get().strip()
        isbn = self.entry_isbn.get().strip()

        if not url:
            messagebox.showwarning("Aviso", "Insira a URL da imagem primeiro.")
            return

        # Se não tiver ISBN, usamos um nome temporário ou timestamp para não dar erro
        nome_arquivo = isbn if isbn else f"temp_{int(datetime.now().timestamp())}"

        try:
            # Reutiliza a lógica de download, redimensionamento e moldura
            self.baixar_e_exibir_capa(url, nome_arquivo)
            messagebox.showinfo("Sucesso", "Capa carregada com sucesso a partir da URL.")
        except Exception as e:
            messagebox.showerror("Erro", f"Não foi possível carregar a imagem da URL:\n{e}")
