import io
import logging
import os
from contextlib import asynccontextmanager

from fastapi import FastAPI, UploadFile, File
import kaggle

DATA_PATH = os.getenv("DATA_PATH", "./datasets")

logger = logging.getLogger("uvicorn.error")

model = None  # Placeholder for the model, to be loaded later

def init_kaggle():
    kaggle.api.authenticate()

    if not os.path.exists(DATA_PATH):
        logger.info(f"Creating data directory at {DATA_PATH}...")
        os.makedirs(DATA_PATH)

    else:
        logger.info(f"Data directory {DATA_PATH} already exists.")

def download_dataset(dataset: str, dirname: str):
    if not os.path.exists(os.path.join(DATA_PATH, dirname)):
        logger.info(f"Downloading {dataset} dataset...")
        kaggle.api.dataset_download_files(dataset, path=DATA_PATH, unzip=True)

    else:
        logger.info(f"Dataset {dataset} already downloaded in {DATA_PATH}/{dirname}.")


@asynccontextmanager
async def lifespan(app: FastAPI):
    init_kaggle()
    download_dataset('hendrichscullen/vehide-dataset-automatic-vehicle-damage-detection', 'damage_detection')
    download_dataset('rickyyyyyyy/torchvision-stanford-cars', 'stanford_cars')
    yield
    logger.info("Application shutdown complete.")


app = FastAPI(lifespan=lifespan)


@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.post("/detect")
async def detect(file: UploadFile = File(...)):
    image_bytes = await file.read()
    boxes, labels, scores = model.predict_damage(io.BytesIO(image_bytes))

    return {
        "boxes": boxes,
        "labels": labels,
        "scores": scores
    }