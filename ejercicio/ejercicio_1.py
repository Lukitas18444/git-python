# Este curso duro 1.5 horas, los demas duraron: el minimo 2.5, promedio 4h, maximo 7h
#a)diferencia en porcentaje entre el actual y los demas cursos
#b)procentaje de material inserbible se reduce en ambos casos
#c)ver 10 horas de este curso, seria equivalente a cuantas horas de los demas cursos y al reves

#a)
otros_cursos_min = 2.5
otros_cursos_max = 7
otros_cursos_promedio = 4

dalto_curso = 1.5

diferencia_con_min = int(100 - dalto_curso / otros_cursos_min * 100)
diferencia_con_max = int(100 - dalto_curso / otros_cursos_max * 100)
diferencia_con_promedio = int(100 - dalto_curso / otros_cursos_promedio * 100)

print(f"el curso de Dlato dura un {diferencia_con_min}% menos que el mas rapido")
print(f"el curso de Dlato dura un {diferencia_con_max}% menos que el mas lento")
print(f"el curso de Dlato dura un {diferencia_con_promedio}% menos que el promedio")
print("---------------------")
#B)
crudo_promedio = 5
crudo_dalto = 3.5

tiempo_vacio_promedio = int(100 - otros_cursos_promedio / crudo_promedio * 100)
tiempo_vacio_dalto = int(100 - dalto_curso / crudo_dalto * 100)

print(f"un curso promedio elimina un {tiempo_vacio_promedio}% de tiempo vacio")
print(f"un curso de Dalto elimina un {tiempo_vacio_dalto}% de tiempo vacio")
print("-------------------------")

#c)
print(f"Ver 10 horas de este curso equivale a ver {otros_cursos_promedio * 100 // dalto_curso / 10} horas de otros cursos")
print(f"Ver 10 horas de otros cursos equivale a ver {dalto_curso * 100 // otros_cursos_promedio / 10} horas de otros cursos")
