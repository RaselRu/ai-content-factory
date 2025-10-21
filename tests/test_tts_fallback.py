diff --git a/tests/test_tts_fallback.py b/tests/test_tts_fallback.py
new file mode 100644
index 0000000000000000000000000000000000000000..d8f798b749e81ebcf11c7e50ae432cfb11a65585
--- /dev/null
+++ b/tests/test_tts_fallback.py
@@ -0,0 +1,9 @@
+from ai_content_factory.content.tts import TextToSpeechEngine
+
+
+def test_tts_silence_fallback(tmp_path):
+    engine = TextToSpeechEngine(preferred_provider="unknown")
+    output_path = engine.synthesize("test text", tmp_path)
+    assert output_path.exists()
+    assert output_path.stat().st_size > 0
+    assert output_path.suffix in {".wav", ".mp3"}
