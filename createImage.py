from PIL import Image
import pandas as pd

size = 500
# img = Image.new('RGB', (size, size), color = (73, 109, 137))
# img.save('images/pil_color.png')

colors = pd.read_csv('ColorList.csv')
# print(colors['name'].iloc[3])
# colors.shape[0]
for i in range(0, colors.shape[0]):
    name = colors['name'].iloc[i].replace(" ", "")
    hexa = colors['hex'].iloc[i]
    r = colors['red'].iloc[i]
    g = colors['green'].iloc[i]
    b = colors['blue'].iloc[i]

    img = Image.new('RGB', (size, size), color = (r, g, b))
    img.save('images/' + str(i) +'.jpeg')