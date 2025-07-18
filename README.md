# Vehicle Damage Detection — Setup Guide

This app uses FastAPI + Torchvision on the backend and Vue.js on the frontend to detect vehicle damage from images.
The backend leverages pre-trained models and public datasets to identify damage like dents, scratches, and more.

## Prerequisites

  - Docker & docker-compose to run the app loaclly
  - [Kaggle](https://www.kaggle.com/) account for datasets

## 1. Set Up Kaggle API Access

- Go to your [Kaggle Account Settings](https://www.kaggle.com/settings).
- Click "Create New API Token" — this downloads `kaggle.json`.
- Move the file to the default path for your OS:

      # (PowerShell)
      mkdir $env:USERPROFILE\.kaggle
      move .\kaggle.json $env:USERPROFILE\.kaggle\

      # (Bash)
      mkdir ~/.kaggle
      mv .\kaggle.json ~/.kaggle

## 2. Download datasets

  I'll probably automate this with a `docker-compose run download` command later.

    cd ./backend
    mkdir datasets

    # Download datasets
    kaggle datasets download -d hendrichscullen/vehide-dataset-automatic-vehicle-damage-detection
    kaggle datasets download -d hamzamanssor/car-damage-assessment
    kaggle datasets download -d rickyyyyyyy/torchvision-stanford-cars

    # (PowerShell) Extract into folders
    Expand-Archive vehide-dataset-automatic-vehicle-damage-detection.zip -DestinationPath datasets/VehiDE
    Expand-Archive car-damage-assessment.zip -DestinationPath datasets/CarDamage
    Expand-Archive torchvision-stanford-cars.zip -DestinationPath datasets/StanfordCars

    # (Bash) Extract into folders
    unzip vehide-dataset-automatic-vehicle-damage-detection.zip -d datasets/VehiDE
    unzip car-damage-assessment.zip -d datasets/CarDamage
    unzip torchvision-stanford-cars.zip -d datasets/StanfordCars

After extraction you can remove the zip files.

## 3. Train the Models

    docker-compose run train

## 4. Validate the Models

    docker-compose run validate

## 5. Build & Run the container

    docker-compose build
    docker-compose up

Backend (FastAPI) is accessible on http://localhost:8000 (OpenAPI docs on http://localhost:8000/docs).

Frontend (Vue.js) is accessible on http://localhost:3000.

