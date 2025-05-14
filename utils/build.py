def generate_pdf(doc, filepath, clean_tex=True):
    try:
        doc.generate_pdf(filepath, clean_tex=clean_tex)
    except Exception as e:
        try:
            print(e.output.decode('latin1'))  # ou use 'errors="replace"' se preferir
        except Exception:
            print("Erro ao decodificar a saída do LaTeX.")
        raise e
