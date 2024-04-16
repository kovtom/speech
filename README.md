# Hangfelismerő és szöveg-felolvasó program

Ez a program képes hangot felismerni és a felismert szöveget hanggá alakítani.

## Használat

1. Indítsd el a programot. A program kéri, hogy beszélj a mikrofonba.
2. Miután beszéltél a mikrofonba, a program megpróbálja felismerni a hangot és szöveggé alakítani.
3. Ha a hangfelismerés sikeres, a program kiírja a felismert szöveget, majd hanggá alakítja és felolvassa.
4. Ha a hangfelismerés nem sikerül, a program kiírja, hogy "Nem sikerült felismerni a hangot!", majd ezt a szöveget hanggá alakítja és felolvassa.

## Virtuális környezet létrehozása és beállítása

A Python csomagok telepítése előtt ajánlott létrehozni egy virtuális környezetet (`venv`), hogy elkerüljük a függőségek konfliktusait. A virtuális környezet létrehozásához és aktiválásához kövesd az alábbi lépéseket:

1. Nyisd meg a terminált és navigálj a projekt könyvtárába.
2. Hozd létre a virtuális környezetet a következő paranccsal: `python3 -m venv venv`
3. Aktiváld a virtuális környezetet a következő paranccsal: `source venv/bin/activate`

Most már készen állsz a függőségek telepítésére a virtuális környezetben.

További információk a virtuális környezetekről és a beállításukról a [Visual Studio Code dokumentációjában](https://code.visualstudio.com/docs/python/environments) találhatók.

## Függőségek

A program a következő Python csomagokat használja:

- `speech_recognition`: A hangfelismeréshez. `pip install SpeechRecognition`
- `gtts` (Google Text-to-Speech): A szöveg hanggá alakításához.
- `pyaudio`: Hang kezeléséhez.
- `setuptools`: Python csomag létrehozására.

Ezeket a csomagokat a `pip install` parancs segítségével telepítheted.

## Megjegyzések

A program a Google Speech Recognition API-t használja a hangfelismeréshez, és a Google Text-to-Speech API-t a szöveg hanggá alakításához. Ezek az API-k internetkapcsolatot igényelnek a működéshez.
