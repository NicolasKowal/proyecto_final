# Choque la pata!
Este es el proyecto final del curso Python dictado por Coderhouse, fue realizado en conjunto por Nicolas Kowalkiewicz y Virginia Bottino.

El proyecto es una página de adopción de mascotas, donde los usuarios pueden ver y consultar mascotas en adopción o  publicar alguna.

Se puede ingresar al panel de administración de Django utilizando el nombre de usuario "ADMIN" y la contraseña "admin".

Desde la página principal, en la barra superior se puede acceder a:
- Conocenos: una vista donde se presentan los creadores del proyecto.
- Agregar Mascota: una vista de creación, para poder publicar una mascota en adopción. Si el usuario no está logueado redirige al login.
- Adoptar: una vista de lista de mascotas en adopción. En la misma se puede filtrar por especie. Si el usuario está logueado permite ver los detalles (sino el botón "Ver" redirige al login). En las mascotas que hayan sido creadas por el usuario logueado también aparecerán las opciones de "Borrar" y "Editar".
- Login: lleva a la vista de login. Esta tiene debajo un botón para registrarse.
- Registrarme: lleva al formulario de registro.

Una vez que el usuario está logueado el botón "Login" y "Registrarme" ya no se muestran más. En su lugar se pueden ver: 
- Usuario: se muestra el nombre de usuario y avatar (si es que tiene).
- Mi perfil: lleva a un formulario de edición del usuario, desde donde se modifica nombre, apellido, email, contraseña y avatar.
- Logout: cierra la sesión y muestra una vista con opciones de login y registrarse.
LINK AL VIDEO SUBIDO A YOUTUBE https://youtu.be/wJlrSCcDxFw
