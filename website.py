from flask import Flask
import pandas as pd

df = pd.DataFrame(columns =['Name', 'Graduation', 'Residence', 'Major', 'Industry']
app = Flask(__name__)

@app.route("/")

def
