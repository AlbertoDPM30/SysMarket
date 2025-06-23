# -*- mode: python ; coding: utf-8 -*-
datas = []
binaries = []
hiddenimports = []

# Incluye manualmente pymysql
hiddenimports += [
    'pymysql', 
    'pymysql.constants.CLIENT', 
    'pymysql.err', 
    'pymysql.connections', 
    'pymysql.cursors',
    'fpdf',
    'fpdf.plugins'
]

# Agrega las carpetas y archivos necesarios para tu proyecto
datas += [('public', 'public'), ('modelos', 'modelos'), ('modulos', 'modulos'), ('./main.py', '.'), ('./db_conexion.py', '.')]

a = Analysis(
    ['login.py'],  # Archivo principal
    pathex=[],  # Puedes incluir rutas adicionales si necesitas
    binaries=binaries,
    datas=datas,
    hiddenimports=hiddenimports,
    runtime_hooks=[],  # No hay hooks necesarios en este caso
    excludes=[],  # No se excluyen paquetes
    noarchive=False,  # Usa un archivo comprimido .pyz
)

pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,  # Scripts principales
    a.binaries,  # Binarios empaquetados
    a.datas,  # Archivos adicionales empaquetados
    [],
    name='SysMarket',  # Nombre del ejecutable
    debug=False,  # Desactiva el modo de depuración
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=True  # Permite ver mensajes en la consola
)