# Hangfelismerő és szöveg-felolvasó program

Ez a program képes hangot felismerni és a felismert szöveget hanggá alakítani.

## Használat

1. Indítsd el a programot. A program kéri, hogy beszélj a mikrofonba.
2. Miután beszéltél a mikrofonba, a program megpróbálja felismerni a hangot és szöveggé alakítani.
3. Ha a hangfelismerés sikeres, a program kiírja a felismert szöveget, majd hanggá alakítja és felolvassa.
4. Ha a hangfelismerés nem sikerül, a program kiírja, hogy "Nem sikerült felismerni a hangot!", majd ezt a szöveget hanggá alakítja és felolvassa.

## Függőségek

A program a következő Python csomagokat használja:

- `speech_recognition`: A hangfelismeréshez.
- `gtts` (Google Text-to-Speech): A szöveg hanggá alakításához.
- `os`: Az operációs rendszer műveleteinek végrehajtásához.
- `setuptools`: Python csomag létrehozására

Ezeket a csomagokat a `pip install` parancs segítségével telepítheted.

## Megjegyzések

A program a Google Speech Recognition API-t használja a hangfelismeréshez, és a Google Text-to-Speech API-t a szöveg hanggá alakításához. Ezek az API-k internetkapcsolatot igényelnek a működéshez.
