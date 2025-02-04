# ODOO
se basa en un patrón MVC

## Structura de carpetas
[img](folder_structure_odoo.jpg)

**Structura**

1. **Models:** Contiene los modelos
2. **Views:** Vistas
3. **Static:** Archivos estáticos
4. **data:** guarda los datos que se precargan cuando al instalar el modulo (datos necesarios para que el modulo funcione) 
5. **wizard:** todas las ventanas emergentes de un formulario
6. **demo:** datos que se precarguen pero la demo,  tener valores de demo
7. **tests:** pruebas unitarias del modulo
8. **security:** archivos de permisos o xml que agrupa o crea los grupos de seguridad de lo susuarios
9.  **report:** archvios qde reportes
10. **controller:** archivos de website, todos los controladores
11. **i18n:** todas las traduciones del modulo, archivos .po 
12. **__init__.py** se indica todos los modelos y archivos .py que estan dentro de las carpetas,  para hacer importaciones
13. **__manifest__.py** (imporante) si no existe odoo no detecta el modulo, se colocar el nombre la descripcion y todo la info con respecto a este modulo y algunas configuraciones
14. **doc:** Carpeta de documentación

**Estructura con scaffold**

- controllers
- demo
- models
- security
- views

**Local host**
- http://localhost:8069/

**Modo desarrollador**
Colocar en la url debug=1

`http://localhost:8082/web?debug=1#action=35&cids=1&menu_id=5&model=ir.module.module&view_type=kanban`


## **odoo.conf**

```
db_host = localhost
db_maxconn = 64
db_name = 
db_password = openpgpwd
db_port = 5432
db_sslmode = prefer
db_template = template0
db_user = openpg

addons_path = #ruta de los folders para personalizar módulos
admin_passwd = admin
```

## **Como tener varias versiones de python y varias versiones de odoo en la misma máquina**

### **Run odoo**

`python odoo-bin -c odoo.conf`

`python odoo-bin -c odoo.conf -d datatest -i base` -d para que se conecte a esa db y -i para que la cree si no existe

`./odoo-bin -c /etc/odoo-server.conf -d data_base_name -u module_name`

`python odoo-bin -c odoo.conf -u <nombre_modulo>`
`python odoo-bin -c odoo.conf -d datatest --dev=all` para que actualice los cambios sin tener que para la instacia

## **Primer modulo**

`__manifesf__.py` 

como mínimo para que una app aparezca:

```
{
    'name': 'primero',
    'application': True
    # 'version': '0.1',
    # 'category': 'Marketing',
    # 'description': """sdasdas
    # """,
    # 'depends': [],
    # 'data': [],
    # 'demo': [],
    # 'installable': True,
    # 'auto_install': False,
}
```

[img](__manifest__.jpg)


**Definiendo accesos**

en ir.model.access.csv se definen los accesos
**Nota:** hay que validar si los permisos están configurados, si no hay que colocarlos

```
id: access_<nombre_del modulo>_custom_<Nomnre de la entidad>

```

**Asignar permisos a grupos de usuarios**

```
ajustes > tecnico > permisos de acceso > Crear, (creas uno nuevo)
```

**Crear modulo con scafold**


**Creando un modelo**

al crear un modelo nuevo, la tabla nueva que se crea tiene por defecto:

- create_uid: quien creo el registro
- create_date: cuando lo creo
- write_uid: quien modifico el registro
- write_date: cuando se modifico



## EN WINDOWS

cd "C:\Program Files (x86)\Odoo 13.0\server"
C:\Program Files (x86)\Odoo 13.0\python\python.exe" odoo-bin -c odoo.conf


DE OTRA MANERA
1. CREAR VENV
2. INSTALAR REQUIREMENTS
3. CREAR ARCHIVO ODOO.CONF Y CONFIGURARLO
4. EJECUTAR python odoo-bin -c odoo.conf


CREAR UN MODULO

python odoo-bin scaffold custom_module addons      (addons es la carpeta de elos addons) 


web?debug=1


**Relaciones**

- **Unos a muchos:** Varias visitas comerciales asociadas a un cliente 
  - `odoo.fields.Many2one`
  - `customer_id = fields.Many2one(string="CLiente", comodel_name="res.partner")`

- **Muchos a uno:** Un cliente puede tener varias visitas comerciales
  - `odoo.fields.One2many`
  - `customer_id = fields.One2Many(string="Visitas", comodel_name="custom_crm.visit")`
- **Muchos a Muchos**
  - `odoo.fields.Many2many`

**Campos computados o calculados**

@api.depends
@api.onchange (se recacula cuando otro campo esmodificado)