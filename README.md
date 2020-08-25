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

## Index

- [Motivation](#motivation)
- [Approach](#approach)
  - [Data Collect](#data-collect)
  - [ML Approach](#ml-approach)
	- [Neural Net architecture](#nn-architecture)
	- [Results](#results)
    - [Nets trained you can find here](#nets-trained)
  - [Streamlit](#streamlit)
	  - [Screenshots](#screenshots)
  - [Heroku](#heroku-deployment)



## Motivation 

This project was born from a personal doubt that I have come across several times: What is the name of that cool graphic? 
And I've always lost some time in finding the exact name or the way to call it of some bookstores. It is true that I talk about more complex graphics, but I decided that it could be interesting to start with the basics and perhaps at some point the tool can help some beginner to discover their first graphics. 

In addition, the main reason for this project was to try and play with the possibilities offered by streamlit as a way of providing a preliminary result in machine learning. In that aspect I think it has been a success, since I have acquired what is necessary to make an attractive and functional streamlit page with a model that I have implemented. 

## Approach

### Data collect

I didn't find anything usable on the internet. So I thought of two alternatives, one to generate my own graphics and the other to get them from some search engine. 

Generating my own graphics seemed very interesting and maybe in the future I will feed the system with randomly generated graphics, however I think that the investment of time would not be rewarded, as the options are endless.

On the contrary, I made the decision to get a group of images from the internet, using the search engines. Obiously the quality of the images (and I don't mean their quality in pixels) would decrease as the amount of images to extract from a single query search increases. I reached a middle point where most of the extracted images match the query text. 

Finally I reviewed the 14 groups of graphics selected in this initial version of the application and eliminated some of the erroneous images I found.

The final data set was not very large. During the pre-processing I tried the data augmentation, but the difference in quantity was not going to be very big. The solution for this is explained in the next section.

### ML approach

Although machine learning is essential for this project, as I explained in the motivations section, it was not the final goal.  Therefore I had to be careful with the development of it, to balance effort and result.

I decided to use Keras for this purpose. I have interest in other libraries but Keras was the one I used the most, this guaranteed familiarity with the process. 

Despite this, generating a good image multi-sorting engine is not an easy task. Even less having so many categories (with many possible options) and so little data for training. 

I decided as an intermediate solution to use a pre-trained network and perform transfer learning. That is, take a pre-trained neural network and add some final layers that classify according to my categories. 

To choose the neural network to use, I simply looked for the one that was giving better results and that was not a bestiality. I found MObilnet from Google and it was just what I was looking for: "Designed to effectively maximize accuracy while being mindful of the restricted resources for an on-device or embedded application. MobileNets are small, low-latency, low-power models parameterized to meet the resource constraints of a variety of use cases. They can be built upon for classification, detection, embeddings and segmentation similar to how other popular large scale models, such as Inception, are used".

The network weighed very little and I could retrain it very easily, to get good results with minimal effort.

#### NN architecture

You can check the neural net arcxhitecture [here](https://github.com/thebooort/The-Plot-Classifier/blob/master/images/model.png)

#### Results

![](https://github.com/thebooort/The-Plot-Classifier/blob/master/images/loss.png)
![](https://github.com/thebooort/The-Plot-Classifier/blob/master/images/accuracy.png)


#### Nets Trained

In this repo I have 3 `.h5` archives with weights for you to experiment with: 

- `keras_model.h5`: Trained with google services with no curated dataset (used at the very beginning)
- `per_trained.h5`: Trained with transfer learning, data augmentation, all images curated, and all images used(no validation).
- `per_trainedv2.h5`: Same of above, but with validation images.

### Streamlit dev

#### Screenshot

![ss1](https://github.com/thebooort/The-Plot-Classifier/blob/master/images/screenshot.jpg)

![ss2](https://github.com/thebooort/The-Plot-Classifier/blob/master/images/screenshot2.jpg)

### Heroku deployment 

construction



### TVestigios del primer readme por arreglar areas
- Descarga de imagenes
Para la descarga de imagenes estoy usando dos lineas de codigo desde la consola del navegador.
Pensé en generarlas yo mismo, pero no se a que nivel de variedad puedo llegar frente a las que puedo descargar desde -servicio online de imagenes nada conocido-.

```
	urls=Array.from(document.querySelectorAll('.rg_i')).map(el=> el.hasAttribute('data-src')?el.getAttribute('data-src'):el.getAttribute('data-iurl'));
```

Y despues descargo el archivo con las urls, para luego descargar las imagenes via script de python 

```
	window.open('data:text/csv;charset=utf-8,' + escape(urls.join('\n')));
```
