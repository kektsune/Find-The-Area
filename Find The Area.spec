# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['Find The Area.py'],
    pathex=[],
    binaries=[],
    datas=[('Rectangle.png', '.'), ('Right Triangle.png', '.'), ('Isosceles Triangle.png', '.'), ('Full Circle.png', '.'), ('Semi Circle.png', '.'), ('Square.png', '.')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='Find The Area',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
