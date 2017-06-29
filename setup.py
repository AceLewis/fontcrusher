from setuptools import setup

setup(
    name='fontcrusher',
    version='0.1.1',
    description='A python module for reducing the size of fonts by removing unnessasary glyphs',
    long_description='A python module for reducing the size of fonts by removing unnessasary glyphs, it can also reduce the size of css used for fonts',
    keywords=['fontcrusher', 'font', 'subset', 'minify', 'compress', 'font subset'],
    url='http://github.com/AceLewis/fontcrusher',
    download_url='https://github.com/AceLewis/fontcrusher/archive/master.zip',
    author='AceLewis',
    maintainer='AceLewis',
    license='AGPLv3',
    packages=['fontcrusher'],
    install_requires=['fonttools'],
    classifiers=(
        'Natural Language :: English',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        "Natural Language :: English",
        "Operating System :: OS Independent",
        'License :: OSI Approved :: GNU Affero General Public License v3',
        "Topic :: Text Processing :: Fonts"
    ),
    zip_safe=False)
