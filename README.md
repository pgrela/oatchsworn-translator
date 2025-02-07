# oatchsworn-translator

This repository contains a set of scripts that I found useful to translate an Oathsworn apk to other languages using AI generated voice.

## step by step
A chaotic manual below.

### Overview
The idea is to recompile the apk file from https://www.shadowborne-games.com/pages/oathapp using `./prepare-input.bat`
then run `./main.py` and recompile using `recompile-apk.bat`

First run might download some gigabytes(!) for text-to-speach neural network model

### Other tools
* `prepare-input.bat` uses https://github.com/REAndroid/APKEditor .jar
* You also need `apksigner.bat` that comes with Android studio I believe
* generate the release key:
```shell
keytool -genkey -v -keystore my-release-key.keystore -alias alias_name -keyalg RSA -keysize 2048 -validity 10000
```
`f7R14dZFsG443LmW0l` was the password :)

### `deepl_auth.py` file
Create `deepl_auth.py` file. The `deepl_auth.py` file should contain your deeply api key:

```python
deepl_auth_key = "23456789-qwertyuiop-1234567"
```
### chapter by chapter
Remember to set `chapter = 1` in `main.py` to desired chapter. This is meant to translate the app chapter by chapter, so it does not exhaust your deeply free account limit and you can add new phrases to your glossary in the meantime.

### language

Similarly set `target_language` in `main.py`

## Support
This works for me on my machine. I don't think I would be able to help you with troubleshooting :/
