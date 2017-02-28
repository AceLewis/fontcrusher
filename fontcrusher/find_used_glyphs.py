"""
This tool is used to find all the font glyphs you have used. It can search
through all files in a directory and thorugh subdirectories by using
{'recursive': True} as the kwargs in a glob argument.
"""

import re
import sys
import glob
import os.path


def find_used_glyphs(include_args, regex_pattern, exclude_args=[]):
    """
    This function will search through the files defined by the glob args
    you can easily include all files in a directory and subdirectories
    using wild cards. Make sure you exclude the font's css file as it
    will in some fonts have the exact same names as the regex used to match.

    This function works somewhat simmilarly to grep.

    include_args should be a list of glob arguments that are also in a list.
    Each glob argument in that list has to be a string and can optionally be
    followed by a dictionary with the kwargs e.g {'recursive': True}.
    """

    exclude_files = set()

    for exclude_arg in exclude_args:
        # If no kwargs exists append them
        if len(exclude_arg) == 1:
            exclude_arg.append({})
        for file in glob.iglob(exclude_arg[0], **exclude_arg[1]):
            exclude_files.update([file])

    # Set because glyphs will be repeated
    glyphs_used = set()

    for include_arg in include_args:
        # If no kwargs exists append them
        if len(include_arg) == 1:
            include_arg.append({})
        for file in glob.iglob(include_arg[0], **include_arg[1]):
            # Check the item is a file and is also one which is not excluded
            if os.path.isfile(file) and file not in exclude_files:
                try:
                    with open(file, 'r') as file_obj:
                        for line in file_obj:
                            search = re.search(regex_pattern, line)
                            if search:
                                glyphs_used.update([search.group(1)])
                except UnicodeDecodeError:
                    pass  # File is not text (binary files)
                except:
                    raise
    return glyphs_used


def get_regex_for_glyph(font_name):
    "A function to return the regex for each font"

    font_types_regex = {
        'font_awesome': 'fa fa-([a-zA-Z0-9\-]+)',
        'foundation_icon': 'fi-([a-zA-Z0-9\-]+)',
        'material_design': 'mdi mdi-([a-zA-Z0-9\-]+)',
        'glyphicon': 'glyphicons glyphicons-([a-zA-Z0-9\-]+)',
        'ionicons': 'icon ion-([a-zA-Z0-9\-]+)',
        'elusive': 'el el-([a-zA-Z0-9\-]+)'
    }

    return font_types_regex[font_name]
