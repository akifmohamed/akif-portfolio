from pathlib import Path

from PIL import Image, ImageOps, ImageDraw


source = Path(r'c:\Users\Akif Mohamed\OneDrive\Documents\portfolio\draft\akif-no-bg.png')
output = Path(r'c:\Users\Akif Mohamed\OneDrive\Documents\portfolio\draft\favicon-photo.png')

image = Image.open(source).convert('RGBA')
size = 128

fitted = ImageOps.fit(image, (size, size), method=Image.Resampling.LANCZOS, centering=(0.5, 0.35))

mask = Image.new('L', (size, size), 0)
draw = ImageDraw.Draw(mask)
draw.ellipse((0, 0, size - 1, size - 1), fill=255)

circle = Image.new('RGBA', (size, size), (0, 0, 0, 0))
circle.paste(fitted, (0, 0), mask)
circle.save(output)

print(output)