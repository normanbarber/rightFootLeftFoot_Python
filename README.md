# rightFootLeftFoot_Python
Identifies unused localization key/value pairs in a project.
This is a variation on a small utility program called CommandL10n. Recursively reads the directory and its sub-directories looking for and reading view files, eventually comparing localization string variables from the view files with keys from the locale file.
I used Python for this version. I want to re-write this simple utility in a few different languages to help me gauge my interest in learning more about each of them.

### example of returned array of unused localization string keys (  returns unused localization keys only )
```json
['started','exported','scheduled']
```

### Open getunusedL10n.py - you will be prompted twice. Once for the view folder and once for your localization file
```javascript
	> Enter path to your view files: "path\\to\\your\\view"
	> Enter path to your locales file: "path\\to\\your\\locale.json"
```
