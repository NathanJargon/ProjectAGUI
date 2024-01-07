# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['C:/Nash/Projects Folder/AGUI/main.py'],
    pathex=[],
    binaries=[],
    datas=[('C:/Nash/Projects Folder/AGUI/csv', 'csv/'), ('C:/Nash/Projects Folder/AGUI/db', 'db/'), ('C:/Nash/Projects Folder/AGUI/dist', 'dist/'), ('C:/Nash/Projects Folder/AGUI/img', 'img/')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='AGUI',
    debug=True,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=True,
    disable_windowed_traceback=True,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=['C:\\Nash\\Projects Folder\\AGUI\\img\\Huh!.ico'],
)
coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='AGUI',
)
