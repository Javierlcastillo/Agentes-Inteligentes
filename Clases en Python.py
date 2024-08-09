class Estudiante:
    def __init__(self, nombre, edad, cursos_inscritos):
        self.nombre = nombre
        self.edad = edad
        self.cursos_inscritos = [] 

    def curso_inscrito(self,curso):
        if curso not in self.cursos_inscritos:
            self.cursos_inscritos.append(curso)

    def darse_de_baja(self,curso):
        if curso in self.cursos_inscritos:
            self.cursos_inscritos.remove(curso)
    
    def ver_cursos_inscritos(self):
        return self.cursos_inscritos
    
class Curso:
    def __init__(self, nombre_curso, horario):
        self.nombre_curso = nombre_curso
        self.horario = horario
        self.estudiantes_inscritos = []
    def inscribir_estudiante(self, estudiante):
        if estudiante not in self.estudiantes_inscritos:
            self.estudiantes_inscritos.append(estudiante)
    def baja_de_estudiante(self, estudiante):
        if estudiante in self.estudiantes_inscritos:
            self.estudiantes_inscritos.remove(estudiante)
    def ver_estudiantes_inscritos(self):
        return self.estudiantes_inscritos

# Creación de instancias
estudiante1 = Estudiante("Jesús", 20)
estudiante2 = Estudiante("María", 22)
estudiante3 = Estudiante("José", 19)
estudiante4 = Estudiante("Rosario", 24)
estudiante5 = Estudiante("Pablo", 20)
estudiante6 = Estudiante("Magdalena", 21)

curso1 = Curso("Matemáticas", "Lunes y Miércoles")
curso2 = Curso("Historia", "Martes y Jueves")

# Inscripción a cursos
curso1.inscribir_estudiante(estudiante1)
curso1.inscribir_estudiante(estudiante2)
curso1.inscribir_estudiante(estudiante5)
curso1.inscribir_estudiante(estudiante6)
curso1.inscribir_estudiante(estudiante2)
curso2.inscribir_estudiante(estudiante1)
curso2.inscribir_estudiante(estudiante3)
curso2.inscribir_estudiante(estudiante4)
curso2.inscribir_estudiante(estudiante6)
print(">> DESPUÉS DE LAS INSCRIPCIONES <<")
estudiante1.ver_cursos_inscritos()
estudiante2.ver_cursos_inscritos()
estudiante3.ver_cursos_inscritos()
estudiante4.ver_cursos_inscritos()
estudiante5.ver_cursos_inscritos()
estudiante6.ver_cursos_inscritos()
curso1.ver_estudiantes_inscritos()
curso2.ver_estudiantes_inscritos()

# Baja de cursos
estudiante1.darse_de_baja(curso1)
estudiante2.darse_de_baja(curso1)
estudiante3.darse_de_baja(curso1)
estudiante6.darse_de_baja(curso2)
print("\n>> DESPUÉS DE LAS BAJAS <<")
estudiante1.ver_cursos_inscritos()
estudiante2.ver_cursos_inscritos()
estudiante3.ver_cursos_inscritos()
estudiante4.ver_cursos_inscritos()
estudiante5.ver_cursos_inscritos()
estudiante6.ver_cursos_inscritos()
curso1.ver_estudiantes_inscritos()
curso2.ver_estudiantes_inscritos()
