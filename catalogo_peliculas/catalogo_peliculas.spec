# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

a = Analysis(
    ['catalogo_peliculas.py'],  # Archivo principal
    pathex=['.'],  # Carpeta actual (ajusta si es necesario)
    binaries=[],
    datas=[
        ('img', 'img'),           # Incluye carpeta img
        ('database', 'database'), # Incluye carpeta database
    ],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='Catalogo_Peliculas',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,  # Oculta la consola (ventana negra)
    disable_windowed_traceback=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon='img/cp-logo.ico'  # Opcional: ícono del .exe
)

coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='Catalogo_Peliculas'
)