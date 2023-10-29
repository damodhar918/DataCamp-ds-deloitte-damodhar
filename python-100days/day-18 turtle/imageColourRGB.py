###This code will not work in repl.it as there is no access to the colorgram package here.###
##We talk about this in the video tutorials##
import colorgram
import colorsys

def image_colour_rgb(img,no_colours):
    """Extracts the RGB values of the colours in the image and returns a list of tuples of the RGB values.

    Returns: list of tuples of the RGB values of the colours in the image.
    """
    rgb_colors = []
    # colors = colorgram.extract(r'C:\Users\jdamodhar\Desktop\python_essential-\python-100\day-18\image.jpg', 30)
    colors = colorgram.extract(img,no_colours)
    for color in colors:
        r = color.rgb.r
        g = color.rgb.g
        b = color.rgb.b
        new_color = (r, g, b)
        rgb_colors.append(new_color)
    return rgb_colors

# x = image_colour_rgb(r'C:\Users\jdamodhar\Desktop\python_essential-\python-100\day-18\image.jpg', 30)
# print(x)