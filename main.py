import cx_Oracle

connection = cx_Oracle.connect("system", "Tardes", "localhost/XE")

cursor = connection.cursor()
try:

    miOficio = input("Introduce Oficio Empleado:")
    consulta = ("SELECT apellido,oficio,salario FROM emp where oficio=:p1")
    cursor.execute(consulta, (miOficio,))
    # Si en un único parámetro tenemos que poner ',' a continuación del valor de la variable
    resultado = False
    for ape, ofi, sal in cursor:
        print("Apellido: ", ape)
        print("Oficio: ", ofi)
        print("Salario: ", str(sal))
        resultado = True
    if resultado==False:
       print ("Sin resultados")



except connection.Error as error:
    print("Error: ", error)

connection.close()
