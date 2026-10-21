tabela_telefonica = {
    "Maria": "3654-1234",
    "Joao": "3655-1321",
    "Barbara": "3654-3910",
    "Mateus": "3655-0019"
}

def buscar_telefone(nome):
    if nome in tabela_telefonica:
        return tabela_telefonica[nome]
    else:
        return "Nome não encontrado"

def adicionar_telefone(nome, telefone):
    tabela_telefonica[nome] = telefone
    print(tabela_telefonica, flush=True)

def remover_telefone(nome):
    if nome in tabela_telefonica:
        del tabela_telefonica[nome]
        print(f"{nome} foi removido da tabela.", flush=True)
    else:
        print(f"{nome} não existe")

if __name__ == "__main__":
    print("Número da Maria: ", buscar_telefone("Maria"))
    print("Número do Carlinhos Maia: ", buscar_telefone("Carlinhos Maia"))
    adicionar_telefone("Milton", "1234-5678")
    print("Número do Milton: ",buscar_telefone("Milton"))
    remover_telefone("Mateus")
    print("Número do Mateus: ", buscar_telefone("Mateus"))