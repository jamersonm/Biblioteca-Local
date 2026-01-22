# 📚 Gerenciador de Acervo Pessoal

Este é um projeto de estudo desenvolvido em **Python**, focado na criação de uma interface gráfica (GUI) moderna e funcional para o gerenciamento de bibliotecas de livros pessoais. A aplicação utiliza a paleta de cores **Nord** e foca em modularidade, alta performance no Linux e boas práticas de desenvolvimento.

## 🛠️ Tecnologias Utilizadas

* **Linguagem:** Python 3.x
* **Interface Gráfica:** [CustomTkinter](https://github.com/TomSchimansky/CustomTkinter) (Interface moderna e responsiva).
* **Banco de Dados:** SQLite3 (Persistência local com suporte a metadados estendidos).
* **Tipografia:** JetBrains Mono (Renderização otimizada para desenvolvedores).
* **Processamento de Imagem:** Pillow (PIL) para tratamento de capas (300x420px).
* **Integração:** Requests para busca via ISBN e URLs externas.

## ✨ Funcionalidades

- [x] **Interface Moderna:** Sidebar retrátil e responsiva com ícones da Lucide.
- [x] **Layout de Cadastro Avançado:** Sistema de cards para organização de Dados Principais, Dados Complementares e Descrição.
- [x] **Preview de Capa:** Área dedicada para visualização da capa do livro em tempo real via URL ou ISBN.
- [x] **Persistência Estendida:** Banco de dados preparado para armazenar Volume, Editora, Status de Leitura e Comentários.
- [x] **Arquitetura Modular:** Separação entre componentes de interface (`telas/`) e persistência (`database.py`).
- [ ] **Integração com API:** Busca automática de metadados via Google Books (Em implementação).
- [ ] **Catálogo Dinâmico:** Exibição em grade (Grid System) com scroll infinito.

## 🗄️ Esquema do Banco de Dados

O banco de dados foi atualizado para suportar um gerenciamento detalhado:
* **Identificação:** ISBN, Título, Autor, Editora, Volume.
* **Físico:** Páginas, Idioma, Nacionalidade, Ano.
* **Pessoal:** Status (Lendo/Lido/Quero Ler), Avaliação, Preço, Data de Término.
* **Conteúdo:** Gênero, Descrição e Comentários.

## 📂 Estrutura do Repositório

```text
├── main.py              # Ponto de entrada e gerenciamento da Sidebar
├── database.py          # Gerenciamento da tabela 'livros' no SQLite
├── Temas/               # Configuração estética (nord.json)
├── telas/               # Módulos das interfaces
│   ├── tela_home.py     # Dashboard inicial
│   ├── tela_cadastro.py # Interface de entrada de dados (Layout 3-card)
│   └── tela_catalogo.py # Visualização do acervo
├── assets/              # Recursos estáticos
│   ├── icons/           # Ícones Lucide (PNG)
│   ├── fonts/           # Fontes JetBrains Mono (TTF)
│   └── covers/          # Cache de capas baixadas
└── requirements.txt     # Dependências (customtkinter, pillow, requests)
