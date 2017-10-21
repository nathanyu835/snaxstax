# Setup and Installation

Create a new virtualenv and source it
```
virtualenv .ENV && source .ENV/bin/activate
```

then install the packages
```
pip install -r requirements.txt
```

# Running the server
```
export FLASK_APP=app.py
export FLASK_DEBUG=1
python -m flask run
```

Then load <http://localhost:5000/>

# Code Layout

## Server
* `app.py` API route for autocomplete

## Client
* `static/index.html` HTML loaded at root URL
* `static/script.js` Javascript file loaded by index.html
* `static/styles.css` CSS file loaded by index.html
