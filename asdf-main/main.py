import os
from datetime import datetime
from getpass import getpass

from conexion import conexiondb
from modelos import (Administrador, Gerente, EmpleadoComun, Departamento, Proyecto,
                     RegistroEmpleados, Credenciales, PDF, Excel)