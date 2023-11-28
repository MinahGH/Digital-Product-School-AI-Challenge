# Digital-Product-School-AI-Challenge

This repository implements a solution for the Digital Product School AI challenge. The goal is to predict number of accidents per month using AI.

## Dataset
Dataset is available at [this link](https://opendata.muenchen.de/dataset/monatszahlen-verkehrsunfaelle/resource/40094bd6-f82d-4979-949b-26c8dc00b9a7)
## Requirements
To install all the dependencies for the notebook run the following :

```
conda create -n env python=3.9
pip install -r requirements.txt
```

## Available Models

```
- 'DPS_adaboost_reg.pkl' : Trained AdaBoost Model 
- 'DPS_xgb_reg.pkl' : Trained XGBoost Model 
- 'scaler.pkl' :  StandardScaler to scale dataset

```

## Endpoint
The model is deployed at [link](https://dps-model-ekxrxrejtq-no.a.run.app).
You need to input a json like this with this POST method 
```javascript
{ "year": 2013,
"month": 3 }
```