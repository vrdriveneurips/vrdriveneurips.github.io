from PIL import Image

def make_square(in_path, out_path, fill_color=(255, 255, 255, 0)):
    img = Image.open(in_path)
    x, y = img.size
    size = max(x, y)

    # New square canvas (transparent by default)
    new_img = Image.new('RGBA', (size, size), fill_color)

    # Center original image
    new_img.paste(img, ((size - x) // 2, (size - y) // 2))

    new_img.save(out_path)

# 사용 예시
make_square("NeurIPS_logo.png", "NeurIPS_logo_square.png")
