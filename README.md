# WhatWhale

---
## Conda virtual environment
[Conda documentation](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html)

### Create env
Create env with python 3.7 and pip
```bash
conda create --name whatwhale python=3.7 pip
```

Create env in specific location
```bash
conda create --prefix ./env python=3.7 pip
```

Create env from `environment.yml` file
```bash
conda env create -f environment.yml
```

### Activate env
Activate by name
```bash
conda activate whatwhale
```
Activate by location
```bash
conda activate ./env
```

After activating environment using its prefix, your prompt will look like this:
```bash
(/absolute/path/to/envs) $
```
You can fix this by modifying the `env_prompt` setting in your `.condarc` file:
```bash
conda config --set env_prompt '({name})'
```
Reactivate env and the prompt should show as:
```bash
(env) $
```

### Deactivate env
```bash
conda deactivate
```

### Viewing packages
List packages in active environment
```bash
conda list
```

List packages in environment using name
```bash
conda list --name whatwhale
```

### Install packages
Install flask in active environment
```bash
conda install flask
```

Install flask in environment using name
```bash
conda install --name whatwhale flask
```

### Using pip
It is recommended to only install packages with pip if `conda install` does not work.

Install pip into active environment
```bash
conda install pip
pip install <package-name>
```

### Sharing env as .yml
Export active environment to new file
```bash
conda env export > environment.yml
```

Export active environment, including only user-requested packages (supports cross-platform development)
```bash
conda env export --from-history > environment.yml
```

### Update env from .yml
Update contents of `environment.yml` file and run:
```bash
conda env update --prefix ./env --file environment.yml --prune
```

### Removing an environment
Remove environment by name
```bash
# remove env
conda env remove --name whatwhale
# verify
conda env list
```

