class Estudiante:
    def __init__(self, nombre, edad, cursos_inscritos):
        self.nombreombre = nombre
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
    
