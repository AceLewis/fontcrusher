"""
I think this example code very quickly explains how this modlue can be used and
can serve as a cookie cutter code that you can copy and paste.
"""

import fontcrusher
from fontcrusher import find_used_glyphs, get_glyph_name, css_crush

# Load in font and CSS file for font
font_object = fontcrusher.load_the_font(r'.\website_folder\fontawesome-webfont.ttf')
css_file = css_crush.read_file(r'.\website_folder\font-awesome.min.css')

# Find all glyphs used in website
regex_for_find = find_used_glyphs.get_regex_for_glyph('font_awesome')
include_argument = [[r'.\website_folder\**\*', {'recursive': True}]]
exclude_arg = [[r'.\website_folder\subdirectory\exclude_file.txt']]
used_glyphs = find_used_glyphs.find_used_glyphs(include_argument, regex_for_find, exclude_args=exclude_arg)

# Find the unicode values of those glyphs and use unicode value to get glyph name
unicode_values = get_glyph_name.get_unicode_value_list('fa', used_glyphs, css_file).values()
glyph_names = get_glyph_name.get_glyph_name_list(font_object, unicode_values).values()

# create a new font object with only the glyphs used in the website
crushed_font = fontcrusher.crush_font(font_object, glyph_names)
# Remove all CSS atributed for unneeded glyphs
crushed_css = css_crush.remove_glyphs_from_css(css_file, 'font_awesome', used_glyphs)

# Save the crushed font and save the crushed CSS
crushed_font.save(r'.\website_folder\fontawesome-webfont.crushed.ttf')
css_crush.write_file(r'.\website_folder\font-awesome.crushed.css', crushed_css)

# To save a woff font
crushed_font.flavor = 'woff'
crushed_font.save(r'.\website_folder\fontawesome-webfont.crushed.woff')