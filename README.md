# FontCrusher

FontCrusher reduce the file size of fonts to less than 5% of their original size by removing unwanted glyphs. This module is aimed towards icon fonts however can be used on any type of font.

## How to Install

FontCrusher uses FontTools so therefore requires Python 2.7, 3.4 or later.

The package is listed in the Python Package Index (PyPI), so you can install it with pip:

``` python
pip install fontcrusher
```

## Terminology
* Icon font - A font that contains many icons that can easily be embedded on a webpage e.g [Font Awesome](http://fontawesome.io/)
* Glyph - These are basically the characters within a font, in the case of an icon font glyphs would be the individual icons.

## What is FontCrusher?

FontCrusher is a module to help you reduce the file size of fonts by removing unused and unwanted glyphs. This module can be used to crush any font however its main target is icon fonts. Icon fonts are becoming more popular, they are a brilliant way to embed salable vector icons that can be controlled in CSS and only require one HTTP request. The problem with icon fonts is they can contain hundreds of icons that all need to be downloaded even if you only need to use a few icons, this module allows you to create fonts that only have the ones you want to save within them.

The motivation behind this tool was because on [my blog/website](https://acelewis.com) I use [Font Awesome](http://fontawesome.io/) for icons, I only use a few icons for the social networks (11 icons in total) however I have to include a font file that contain 675 icons. I tried finding nice tools to easily create a subset of the font however most of them just didn't work with icon fonts and the ones that did were very manual requiring you to find the glyphs you want to keep manually. For these reasons I wanted to make a tool to create subsets of fonts that can easily and automatically create the crushed fonts.

## Example

 The [example folder](/example) contains code that can be automatically run to compress the font used on an example website, the example website is based of my website and the icons I used on it.

Before the compression the `.ttf` file size was 165,548 Bytes and the `.css` file was 31,000 Bytes after crushing both the `.ttf`and `.css` the file sizes were 3,276 Bytes and 3,995 Bytes respectively. That is a saving of 189277 Bytes (189 kB) which is 3.4% of the orignial file size.

    (165,548+31,000)-(3,276+3,995) = 189277 Bytes (189 kB)
    (3,276+3,995)/(165,548+31,000) = 3.4%

## The Tools

#### - crush\_font

The main tools is `crush_font` this is the tool that actually removes all unwanted glyphs from a font object. Example use;

``` python
import fontcrusher
crushed_font = fontcrusher.crush_font(font_object, glyph_names)
```

To find the `glyph_names` automatically the following tools can be used.

#### - find\_used\_glyphs

This tool finds all the glyphs you have used within a project/website automatically.

``` python
from fontcrusher.find_used_glyphs import *
regex_for_find = get_regex_for_glyph('font_awesome')
include = [[r'.\website_folder\**\*', {'recursive': True}]]
exclude = [[r'.\website_folder\subdirectory\exclude_file.txt']]
used_glyphs = find_used_glyphs(include, regex_for_find, exclude_args=exclude)
```

#### - get\_glyph\_name
Once you know the glyphs you have used you need to find out their glyph name.

One problem with this is the names of glyphs are not always consistent e.g in [Font Awesome](http://fontawesome.io/) four different naming conventions seem to be used.

* `'cc-visa'` (Visa) has a glyph name of `'uniF1F0'`
* `'cc-mastercard'` (Mastercard) has a glyph name of `'_466'`
* `'cc-amex'` (American Express) has a glyph name of `'f1f3'`
* `'credit-card'` (Credit Card) has a glyph name of `'credit_card'`

`get_glyph_name` can be used to first find the Unicode value of all the `used_glyphs` from their CSS names, after their Unicode value is known the actual glyphs name can be found.

``` python
from fontcrusher.get_glyph_name import *
unicode_values = get_unicode_value_list('fa', used_glyphs, css_file).values()
glyph_names = get_glyph_name_list(font_object, unicode_values).values()
```

#### - css_crush

Not only would you want to crush your font but you probably want to compress the CSS file for the font too. The CSS files of icon fonts contain information for each glyph, this removes the information for all unused glyphs it does not also minimize the CSS file.

``` python
from fontcrusher import css_crush
css_file = css_crush.read_file(r'.\website_folder\font-awesome.min.css')
crushed_css = css_crush.remove_glyphs_from_css(css_file, 'font_awesome', used_glyphs)
css_crush.write_file(r'.\website_folder\font-awesome.crushed.css', crushed_css)
```

## Benefits of FontCrusher

Smaller file sizes means that your website will load much faster and will put less strain on your server. Faster loading websites are much better for users and ranks you better on search engines such as Google. Font icons can be used in programs and applications, FontCrusher can be used to reduce the file size of your application.

FontCrusher can be run automatically to find the used glyphs in a project and crush the font/CSS with no manual intervention.

CDNs could be used for many of the popular fonts so will reduce the bandwidth on your server so you may be inclined to use them. CDNs are a good option in some cases however they will not load as fast, users will use more data, your site will be slower and potentially rank lower on Google. CDNs also have other issues associated with them they can track users and [can reduce peoples privacy](http://webmasters.stackexchange.com/questions/60464/are-there-privacy-considerations-in-using-google-web-fonts) online for this reason some people disable CDNs to stop tracking and some adblocking extensions block these CDNs, using a CDN may break your site for these users. CDNs also can't be used in offline applications/websites.

## Extra Notes

FontCrusher can save fonts in `.ttf` and `.woff` (and `.woff2` if brotli is installed) these formats can be used by most browsers however some old browsers need other formats too. These other formats for example `.svg` and `.eot` can be created with other tools or by using free web services e.g https://transfonter.org/.

## License

This project is licensed under the AGPLv3 License, if you want to use this code under any other licence just contact me.
