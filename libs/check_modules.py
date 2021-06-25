import sys

def check_modules():
    try:
        import requests
    except:
        print_error("'requests' module not found!")
        print_status("run install_requirements.bat to install the modules")
        sys.exiprint_errort(0)

    try:
        import colorama
    except Exception as e:
        print_error("'colorama' package not installed!")
        print_status("run install_requirements.bat to install the modules")
        print(e)
        sys.exit(0)

    try:
        import asyncio
    except:
        print_error("'asyncio' package not installed!")
        print_status("run install_requirements.bat to install the modules")
        sys.exit(0)

    try:
        import proxybroker
    except:
        print_error("'proxybroker' package not installed!")
        print_status("run install_requirements.bat to install the modules")
        sys.exit(0)

    try:
        import warnings
    except:
        print_error("'warnings' package not installed!")
        print_status("run install_requirements.bat to install the modules")
        sys.exit(0)

    import warnings
    warnings.filterwarnings("ignore")

    from colorama import init
    init()
