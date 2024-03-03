
from classroom.asignatura import Asignatura

class Grupo:
    grado = None

    def __init__(self, grupo="grupo ordinado", asignaturas=None, estudiantes=None):
        self._grupo = grupo
        self._asignaturas = asignaturas if asignaturas else []
        self.listadoAlumnos = estudiantes if estudiantes else []

    def listadoAsignaturas(self, **kwargs):
        for x in kwargs.values():
            self._asignaturas.append(Asignatura(x))

    def agregarAlumno(self, alumno, lista=None):
        if lista is None:
            lista=self.listadoAlumnos
        lista.append(alumno)
        self.listadoAlumnos = lista

    def __str__(self):
         return f"Grupo de estudiantes: {self._grupo}"

    @ classmethod
    def asignarNombre(self):
        self.grado = "Grado 10"

    
