# Projeto_Programa_Match

### Repositório para o 2º projeto no programa MATCH!, parceria da Mastertech e IBM

# Resumo:

Este código implementa o Projeto Catálogo de Livros com Verificação de Disponibildiade. A interface gráfica foi feita usando a biblioteca Tkinter, conforme dicas dos demais estudantes durantes as mentorias, contudo, como não tenho domínio da biblioteca tkinter e ainda não havia feito qualquer interface gráfica com Python, utilizei o auxílio do ChatGPT.

O código permite o cadastro de novos livros, a exibição dos livros cadastrados, e a consulta da disponibilidade de livros por título ou autor da obra.

[Verifique o vídeo para ver o código em funcionamento.](/Projeto_Catalogo_De_Livros.mp4)

[Verifique o código.](/Catalogo.py)

## Funcionalidades:

Cadastramento de livros: Adiciona novos livros ao catálogo com título, autor e exemplar disponível.

Verificação de disponibilidade: Verifica se um livro possui exemplares disponíveis.

Pesquisa por título ou autor: Permite buscar livros no catálogo com base no título ou autor.

Interface gráfica: Utiliza Tkinter para criar uma interface com entrada de dados e exibição dos resultados.

### Funcionamento Principal:

Instanciação da interface gráfica: Inicializa a janela Tkinter e cria a interface com os elementos necessários.

Funções para cadastrar, consultar e exibir livros: São acionadas pelos botões da interface para realizar as operações no catálogo.

### Classes Principais:

#### Livro:

* Atributos:
    * titulo: Título do livro.
    * autor: Autor do livro.
    * exemplares_disponiveis: Número de exemplares disponíveis do livro.

#### CatalogoLivros:

* Atributos:

    * catalogo: Lista que armazena os livros cadastrados.

* Métodos:

    * __init__: Inicializa o catálogo com alguns livros já cadastrados.

    * cadastrar_livro: Adiciona um novo livro ao catálogo ou incrementa exemplares se o livro já existe.

    * validar_disponibilidade: Verifica se um livro tem exemplares disponíveis.

    * pesquisar_por_titulo e pesquisar_por_autor: Realiza busca de livros por título ou autor.

Execução do Código:

Para executar o código, é necessário uma instalação do Python com a biblioteca Tkinter.

O Google Colab não possui acesso à biblioteca, logo não é possível utilizar a interface gráfica ou executar o código.

Após a execução, uma janela com a interface gráfica será exibida.

## Versões e Dificuldades

Na primeira versão havia colocado a consulta apenas por obra e por autor, separadas, contudo, percebi que seria mais simples permitir a consulta tanto por um quanto por outro.

Também não havia cadastrado livros previamente, assim o catálogo sempre estava vazio ao iniciar o programa, após executar algumas vezes percebi que seria interessante possuir livros pré-cadastrados.

Em outro momento, percebi que ao cadastrar um novo livro, a quantidade existente de livros no catálogo permanecia a mesma, assim, tive que adicionar um código de incremento para que funcionasse corretamente e desse o valor correto de livros no catálogo.

A utilização de interface gráfica veio de dicas dos demais estudantes durante a mentoria, contudo a implementação foi particularmente difícil, pois esta é a primeira vez que utilizei interface gráfica em um código python.

---

<details close>
    <summary>Ferrametas usadas</summary>
    Código: VSCode
    Gravação de Tela: OBS Studio
    Edição de Vídeo: Microsoft Clipchamp    
</details>
