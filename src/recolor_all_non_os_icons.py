from pathlib import Path

THIS_FILE = Path(__file__)

icons_src_dir = THIS_FILE.parent / 'icons'
icons_out_dir = THIS_FILE.parent.parent / 'icons'

for prefix in ('arrow_', 'func_', 'tool_', 'vol_'):
    for icon in icons_src_dir.glob(f'*/{prefix}*.png'):
        icon_sub_path = icon.relative_to(icons_src_dir)
        icon_out_path = icons_out_dir / icon_sub_path
        print(f"INVERT_COLOR='' python recolor_png.py {icon} {icon_out_path}")

