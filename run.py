import importlib.util
import os

# ဖိုင်နာမည်အရှည်ကြီးကို သတ်မှတ်ခြင်း
FILENAME = "aa.cpython-313-aarch64-linux-android.so"

def start():
    if not os.path.exists(FILENAME):
        print(f"Error: {FILENAME} not found!")
        return

    try:
        # ဖိုင်နာမည် ဘယ်လောက်ရှည်ရှည် 'aa' အနေနဲ့ import လုပ်မယ်
        spec = importlib.util.spec_from_file_location("aa", os.path.abspath(FILENAME))
        aa = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(aa)

        # aa.so ထဲက main() function ကို run မယ်
        aa.main()
        
    except Exception as e:
        print(f"Runtime Error: {e}")

if name == "main":
    start()
