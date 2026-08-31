import os
from PIL import Image


def clear_all_logs():
    file_current = os.path.dirname(os.path.abspath(__file__))

    count = 0

    for root, files, archives in os.walk(file_current):
        for archive in archives:
            if archive.lower().endswith('.png'):
                caminho_completo = os.path.join(root, archive)

                try:
                    with Image.open(caminho_completo) as img:
                        image_clean = Image.new(img.mode, img.size)
                        image_clean.putdata(list(img.getdata()))

                        image_clean.save(caminho_completo, format="PNG")

                    print(f"[OK] Remove : {caminho_completo}")
                    contador += 1
                except Exception as e:
                    print(f"[ERRO] Falha ao processar {caminho_completo}: {e}")

    print(f"\nProcesso concluído! Total de PNGs limpos: {contador}")


if __name__ == "__main__":
    limpar_todos_pngs()
