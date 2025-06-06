# pip install yt_dlp

import yt_dlp as youtube_dl

def descargar_video(url):
    ydl_opts = {
        'format': 'bestvideo+bestaudio/best', # Intenta obtener la mejor calidad de video y audio
        'outtmpl': '%(title)s.%(ext)s',
        'noplaylist': True # Añadido para asegurar que solo descarga el video si la URL es de una playlist
    }

    try:
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print(f"Video descargado exitosamente: {url}")
    except Exception as e:
        print(f"Error al descargar {url}: {e}")
        # Aquí podrías intentar con un formato más simple como fallback
        print("Intentando con un formato alternativo (best)...")
        ydl_opts['format'] = 'best'
        try:
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
            print(f"Video descargado exitosamente con formato 'best': {url}")
        except Exception as e_fallback:
            print(f"Error al descargar {url} con formato 'best': {e_fallback}")


# Sería mejor usar la URL directa del video si es posible
# url_video = "https://www.youtube.com/watch?v=XBIaqOm0RKQ"
url_video = "https://www.youtube.com/watch?v=XBIaqOm0RKQ" # Esta URL parece ser interpretada como el video con ID XBIaqOm0RKQ
descargar_video(url_video)