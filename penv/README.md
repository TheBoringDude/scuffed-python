# sppenv
Simplified Python `.env` file parser.

## Install
```bash
pip3 install sppenv
```

## Usage
- `.env` - This should be in the project root directory
```
HELLO=WORLD
```

- `sample.py`
```python3
import os
from sppenv import load_env

# run the loader
load_env()

# environment variables from .env are now accessible...
print(os.getenv("HELLO")) # it will print "WORLD"
```