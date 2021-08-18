# Rihanna Estimator 

This web-app allows you to estimate the price of a diamond. Fill in the form and get the estimated price of your diamond. 

The predictive model (*DecisionTreeRegressor*) is based on several features : 
* **carat** : weight of the diamond *(0.2 to 5.01)*
* **cut** : quality of the cut *(Fair, Good, Very Good, Premium, Ideal)*
* **color** : diamond color *(J [worst] to D [best])*
* **clarity** : measurement of how clear the diamond is *(I1 [worst], SI2, SI1, VS2, VS1, VVS2, VVS1, IF [best])*
* **x** : length in mm *(0 to 10.74)*
* **y** : width in mm *(0 to 58.9)*
* **z** : depth in mm 	*(0 to 31.8)*
* **depth** : total depth percentage *(43 to 79)*
* **table** :width of top of diamond relative to widest point 

## Architecture

![](https://zupimages.net/up/21/33/cwvm.png)

* **api folder** : 
  - *fast.py* : main page of api using FastAPI and form controller
  - *fit_model.joblib* : holds the pretrained model for diamond price prediction
* **app folder** : contains front app
* **pkg_diamond** :
  * *get_data.py* : function to get data
  * *model.py* : Class to fit and save the model
  * *pipeline.py* : Class to get data ready for model
  * *preprocessing.py* : Class to clean data

## Demo

Click on the link to test the app or go to the next section to run it locally.

**Rihanna Estimator : https://rihanna.azurewebsites.net/**

  
## Screenshots

![](https://zupimages.net/up/21/33/stco.png)

  
## Run Locally

Clone the project

```bash
  git clone https://github.com/Galex33/api-dockers.git
  OR
  git clone git@github.com:Galex33/api-dockers.git
```
Go to the project directory 

```bash
  cd api-dockers
```

Install requirements (python 3.8)

```bash
  make install_requirements
```

Go to the api directory 

```bash
  cd api
```

Run FastAPI

```bash
uvicorn fast:app
```

App is running on  http://127.0.0.1:8000 

  
## Authors

- [Marie-Laure PETUAUD-LETANG](https://github.com/mlpetuaud)
- [@Galex33](https://github.com/Galex33)
- [@Asabuzz](https://github.com/Asabuzz)

  
## Contributing

The data from this project was taken from [Kaggle Data](https://www.kaggle.com/shivam2503/diamonds). 

Contributions are always welcome!

To create beautiful README : https://readme.so.
