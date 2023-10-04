from pathlib import Path

THIS_FILE = Path(__file__)

icons_dir = THIS_FILE.parent.parent / 'icons'

for prefix in ('arrow_', 'func_', 'tool_', 'vol_'):
    for icon in icons_dir.glob(f'*/{prefix}*.png'):
        print(f"python recolor_png.py {icon} {icon}")

