# pip install gTTS

from gtts import gTTS
import os

# Texto que quieres convertir a audio
texto_largo = """
El Ocaso Siniestro
El calor del asfalto aún se sentía a través de las suelas de mis sandalias, incluso dentro del auto. Un resplandor anaranjado teñía el horizonte, señal de que el día se extinguía lentamente. "¿Casi llegamos?", pregunté, mi voz teñida de
impaciencia y emoción. Llevábamos horas en la carretera, rumbo a unas merecidas vacaciones en la costa, y la idea de sentir la arena bajo mis pies era el único motor que me mantenía despierta. Juan sonrió, apretando mi mano. "Unas pocas
horas más, mi amor. Ya verás que el esfuerzo vale la pena". Justo en ese momento, un sonido gutural, como si el motor estuviera a punto de rendirse, nos sacudió. El auto dio un brinco, tosió, y luego, un silencio sepulcral nos envolvió.
La aguja del velocímetro cayó a cero, y el motor se apagó por completo.

Juan intentó encenderlo varias veces, pero fue inútil. "Maldición", masculló, golpeando el volante con frustración. Estábamos en medio de la nada, rodeados por un bosque denso que parecía engullir la poca luz restante. El aire se volvió
pesado, la brisa de la tarde traía consigo un olor a tierra húmeda y algo más... algo indescifrable. "No te preocupes", dijo Juan, forzando una sonrisa. "Voy a caminar hasta encontrar ayuda. Seguramente hay algún pueblo cerca". Me dio un
beso rápido, tomó una botella de agua y se adentró en la oscuridad creciente del bosque. La luz del día se desvanecía rápidamente, arrastrando consigo la sensación de seguridad. El sol finalmente se hundió por completo, y la noche se
abalanzó sobre el coche como un depredador silencioso. Afuera, los sonidos del bosque comenzaron a intensificarse: el ulular de un búho, el crujir de las hojas bajo lo que parecía ser pasos. Mi corazón latía desbocado. ¿Y si Juan no
encontraba a nadie? ¿Y si algo le había pasado? La oscuridad se cernía, y con ella, una sensación de que no estaba sola en ese auto varado. Un escalofrío me recorrió la espalda cuando, a través del parabrisas empañado, juraría haber
visto una sombra moverse justo al borde del bosque, observando el coche.
"""

# Idioma en el que se hablará el texto.
# 'es' es para español. Puedes probar otros como 'en' para inglés.
# La voz específica (masculina/femenina) dependerá del idioma y de la voz
# predeterminada de Google para ese idioma. gTTS no permite elegir explícitamente
# el género, pero puedes experimentar con diferentes códigos de idioma o
# configuraciones regionales (parámetro 'tld') si buscas una voz particular.
idioma = 'es'

try:
    # Crear el objeto gTTS
    # El parámetro 'slow=False' hace que la velocidad de habla sea normal.
    # Puedes ponerlo en 'True' para una velocidad más lenta.
    tts = gTTS(text=texto_largo, lang=idioma, slow=True)

    # Nombre del archivo de audio que se guardará
    nombre_archivo = "mi_audio_generado.mp3"

    # Guardar el archivo de audio
    tts.save(nombre_archivo)

    print(f"¡El audio se ha guardado como '{nombre_archivo}'!")
    print(f"Puedes encontrarlo en el directorio: {os.getcwd()}")

    # Opcional: reproducir el audio automáticamente (puede no funcionar en todos los entornos)
    # Para Windows: os.system(f"start {nombre_archivo}")
    # Para macOS: os.system(f"open {nombre_archivo}")
    # Para Linux: os.system(f"xdg-open {nombre_archivo}")

except Exception as e:
    print(f"Ocurrió un error: {e}")