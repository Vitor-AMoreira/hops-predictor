# Hops-predictor

## Table of Contents
1. [Description](#Description)
2. [System Architecture](#System)
3. [Database](#Database)
4. [Model Trainning](#Model)
5. [Examples](#Examples)
6. [Dependencies](#dependencies)




## Description
The project focuses on developing an artificial intelligence (AI) tool for predicting hop aromas in beers. Currently, there are around 120 beer styles and 250 hop varieties, for this reasons, the vast array of beer styles and hop varieties available in the market, brewers and enthusiasts often seek ways to understand and anticipate the sensory experience provided by different hop choices.

By leveraging machine learning algorithms and data obtained from academic article references, this tool offers a practical solution to predict the sensory attributes of various hop varieties. It enables users to explore and identify the potential aromas associated with specific hops: The developed tool has the capability to predict 3 sensory attributes of 81 different hop varieties


## System Architecture


![System architecture schema](img/system-architecture.png)

This document provides an overview of the system architecture for the application, which is divided into three main components: **Database**, **API**, and **Web Application**. It outlines the high-level design and interactions between these components.

## Database
### Dataset
Like in almost all artificial intelligence models, data scarcity was one of the main challenges. Our data was collected from over 80 scientific articles, which provided some achievable predictions through certain parameters for populating our database. Almost all of this data is used for training our artificial intelligence, which will utilize the same data for future predictions.
### Diagram
![Database Diagram](img/databaseDiagram.png)

## Model Trainning

## Examples

## Dependencies
1. pandas
2. numpy
3. pickle
4. flask
5. sklearn

To be continued
