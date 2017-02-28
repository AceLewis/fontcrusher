import re


def read_file(css_file_name):
    "Function to read the CSS file"
    with open(css_file_name, 'r') as file:
        return file.read()


def write_file(file_name, css_to_write):
    "Function to write the CSS to a file"
    with open(file_name, 'w') as file:
        file.write(css_to_write)


def remove_glyphs_from_css(input_css, font_type, glyphs):
    "Remove CSS for unwanted glyphs"
    re_patterns = get_re_for_glyphs(font_type, glyphs)
    for re_pattern, re_replacement in re_patterns:
        input_css = re.sub(re_pattern, re_replacement, input_css)
    return re.sub(r'\n{3,}', '\n\n', input_css)


def get_re_for_glyphs(font_type, glyphs):
    """Function to get the regex used for removing unwanted glyphs
    If a custom font is used put in the fonts css abbreviation for the font_type
    """
    # All font names and font abbreviations with font abbreviations used
    font_types_abbreviations = {
        'font_awesome': 'fa',
        'foundation_icon': 'fi',
        'material_design': 'mdi',
        'glyphicon': 'glyphicon',  # Useless but for completion
        'ionicons': 'ion',
        'elusive': 'el'
    }
    return get_re_for_font_glyphs(font_types_abbreviations.get(font_type, font_type), glyphs)


def get_re_for_font_glyphs(font_abbreviation, glyphs):
    "Function to get the regex for unwanted glyphs"
    # Only keep used glyphs
    font_awesome_regex = [r'(?i)(?<=}})\s*(\.{}-(?!('.format(font_abbreviation),
                          r'):)[0-9a-z\-]*:before,\s*)*\.{}-(?!('.format(font_abbreviation),
                          r'):)[0-9a-z-]*:before\s*{\s*content:\s*"\\?\w+"[^\}]*\}']
    # Also remove unused aliases
    unused_selector = [r'(?i)\.{}-(?!('.format(font_abbreviation),
                       r'):before)[^.]*?:before,?']

    return [(('|'.join(glyphs)).join(font_awesome_regex), ''),
            (('|'.join(glyphs)).join(unused_selector), '')]
