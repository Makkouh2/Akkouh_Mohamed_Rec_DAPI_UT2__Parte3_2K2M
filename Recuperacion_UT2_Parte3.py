def calculate_grade(practica01, practica02, practica03, examen,recuperacion, actitud):
    """Funcion me calcula la nota final de cada alumno
       
        parametros:
        - Practica01=Nota float
        -Practica02=Nota float
        -Practica03=Nota float
        -Practica04=Nota float
        -Examen=Nota float
        -Recuperación=Nota float
        -Actitud=Nota float


        salida:
        - Nota final: nota del alumno
        -Aprobado : boleano true o false 
        """
    notafinal = ((practica01 + practica02 + practica03) / 3) * 0.3 + max(examen, recuperacion) * 0.6 + actitud * 0.1
    
    if notafinal>= 5:
        aprobado = True
    else:
        aprobado = False

    return notafinal, aprobado
        
print(calculate_grade(5,3,6,7,8,9))

    

