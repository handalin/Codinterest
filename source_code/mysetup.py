from distutils.core import setup
import py2exe

setup (
    options = {
        "py2exe":{
            "dll_excludes": ["MSVCP90.dll","OLEAUT32.dll","USER32.dll",
                             "gdiplus.dll","SHELL32.dll","ole32.dll",
                             "COMDLG32.dll","WSOCK32.dll","COMCTL32.dll",
                             "ADVAPI32.dll","WS2_32.dll","GDI32.dll",
                             "WINMM.dll","KERNEL32.dll","RPCRT4.dll",
                             "WINSPOOL.DRV"],
            #"drv_excludes": ["WINSPOOL.DRV"],
        }
    }
    ,windows=["Codinterest.py"]
)
