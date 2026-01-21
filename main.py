# IMPORTS
import os
import customtkinter as ctk
from PIL import Image

# DATABASE
from database import BibliotecaDB

# TELAS
from telas.tela_home import TelaHome
from telas.tela_cadastro import TelaCadastro
# ----------------------------------------------------customtkinter

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
caminho_fonte = os.path.join(BASE_DIR, "assets", "fonts", "static", "JetBrainsMono-Regular.ttf")
caminho_tema = os.path.join(BASE_DIR, "temas", "nord.json")

ctk.FontManager.load_font(caminho_fonte)

try:
    ctk.set_default_color_theme(caminho_tema)
except Exception as e:
    print(f"Erro ao carregar tema: {e}")
    ctk.set_default_color_theme("blue")

ctk.set_appearance_mode("dark")

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Configurações da janela
        self.title("Biblioteca Local")
        self.geometry("1980x1020")

        # Carregar icons
        self.carregar_icones()

        # Inicia o banco de dados
        self.db = BibliotecaDB()

        # Layout
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # sidebar
        self.sidebar_expandida = True
        self.sidebar = ctk.CTkFrame(self, width=160, corner_radius=10)
        self.sidebar.grid(row=0, column=0, sticky="nsew")
        self.sidebar.grid_propagate(False)
        self.sidebar.pack_propagate(False)

        # Botão de Menu (Hambúrguer)
        self.btn_menu = ctk.CTkButton(self.sidebar, 
                                      image=self.icons["menu"],
                                      text="Menu", 
                                      anchor="w",
                                      command=self.toggle_sidebar)
        self.btn_menu.pack(pady=25, padx=10, anchor="w")

        # Botões de Navegação (Usaremos variáveis para mudar o texto depois)
        self.btn_home = ctk.CTkButton(self.sidebar,
                                      image=self.icons["home"],
                                      text="Home", 
                                      anchor="w",
                                      command=self.show_home)
        self.btn_home.pack(pady=5, padx=10, fill="x")
        
        self.btn_biblioteca = ctk.CTkButton(self.sidebar,
                                            image=self.icons["biblioteca"],
                                            text="Biblioteca", 
                                            anchor="w",
                                            command=self.show_biblioteca)
        self.btn_biblioteca.pack(pady=5, padx=10, fill="x")

        self.btn_cadastro = ctk.CTkButton(self.sidebar,
                                          image=self.icons["cadastro"],
                                          text="Cadastro", 
                                          anchor="w",
                                          command=self.show_cadastro)
        self.btn_cadastro.pack(pady=5, padx=10, fill="x")

        self.btn_estatisticas = ctk.CTkButton(self.sidebar,
                                              image=self.icons["estatísticas"],
                                              text="Estatísticas", 
                                              anchor="w",
                                              command=self.show_estatisticas)
        self.btn_estatisticas.pack(pady=5, padx=10, fill="x")

        self.btn_mundo = ctk.CTkButton(self.sidebar,
                                       image=self.icons["mundo"],
                                       text="Mundo", 
                                       anchor="w",
                                       command=self.show_mundo)
        self.btn_mundo.pack(pady=5, padx=10, fill="x")

        self.btn_citacoes = ctk.CTkButton(self.sidebar,
                                          image=self.icons["citacoes"],
                                          text="Citações", 
                                          anchor="w",
                                          command=self.show_citacoes)
        self.btn_citacoes.pack(pady=5, padx=10, fill="x")

        self.spacer = ctk.CTkLabel(self.sidebar, text="")
        self.spacer.pack(expand=True, fill="both")

        self.btn_configuracoes = ctk.CTkButton(self.sidebar,
                                               image=self.icons["configuracoes"],
                                               text="Configurações",
                                               anchor="w",
                                               command=self.show_configuracoes)
        self.btn_configuracoes.pack(side="bottom", pady=20, padx=10, fill="x")

        # Conteudo
        self.main_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.main_frame.grid(row=0, column=1, sticky="nsew", padx=20, pady=20)

        self.show_home()

    def toggle_sidebar(self):
        if self.sidebar_expandida:
            # RECOLHER
            self.animar_sidebar(60)
            self.btn_menu.configure(text="")
            self.btn_home.configure(text="")
            self.btn_biblioteca.configure(text="")
            self.btn_cadastro.configure(text="")
            self.btn_estatisticas.configure(text="")
            self.btn_mundo.configure(text="")
            self.btn_citacoes.configure(text="")
            self.btn_configuracoes.configure(text="")
            self.sidebar_expandida = False
        else:
            # EXPANDIR
            self.animar_sidebar(160)
            self.btn_menu.configure(text="Menu")
            self.btn_home.configure(text="Home")
            self.btn_biblioteca.configure(text="Biblioteca")
            self.btn_cadastro.configure(text="Cadastro")
            self.btn_estatisticas.configure(text="Estatísticas")
            self.btn_mundo.configure(text="Mundo")
            self.btn_citacoes.configure(text="Citações")
            self.btn_configuracoes.configure(text="Configurações")
            self.sidebar_expandida = True 

    def animar_sidebar(self, largura_alvo):
        largura_atual = self.sidebar.winfo_width()
        passo = 30  # Quantos pixels a barra move por frame
    
        if abs(largura_atual - largura_alvo) > passo:
            nova_largura = largura_atual + (passo if largura_alvo > largura_atual else -passo)
            self.sidebar.configure(width=nova_largura)
            # Chama a si mesmo após 10ms (gera o efeito de 60fps)
            self.after(1, lambda: self.animar_sidebar(largura_alvo))
        else:
            self.sidebar.configure(width=largura_alvo)
    

    def show_home(self):
        for widget in self.main_frame.winfo_children():
            widget.destroy()
        self.aba_home = TelaHome(self.main_frame, self.db)
        self.aba_home.pack(fill="both", expand=True)

    def show_biblioteca(self):
        # Placeholder para o catálogo
        pass

    def show_cadastro(self):
        #for widget in self.main_frame.winfo_children():
        #    widget.destroy()
        #self.aba_cadastro = TelaCadastro(self.main_frame, self.db)
        #self.aba_cadastro.pack(fill="both", expand=True)
        pass

    def show_estatisticas(self):
        # Placeholder para o catálogo
        pass

    def show_mundo(self):
        # Placeholder para o catálogo
        pass

    def show_citacoes(self):
        # Placeholder para o catálogo
        pass

    def show_configuracoes(self):
        pass

    def carregar_icones(self):
        # Pasta onde você salvou os PNGs do Lucide
        path = "assets/icons/"
        
        self.icons = {
            "menu": ctk.CTkImage(Image.open(f"{path}menu.png"), size=(20, 20)),
            "home": ctk.CTkImage(Image.open(f"{path}house.png"), size=(20,20)),
            "biblioteca": ctk.CTkImage(Image.open(f"{path}library-big.png"), size=(20,20)),
            "cadastro": ctk.CTkImage(Image.open(f"{path}file-plus.png"), size=(20,20)),
            "estatísticas": ctk.CTkImage(Image.open(f"{path}chart-no-axes-combined.png"), size=(20,20)),
            "mundo": ctk.CTkImage(Image.open(f"{path}globe.png"), size=(20,20)),
            "citacoes": ctk.CTkImage(Image.open(f"{path}quote.png"), size=(20,20)),
            "configuracoes": ctk.CTkImage(Image.open(f"{path}settings.png"), size=(20,20))
        }

if __name__ == "__main__":
    app = App()
    app.mainloop()
