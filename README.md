##Audiobookshelf Rename From Metadata
This script generates a bash script which renames folders in an [Audiobookshelf](https://github.com/advplyr/audiobookshelf) Library based on metadata. It's currently set up to conform to my personal settings and preferences.

Currently this is only tested on Linux and probably works on MacOS. It could be quickly made to work on a Windows machine with fairly minor tweaks to the constants and
```python
f.write (f'mv "{root}" "{DELIMITER.join(path)}"\n')
```

####This could be the start of a useful ABS feature, but there are a number of issues that would need to be addressed first.

1. There are a number of sanity checks that are not necessary with my particular situation, but that need to be adressed before any sort of deployment
1. - If any series name listed in metadata.abs contains `', ' or ' #'`, you can expect bad behavior.
2. The entire structure of the program revolves around the assumption that metadata is set to be stored in folders alongside audiobooks.
3. This should probably be rewritten in JavaScript, since the project doesn't currently use python, and there's nothing about this that couldn't be done with node.
4. Instead of creating a script, it should verify the changes and then actually do the rename through the ABS interface. I'm using the bash script as an intermediary to accomplish this, but it's probably not a good solution for prod.