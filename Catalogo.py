# adiciona o tkinter para utilizar interface gráfica
import tkinter as tk

class Livro:
    def __init__(self, titulo, autor, exemplares_disponiveis):
        self.titulo = titulo
        self.autor = autor
        self.exemplares_disponiveis = exemplares_disponiveis

    def __str__(self):
        return f'{self.titulo} - {self.autor} ({self.exemplares_disponiveis} disponíveis)'

class CatalogoLivros:
    def __init__(self):
        self.catalogo = [] # Inicializa o catálogo vazio ao criar uma nova instância
        # Adiciona alguns livros diretamente no catálogo ao criar a instância
        self.catalogo.append(Livro("Dom Quixote", "Miguel de Cervantes", 5))
        self.catalogo.append(Livro("O Pequeno Príncipe", "Antoine de Saint-Exupéry", 3))
        self.catalogo.append(Livro("A Arte da Guerra", "Sun Tzu", 7))
        self.catalogo.append(Livro("Harry Poter e a Pedra Filosofal", "J. K. Rowling", 5))

    def cadastrar_livro(self, titulo, autor):
        livro_existente = next((livro for livro in self.catalogo if livro.titulo.lower() == titulo.lower() and livro.autor.lower() == autor.lower()), None)
        if livro_existente:
            livro_existente.exemplares_disponiveis += 1
            print(f'Mais um exemplar do livro "{titulo}", cujo autor é {autor}, foi adicionado ao catálogo. Total de exemplares agora: {livro_existente.exemplares_disponiveis}')
        
        else:
            novo_livro = Livro(titulo, autor, 1)  # Definindo exemplares como 1 por padrão
            self.catalogo.append(novo_livro)
            print(f'O livro "{titulo}", cujo(a) autor(a) é {autor}, foi cadastrado com sucesso!')

    def validar_disponibilidade(self, livro):
        if livro.exemplares_disponiveis > 0:
            return True
        else:
            return False

    def pesquisar_por_titulo(self, titulo):
        resultados = [livro for livro in self.catalogo if livro.titulo.lower() == titulo.lower()]
        return resultados

    def pesquisar_por_autor(self, autor):
        resultados = [livro for livro in self.catalogo if livro.autor.lower() == autor.lower()]
        return resultados

class InterfaceCatalogo:
    def __init__(self, root):
        self.root = root
        self.root.title("Catálogo de Livros com Verificação de Disponibilidade")

        self.catalogo = CatalogoLivros()        

        self.frame = tk.Frame(self.root)
        self.frame.pack()

        self.label_titulo = tk.Label(self.frame, text="Título: ")
        self.label_titulo.pack()

        self.entry_titulo = tk.Entry(self.frame)
        self.entry_titulo.pack()

        self.label_autor = tk.Label(self.frame, text="Autor: ")
        self.label_autor.pack()

        self.entry_autor = tk.Entry(self.frame)
        self.entry_autor.pack()

        self.btn_cadastrar = tk.Button(self.frame, text="Cadastrar Livro", command=self.cadastrar_livro)
        self.btn_cadastrar.pack()

        self.label_consulta = tk.Label(self.frame, text="Consultar disponibilidade\n por título ou autor: ")
        self.label_consulta.pack()

        self.entry_consulta = tk.Entry(self.frame)
        self.entry_consulta.pack()

        self.btn_consultar = tk.Button(self.frame, text="Consultar Disponibilidade", command=self.consultar_disponibilidade)
        self.btn_consultar.pack()

        self.resultados_text = tk.Text(self.frame, height=10, width=60)
        self.resultados_text.pack()
        
        self.exibir_livros_cadastrados()
              
    def exibir_livros_cadastrados(self):
        livros_cadastrados = "Livros já cadastrados:\n"
        for livro in self.catalogo.catalogo:
            livros_cadastrados += f"- {livro.titulo} por {livro.autor} ({livro.exemplares_disponiveis} exemplares disponíveis)\n"
        self.mostrar_resultados(livros_cadastrados)
        
    def cadastrar_livro(self):
        titulo = self.entry_titulo.get()
        autor = self.entry_autor.get()
        self.catalogo.cadastrar_livro(titulo, autor)
        self.entry_titulo.delete(0, tk.END)
        self.entry_autor.delete(0, tk.END)
        self.mostrar_resultados(f'O livro "{titulo}", cujo(a) autor(a) é {autor} foi cadastrado com sucesso!\n')

    def consultar_disponibilidade(self):
        consulta = self.entry_consulta.get()
        resultados_titulo = self.catalogo.pesquisar_por_titulo(consulta)
        resultados_autor = self.catalogo.pesquisar_por_autor(consulta)

        if resultados_titulo or resultados_autor:
            mensagem = ""
            for livro in resultados_titulo:
                disponibilidade = "disponível" if self.catalogo.validar_disponibilidade(livro) else "não disponível"
                mensagem += f'{str(livro)} está {disponibilidade}\n'

            for livro in resultados_autor:
                disponibilidade = "disponível" if self.catalogo.validar_disponibilidade(livro) else "não disponível"
                mensagem += f'{str(livro)} está {disponibilidade}\n'

            self.mostrar_resultados(mensagem)
        else:
            self.mostrar_resultados(f'Nenhum livro encontrado com o título ou autor "{consulta}"\n')

    def mostrar_resultados(self, mensagem):
        self.resultados_text.insert(tk.END, mensagem)

if __name__ == "__main__":
    root = tk.Tk()
    app = InterfaceCatalogo(root)
    root.mainloop()
