# Covid Data Tools

Codato ("COvid DAta TOols") is an machine learning framework integrating a number of different data science applications, packaged as lightweight, autonomous, pluggable apps. Although this framework is dedicated to analyzing Covid-19, it could easily be applied to any epidemiological study. (Indeed, given a bit more time, we'd like to run it for historical outbreaks of which we already know the outcomes.) Moreover the models are fully swappable, so datasets need not be limited to the epidemiological.

It's data driven, not hard coded, and the toolset itself is domain agnostic, so it could easily be used with any time series data influenced by environmental factors. Models can be written either in C (as the SEIR model here is) or Python (as the NLP model is, although it's also Cythonised.) Obviously, there's a pretty big performance difference.


# Table of contents

  * [Overview](#overview)
  * [Build](#build)
  * [Install](#install)
  * [Deploy](#deploy)
     * [K8s](#k8s)
     * [Docker](#docker)
     * [Metal](#metal)
  * [Run](#run)
  * [Features](#modules)
     * [Api](#api)  
     * [Ask](#ask)  
     * [Data](#data)  
     * [Explore](#explore)  
     * [Features](#feature)  
     * [Model](#model)  
     * [Predict](#predict)  
     * [Simulation](#simulation)  
  * [SEIR+ Modeling](#seir)     
  * [Web Server](#webserver)
       * [Low Latency Backend](#low-latency)
       * [Custom Themes](#custom-themes)    
  * [Examples](#examples)
     * [Conversational Inquiry](#conversational-inquiry)
     * [Model Tuning](#models)
     * [Running Simulation](#simulation)
  * [Release Notes](#releasenotes)        
  * [Contributing](#contributing)
         * [Feedback](#feedback)    
  * [Resources](#license)
  * [Live Demo](#demo)
  * [License](#resources)  
  * [In Gratitude](#thx)


## BUILD

Codato models, such as the SEIR epidemiological model, the NLP model used for question answering (“unendlich-verstehen”), curve fitting and other are written in C/ython, so they need to be compiled for your architecture.

Codata is designed to be fault tolerant for missing [apps](#features). So you should be able to run it without building anything, and everything else should just work. Test coverage on this is, shall we say, less than complete.

## INSTALL

### Installation and Setup

* Dependencies
      * Codato is is a framework, not a library. As such, all dependencies are managed in the environment.

* Installation steps (once you have built)

      * create env / source env file
      * run installer

`environment.yml` should have everything you need to get started. If you’re not using Conda, I feel bad for you son, I got 99 problems but dependencies ain’t one. Note there are 2 environment files shipped, production and development. NB. the production env currently still uses the built in server.

Answer a couple questions and it's off to the races:

```
./install.sh
```

## DEPLOY

Codato is deployable via Kubernetes, plain old Docker or close to the metal if you prefer to go containerless (a bit like streaking through a data center, I’d say.)

### Kubernetes

Helm charts are located in: ```/charts```
At some point will probably move all 3 deploy methods into ```deploy``` directory.

### Docker

```
docker compsse up
```
if you have root. If you don’t have root, you go hungry, I guess. Maybe find somone who does.

### Metal

Just run the innstaller.

```
\m/
```

## RUN

Now you can run `codato server start` from the command line, or invoke start.sh directly, which is totally self-contained for running on bare naked metal:

```./start.sh
```

### SERVER

To start the front end, run the following command. Yes, it's a server, that's what the app talks to. It's all back to front. (Literaly.)

```
run webserver
```

This is essentially the equivalent of invoking:

```python run.py
```

Since the API is served with flask, you _should_ be able to start the application server with ```flask run``` which will first look for ``app.py`` and not finding it, will attempt to execute `run.py`

* [Low Latency Backend](#low-latency)

* [Custom Themes](#custom-themes)   

Simply pass the theme name to ```codato webserver``` such as:
```codato webserver --theme=pride``` (rainbow pride)
```codato webserver --theme=blm``` (dark mode)
```codato webserver --defalt``` (default theme)

### Standalone Modules
Run Predict as stantalone module: (ie not using python -m)

```python -m apps.predict
```
A number of flags are supported on start up:
```
* -D load default settings
* -d date range to display
* -h display help page
-m model to be used
* -t select traning period
-v display version info
```

## MODULES
(_aka_ FEATURES _or_ APPS)

Not to be confused with features of a model, Codato platform feature are standalone, *pluggable* modules (aka apps) which define a reactive front end and the callbacks it requires, and are automatically added simply by dropping them in the ```apps```  directory. Currently its callback needs to be maually registered in server.py, but this will be autodetected as well, allowing apps to easily be added and/or swapped out unidrectionally. Martin Fowloer is smiling his happy smile.

Codato includes the following apps by default: (move app to "inactitive" folder to remove.)

### API

This is not an app per se but is the underlying interface all apps implement. Documentation generated using Open API using either redoc or Swagger.

      * API first platform
      * Ref Doc via redoc
      * How to add a new API endpoint?

### Ask

      * Front End Conversational Interface
      * Natural language queries over any dataset

### Data

      * Add dataset via upload or URL
      * Browse data tables
      * Edit data in browser
      * Save or downloaded updated dataset

### Explore

      * Visually explore datasets to identify salient features
      * Feature distance comparator

### Features

      * Add features to your model
      * Fit using fractal gradient reduction

### Model

      * Run model over any available dataset
      * Adjust parameters in real time

### Simulation

      * Match model parameters to real-world data
      * Validated output fed into Remodell

### Validation

      * Time-series cross-validation
      * Hyperparameter tuning

      Since k-fold Cross Validation doesn't work for time series data., the framework includes custom time-series cross-valisation (TX) that avoids "rolling" the data.

### World

      * Visual explorer of real world Covid data

## SIMULATION

### SEIR Model overview and caveats:
* Fixed population constraint in SEIR modeling.
* Standard SEIR models is they assume infection period is equivalent for both those who recover and those who do not.  This is only an assumption.
* Implicit assumption that infectiou period is equivalent to the contagion period, which doesn't allow for for latency in sympton onset. _(Since it's classically defined as delay in symptom onset from exposure. But in the case of CoronaVirus, patients cold be infectious for days or even weeks before they become symptomatic- if they become symptomatic at all.)_

### SEIR+ Model

The limiatations of the standard SEIR model have been addressed, with additional considerations:

* Recovered ("Removed" in SIR mode) split into recovered, and not-recovered.

## CONTRIBUTE

   * We welcome contributions!
   * Front End & Designers esp!
   * Send that Pull Request!

## Release Notes

### Known issues

* Kind of a lot right now, it's literally version 0.1

And no, there's NO animated race chart, there’s enough of those on the Internet. But the point is how trivial it is to add one here by implementing a module that exposes 2 interfaces: ```layout```, which is a list of html elements and reactive components of at least length 1, and ```callbacks``` which defines a return function for a reactive binding. That's it.

### Github issue queue

[Tell us](https://github.com/ForestMars/Coda.to/issues) one we haven't thought of!

## Resources

* [Unconditional Mean, Volatility, and the FOURIER-GARCH Representation](https://link.springer.com/chapter/10.1057/9780230295209_5)
* [Fractional and Fractal Formulations of Gradient Linear and Nonlinear Elasticity](https://arxiv.org/abs/1808.04452)

## Demo

A live demo of this projec it running at [Coda.to](http://coda.to).

## License

Codato is released under either the MIT or the GPL license, depending who you ask. Please [contact us](mailto:legal@coda.to) for clarification.

## Gratitude

You know who you are.


## Dragons

<div align="center"> ABOUT | TEAM | CONTACT </div>

**About:** It's less about optics or end users, more about collaborative tools.

**Team:** We are a group of research scientists and data engineers based mainly in New York, but collaborating over Zoom (actually, Slack)

**Contact:** [Email](mailto:coronapacalypsenow@gmail.com) suits us best.
