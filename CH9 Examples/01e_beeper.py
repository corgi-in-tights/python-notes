# 5.02 Exercise: Beeper

# This program plays beep.mp3 when run.
import os
import sys
from pathlib import Path

beep_path = Path.cwd() / "CH9 Examples" / "resources" / "beep.mp3"

if sys.platform == "darwin":  # macOS
    os.system(f"open '{beep_path}'")
elif sys.platform.startswith("win"):
    os.system(f'start "" "{beep_path}"')
elif sys.platform.startswith("linux"):
    os.system(f"xdg-open '{beep_path}'")
else:
    print("Unsupported OS. Cannot play beep.")

print("Beep sound should play!")
