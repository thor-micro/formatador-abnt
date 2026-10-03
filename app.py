    main()print("Formatador ABNT iniciado!")
from pathlib import Path


NOME_APLICACAO = "Formatador Acadêmico UFOPA"


def verificar_arquivo(caminho):
    """Verifica se o arquivo recebido é um DOCX."""
    arquivo = Path(caminho)

    if not arquivo.exists():
        return False, "Arquivo não encontrado."

    if arquivo.suffix.lower() != ".docx":
        return False, "O arquivo precisa estar no formato .docx."

    return True, "Arquivo DOCX válido."


def main():
    print("=" * 50)
    print(NOME_APLICACAO)
    print("=" * 50)
    print()
    print("Sistema iniciado.")
    print("Aguardando um arquivo DOCX...")


if __name__ == "__main__":
