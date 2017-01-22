#Aqui colocamos toda la documentacion con muchos ejemplos para facilitar la comprension al usuario de la funcionalidad de nustro paquete.


Nos ubicamos en la carpeta dond esta nuestro archivo setup.py
desde la terminal

Lo ejecutamos dos veces la primera para autenticar la segunda para subir el proyecto

python3 setup.py register -r pypi

nos marca un warning

python3 setup.py register sdist upload -r pypi

ya se sube el archivo 
responde con status 200 quiere decir que nuestro archivo ya se subio