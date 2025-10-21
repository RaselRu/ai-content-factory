# AI Content Factory — Horror Shorts Pipeline

Конвейер для автоматической генерации коротких хоррор-видео:
script → TTS → images → edit → SEO → Release (GitHub Release).

Быстрый старт локально:
1. Установите зависимости: ffmpeg, ImageMagick, Python 3.11, wget
2. Создайте виртуальное окружение и установите Python-зависимости (если добавите requirements.txt).
3. Запустите генерацию одного шорта:
   python3 tools/gen_script.py --id vid001 --lang ru --style creepypasta --dur 30
   python3 tools/tts_piper.py --text-file content/scripts/vid001.txt --out content/voice/vid001.wav --lang ru
   python3 tools/gen_images.py --id vid001 --prompt "horror scene" --count 4
   python3 tools/assemble_ffmpeg.py --id vid001 --imgs-glob "assets/images/vid001_*.jpg" --voice content/voice/vid001.wav --sfx assets/sfx/*.wav --dur 30

Запуск в Actions:
- Workflow `build_short.yml` — ручной запуск (workflow_dispatch) и планировщик (09:00 Asia/Almaty).
- Workflow `batch_build.yml` — пакетная генерация.

Hugging Face:
- Для генерации реальных кадров настройте secret HF_TOKEN (Repository → Settings → Secrets).
- Если HF_TOKEN отсутствует, используются тёмные плейсхолдеры.

Лицензии:
- SFX в assets/sfx должны быть CC0 (в репозитории добавлены placeholder-эффекты).

Трюки удержания:
- Сильный хук 1–3 сек;
- Низкий бас + шёпот на спаде (volume automation).