## Audiobookshelf Rename From Metadata
This script generates a bash script which renames folders in an [Audiobookshelf](https://github.com/advplyr/audiobookshelf) Library based on metadata.

## DO NOT USE THIS UNLESS YOU ARE ABSOLUTELY POSITIVE YOU UNDERSTAND WHAT YOU ARE DOING
This script is currently set up to conform to my personal settings and preferences. Specifically it produces folder names in `TITLE - SUBTITLE {Narrator}` format. If the book is a part of one and only one series, it will prepend the book number, resulting in folders in `BOOK#. TITLE - SUBTITLE {Narrator}` format. If you're familiar with python, it shouldn't bee too hard to adjust it to your preferences.

Notably, it does NOT currently move folders, so the assumption is that you already have your folders in their correct `LIBRARY/AUTHOR/SERIES(optional)/` locations. Or you can move them around afterwards.

I HIGHLY recommend manually reviewing the output script before running it. This tool can absolutely cause chaos in your library if you aren't paying attention. I am not responsible for any lost or disorganized data as a result of your choice to use this script.

## Current Status

Currently this is only tested on Linux and probably works on MacOS. It could be quickly made to work on a Windows machine with fairly minor tweaks to the constants and
```python
f.write (f'mv "{root}" "{DELIMITER.join(path)}"\n')
```

#### This could be the start of a useful ABS feature, but there are a number of issues that would need to be addressed first.

1. There are a number of sanity checks that are not necessary with my particular situation, but that need to be adressed before any sort of deployment
    - If any series name listed in metadata.abs contains `', ' or ' #'`, you can expect bad behavior.
2. The entire structure of the program revolves around the assumption that metadata is set to be stored in folders alongside audiobooks.
3. This should probably be rewritten in JavaScript, since the project doesn't currently use python, and there's nothing about this that couldn't be done with node.
4. Instead of creating a script, it should verify the changes and then actually do the rename through the ABS interface. I'm using the bash script as an intermediary to accomplish this, but it's probably not a good solution for prod.