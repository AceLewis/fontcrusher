import fontTools.subset


def load_the_font(load_font_path):
    "Function to load a font, font must be TrueType or OpenType font e.g TFF, WOFF"
    options = fontTools.subset.Options()
    return fontTools.subset.load_font(load_font_path, options)


def get_glyphs_from_file(file_name):
    "Obtain the glyphs that want to be kept from a line seperated file"
    with open(file_name, 'r') as file:
        return file.read().splitlines()


def load_and_crush_font(font_path, glyphs):
    "Load a font then compress it to keep only needed glyphs"
    original_font = load_the_font(font_path)
    return crush_font(original_font, glyphs)


def crush_font(font_object, glyphs):
    "Function to strip unneeded glyphs from a font object"
    options = fontTools.subset.Options()
    options.desubroutinize = True
    # Create a subset of the font
    subsetter = fontTools.subset.Subsetter(options=options)
    subsetter.populate(glyphs=set(glyphs))
    subsetter.subset(font_object)
    return font_object
