import remesa.settings as settings


def remesa(request):
    return {"STORE_NAME": getattr(settings, "STORE_NAME", None)}
