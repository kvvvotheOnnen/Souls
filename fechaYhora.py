import datetime
import pytz

def fechaYhora():
    mi_zona_horaria = pytz.timezone('America/Santiago')
    now = datetime.datetime.now(mi_zona_horaria)
    hora_actual = now.strftime("%H:%M:%S")
    fecha_actual = now.strftime("%Y-%m-%d")
    fecha = f"{fecha_actual} {hora_actual}"
    return fecha