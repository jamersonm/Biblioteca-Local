# 📚 Gerenciador de Acervo Pessoal

Este é um projeto de estudo desenvolvido em **Python**, focado na criação de uma interface gráfica (GUI) moderna e funcional para o gerenciamento de bibliotecas de livros pessoais. A aplicação utiliza o padrão de design **Nord** e foca em modularidade e boas práticas de desenvolvimento.

## 🛠️ Tecnologias Utilizadas

* **Linguagem:** Python 3.x
* **Interface Gráfica:** [CustomTkinter](https://github.com/TomSchimansky/CustomTkinter) (Uma evolução moderna do Tkinter).
* **Banco de Dados:** SQLite3 para persistência local de dados.
* **Processamento de Imagem:** Pillow (PIL) para redimensionamento e exibição de capas.
* **Integração com APIs:** Requests para busca de metadados via Google Books e Open Library.
* **Estilização:** Sistema de temas via JSON com a paleta de cores **Nord**.

## ✨ Funcionalidades

- [x] **Interface Moderna:** Sidebar retrátil e responsiva com ícones da Lucide.
- [x] **Tematização Dinâmica:** Suporte total ao tema Nord com fonte **JetBrains Mono** embutida.
- [x] **Arquitetura Modular:** Separação clara entre lógica de banco de dados, interface e recursos estáticos.
- [x] **Busca Automática:** Recuperação de informações (Título, Autor, Sinopse) através do código ISBN.
- [ ] **Catálogo Dinâmico:** Exibição de livros em grade com scroll infinito (Em desenvolvimento).
- [ ] **Filtros Avançados:** Organização por status de leitura (Lendo, Lido, Quero Ler).

## 📂 Estrutura do Repositório

```text
├── main.py              # Ponto de entrada (Gerencia a janela principal e a sidebar)
├── database.py          # Classe de abstração do banco de dados SQLite
├── Temas/               # Arquivos JSON de configuração estética (nord.json)
├── telas/               # Módulos das interfaces específicas (Cadastro, Catálogo)
│   ├── tela_cadastro.py
│   └── tela_catalogo.py
├── assets/              # Recursos visuais
│   ├── icons/           # Ícones Lucide (PNG)
│   ├── fonts/           # JetBrains Mono (TTF)
│   └── capas/           # Cache de imagens das capas baixadas
└── requirements.txt     # Dependências do projeto
