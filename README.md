# ragu

## Setup

### Prerequisites
- Python 3
- Pip

### Steps
1. Set up a virtual environment `python3 -m venv env`.
2. Activate the venv `source env/bin/activate`.
3. Install requirements `pip install -r requirements.txt`.
4. Install pre-commit `pre-commit install`

#### Flake8
1. Install git hook `flake8 --install-hook git`.
2. Prevent git from committing on flake8 failures `git config --bool flake8.strict true`.
