#  Project Tweets Sentiment Analysis
<img src="https://github.com/ltadrummond/us-income/blob/main/visuals/us-dollar-bundles.jpg">

## Description

The aim of this project is to be able to analyse a sentiment of a tweet, being this positive or negative. To do so it's requeired to be able to do scrapping from tweets related to the famous netflix series Squida Game. Also it is needed to correclty clean and preprocess the tweets. Finally an sentiment analyser is deployed so anyone na analyse the sentiment on a desired tweet.

## Installation
* Python 3.8
* Trello

## Databases
The data was collected from twitter using a libary called twint. I was able to aquire around 11000 tweets.

## Packages used
* pandas
* numpy
* wordcloud
* streamlit
* nltk

# Usage
| File                        | Description                                                     |
|-----------------------------|-----------------------------------------------------------------|
| utils                   | Folder containing the python code. |
| deployment                    | Folder containing the needed files to deploy as well as python code related. |
| us_income_model_evaluation.ipynb              | jupyter notebook file containing Python code, using the random forest algorithm.|
| images            | Folder containing plots that are interesting and helped to bring insight as well as appealing pictures.  |


# Visuals

* Taking a look at how features correlate on the train set.
<img src="https://github.com/ltadrummond/us-income/blob/main/visuals/correlation_train_features.png">


# Model Validation


## Model Evaluation


# Conclusions

Overfitting can be avoided by:
- Validation techniques;
- Balanced data destribuiton over test and train;
- Bringing more data.
- Taking a good look at evalution metrics.

Model doesn't perform better only with high importance feautures. Actually repeting this porcess with even higher importance features could lead to overfittion, because of loss of data and train and test accuracy scores start to invert (higher on test then on train).

The classification report brings insight over other metrics. Such metrics are important because not all cases are to be predicted with the same "intention". In some situations it is preferable to have one metric higher then the other. If we are trying to predict hart failure problems, for example, it is important to have a high precison (if there are more false positives it is preferable).

The accuracy can be misleading. Sometimes it may be desirable to select a model with a lower accuracy because it has a greater predictive power on the problem.
For example, in a problem where there is a large class imbalance, a model can predict the value of the majority class for all predictions and achieve a high classification accuracy, the problem is that this model is not useful in the problem domain.
Accuracy works best if false positives and false negatives have similar cost. 


# Last words
Keeping all the feautures and performing hyperparameter tunning I manage to get a prediction with next values:
| precision                            |  Meaning                 |
|-----------------------------|-----------------------------------------------------------------|
| < 50k = 0.88              | for all the people that were are labeled as having wages under 50k, in reality 88% happen. |
| > 50k =  0.77                  | for all the people that were are labeled as having wages over 50k, in reality 77% happen. |

| recall                          |  Meaning                 |
|-----------------------------|-----------------------------------------------------------------|
| < 50k = 0.95               | for all the people that were are labeled as having wages under 50k, the model guesses 95% correctly. |
| > 50k =  0.59                | for all the people that were are labeled as having wages over 50k, the model guesses 59% correctly. |

| f1-score                        |  Meaning                 |
|-----------------------------|-----------------------------------------------------------------|
| < 50k = 0.91                 | F1 is usually more useful than accuracy, especially if you have an uneven class distribution.  |
| > 50k =  0.67                | F1 is usually more useful than accuracy, especially if you have an uneven class distribution. |

Accuracy works best if false positives and false negatives have similar cost. So for this situation we should consider the F1-Score.


# Contributors
| Name                  | Github                                 |
|-----------------------|----------------------------------------|
|Leonor Drummonnd      | https://github.com/ltadrummond              |




# Timeline
11/10/2021 - 14/10/2021
