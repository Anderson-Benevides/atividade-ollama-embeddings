import requests

URL = "http://localhost:11434/api/embed"

MODELO = "nomic-embed-text"

texto = "A tecnologia pode ajudar na educacao."

dados = {
    "model": MODELO,
    "input": texto
}

try:
    resposta = requests.post(URL, json=dados, timeout=120)
    resposta.raise_for_status()

    resultado = resposta.json()
    vetor = resultado["embeddings"][0]

    print("Texto original:", texto)
    print("Modelo utilizado:", MODELO)
    print("Embedding gerado com sucesso!")
    print("Tamanho do vetor:", len(vetor))
    print("Primeiros 10 valores:", vetor[:10])

except requests.exceptions.ConnectionError:
    print("Erro: nao foi possivel conectar ao Ollama.")
    print("Verifique se o Ollama esta instalado e em execucao.")

except requests.exceptions.RequestException as erro:
    print("Erro na requisicao:", erro)

except (KeyError, IndexError):
    print("Erro: a resposta do Ollama nao tem o formato esperado.")
