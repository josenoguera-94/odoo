# ODOO WITH DOCKER

**RUN**
```
docker-compose up
```

https://www.youtube.com/@OdooMates/playlists

https://www.odoo.com/documentation/16.0/ko/developer/reference/cli.html

## How connect to db of odoo.sh by ssh
1. `ssh -v -L 5432:localhost:5432 -N <user>@<your-odoo-sh>.odoo.com` `<user>` and `<your-odoo-sh>` are your odoo.sh account and odoo.sh domain.
2. entry to odoo sh console and type `env` to get credentials of db:  `PGUSER`, `PGPASSWORD`, `PGDATABASE`. the host and port are `localhost` and `5432`.
3. `psql -h localhost -p 5432 -U <PGUSER> -d <PGDATABASE>` and type password. or you can use `pgadmin` to connect to db.


# ODOO 14 Part 31-32 Agregar un nuevo campo al empleado (modulo ya creado) Sobreescribir el modelo existente y uso domain (como un where en sql)

Cuando se creee un modulo nuevo que no se olvide dar permisos en settings/users

http://127.0.0.1:8069/web#action=87&model=res.config.settings&view_type=form&cids=1&menu_id=4

/usr/bin/odoo scaffold my_module /mnt/extra-addons
sudo chmod -R 777 ./addons/my_module/
python odoo-bin scaffold <module_name> <path>

docker exec -it 7df436518167 bash

python odoo-bin -r dbuser -w dbpassword --addons-path=addons,modules -d mydb -i base -U <module_name>,<module_name>..

-U es para actualizar el modulo cada vez que se reinicie el contenedor

https://www.odoo.com/documentation/18.0/es/developer/reference/frontend/framework_overview.html

https://www.odoo.com/documentation/18.0/es/contributing/development/coding_guidelines.html
https://www.odoo.com/documentation/18.0/developer/tutorials/backend.html

odoo-bin -i <module_name>  es para instalar el modulo

en odoo sh , `src/user` se encuentra los modulos que hemos creado