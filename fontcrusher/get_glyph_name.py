"""
This tool is used to find the glyph names from css selectors.

The glyph naming convention are not always consistant for example in
Font Awesome the naming seems to follow four different naming conventions.

'cc-visa' (Visa) has a glyph name of 'uniF1F0'
'cc-mastercard' (Mastercard) has a glyph name of '_466'
'cc-amex' (American Express) has a glyph name of 'f1f3'
'credit-card' (Credit Card) has a glyph name of 'credit_card'

Due to this big inconsistancy this tool is needed to find the glyph names from
the css selectors used when you to embed them in webpages.
"""

import re

import fontcrusher


def get_character_mapping(font_object):
    "Function to get the character mapping from the unicode value to the glyph name"
    # Get character mapping from the cmap table
    char_mapping = [c.cmap.items() for c in font_object["cmap"].tables]
    # Now flatten list by one layer and create a dictrionary
    return dict(item for sublist in char_mapping for item in sublist)


def get_re_for_glyph_unicode(font_type, glyph):
    """Function to get the regex used for finding the unicode value for a font
    If a custom font is used put in the fonts css abreviation for the font_type
    """
    # All font names and font abreviations with font abreviations used
    font_types_abbreviations = {
        'font_awesome': 'fa',
        'foundation_icon': 'fi',
        'material_design': 'mdi',
        'glyphicon': 'glyphicon',  # Useless but for completion
        'ionicons': 'ion',
        'elusive': 'el'
    }
    return get_re_for_font_glyph_unicode(font_types_abbreviations.get(font_type, font_type), glyph)


def get_re_for_font_glyph_unicode(font_abreviation, glyph):
    "Function to get the regex for glyph unicode value"
    font_awesome_regex = [r'(?i)\.{}-'.format(font_abreviation),
                          """:before[^{}]*{\s*content:\s*['"]([^'"]*)['"][^\}]*\}"""]

    return ('|'.join([glyph])).join(font_awesome_regex)


def get_unicode_value(font_type, glyph, css_file):
    "Returns the unicode value for the glyph requested"
    re_string = get_re_for_glyph_unicode(font_type, glyph)
    # Need to raise error if glyph not found
    try:
        # Convert the hex string into a base 10 integer
        return int(re.findall(re_string, css_file)[0][1:], 16)
    except IndexError:
        raise KeyError('The glyph "{}" was not found in the css file'.format(glyph))


def get_unicode_value_list(font_abbreviation, glyph_list, css_file):
    "Returns the unicode mapping for a list of glyphs in a dictionary"
    return {glyph: get_unicode_value(font_abbreviation, glyph, css_file) for glyph in glyph_list}


def get_glyph_name(character_map, unicode_value):
    "Get the name of the glyph from the unicode value"
    return character_map[unicode_value]


def get_glyph_name_list(font_object, unicode_value_list):
    "Get a dictionary of the unicode chracter to the glyph name for a list of glyphs"
    character_map = get_character_mapping(font_object)
    return {u_value: get_glyph_name(character_map, u_value) for u_value in unicode_value_list}
