# The Plot Classifier

![TPClogo](https://github.com/thebooort/The-Plot-Classifier/blob/master/images/logo/logoTPC.png)

## Any serious aspect you might find in this repo is purely coincidental

![](https://img.shields.io/github/issues/thebooort/The-Plot-Classifier)
![](https://img.shields.io/github/stars/thebooort/The-Plot-Classifier)
![](https://img.shields.io/github/license/thebooort/The-Plot-Classifier)
![](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat)
![](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)
![](https://badges.frapsoft.com/os/v1/open-source.png?v=103)

Hey! the tool you don't even know you need! 

Now with ̶t̶h̶e̶ ̶g̶l̶o̶r̶i̶o̶u̶s̶ ̶h̶u̶m̶a̶n̶k̶i̶n̶d̶ ̶e̶v̶o̶l̶u̶t̶i̶o̶n̶ Deep Learning inside!

(Silly summer project to know the name of that cool plot/chart/visualization you saw on a webpage)

## Current Accucracy per class


![TPClogo](https://github.com/thebooort/The-Plot-Classifier/blob/master/images/accuracy.png)



## Pasos

- Imagenes
- Prototipo
- Modelo final
- Deploy del modelo


### Tareas
- Descarga de imagenes
Para la descarga de imagenes estoy usando dos lineas de codigo desde la consola del navegador.
Pensé en generarlas yo mismo, pero no se a que nivel de variedad puedo llegar frente a las que puedo descargar desde -servicio online de imagenes nada conocido-.

	urls=Array.from(document.querySelectorAll('.rg_i')).map(el=> el.hasAttribute('data-src')?el.getAttribute('data-src'):el.getAttribute('data-iurl'));
	
Y despues descargo el archivo con las urls, para luego descargar las imagenes via script de python 

	window.open('data:text/csv;charset=utf-8,' + escape(urls.join('\n')));

- estandarización de las imagenes (posible data augmentation?)
- crear el modelo
  - prototipo con google teach lab ?
  - siguiente paso con keras?
  - ver lo que esta dando fuerte en este area
- Codear la pagina de streamlit
- añadirle el poder subir imagenes
- hacer deploy en heroku
