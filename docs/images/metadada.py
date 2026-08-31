import os
from PIL import Image


def clear_all_logs():
    file_current = os.path.dirname(os.path.abspath(__file__))

    count = 0

    for root, files, archives in os.walk(file_current):
        for archive in archives:
            if archive.lower().endswith('.png'):
                full_path = os.path.join(root, archive)

                try:
                    with Image.open(full_path) as img:
                        image_clean = Image.new(img.mode, img.size)
                        image_clean.putdata(list(img.getdata()))

                        image_clean.save(full_path, format="PNG")

                    print(f"[OK] Remove : {full_path}")
                    count += 1
                except Exception as e:
                    print(f"[ERRO] Fail in process {full_path}: {e}")


if __name__ == "__main__":
    clear_all_logs()
