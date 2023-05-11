# NBI-Handelsakademin-ML-Labs
ML Labbar för NBI Handelsakademin. 

## image-lab
- Tänkt att köras direkt i Googel CoLab.
- Ett Kaggle-konto är nödvändigt för att ladda ner datasetet, finns instruktioner i relevanta notebooks.
- Går och köra lokalt i t.ex. VSCode om man modifierar paths som utgår ifrån CoLab.

Lokalt conda environment:
```bash
conda create -n nbi python=3.10
conda install -c conda-forge kaggle ipykernel
conda install -c conda-forge tensorflow keras opencv
conda install -c conda-forge matplotlib scikit-learn
``` 

