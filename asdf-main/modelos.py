from abc import ABC, abstractmethod
from datetime import datetime

import bcrypt

class Empleado():
    def __init__(self, id_empleado, nombre, direccion, fono, email, f_inicio_contrato,
                 salario, rut):
        self.id_empleado = id_empleado
        self.nombre = nombre
        self.direccion = direccion
        self.fono = fono
        self.email = email
        self.f_inicio_contrato = f_inicio_contrato
        self.salario = salario
        self.rut = rut
        self._credenciales = None             
        self._departamento = None                  
        self._proyectos = []
        self._registros = []

class Credenciales:
    def __init__(self, usuario):
        self.__usuario = usuario
        self.__salt = None
        self.__hash_contrasena = None

class Departamento:
    def __init__(self, num_dep, nombre_dep, gerente_asociado, tipo_dep):
        self.num_dep = num_dep
        self.nombre_dep = nombre_dep
        self.gerente_asociado = gerente_asociado
        self.tipo_dep = tipo_dep
        self.__empleados = [] 


class Proyecto:
    def __init__(self, nombre_proyecto, descripcion, fecha_inicio):
        self.nombre_proyecto = nombre_proyecto
        self.descripcion = descripcion
        self.fecha_inicio = fecha_inicio
        self.__empleados = []   

class RegistroTiempo:
    def __init__(self, fecha, horas_trabajadas, descr_tareas):
        self.fecha = fecha
        self.horas_trabajadas = horas_trabajadas
        self.descr_tareas = descr_tareas
        self.__aprobado = False

class administrador:
    def __init__(self, *datos, nivel_de_permisos="TOTAL"):
        super().__init__(*datos)
        self.nivel_de_permisos = nivel_de_permisos

class Gerente(Empleado):
    def __init__(self, *datos, dep_asignado=None):
        super().__init__(*datos)
        self.dep_asignado = dep_asignado

class EmpleadoComun(Empleado):
    def __init__(self, *datos, area_de_trabajo="General"):
        super().__init__(*datos)
        self.area_de_trabajo = area_de_trabajo

class RegistroEmpleados:
    def __init__(self, bd):
        self.__bd = bd
        self.lista_empleados = []
        self.fecha_ultima_mod = None
        