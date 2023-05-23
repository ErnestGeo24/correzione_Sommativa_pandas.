from flask import Flask, render_template, request
app = Flask(__name__)

import pandas as pd 
import os 
import matplotlib.pyplot as plt



aree = pd.read_csv('https://raw.githubusercontent.com/ErnestGeo24/correzione_Sommativa_pandas./main/ds600_aree-del-territorio-del-comune-di-milano-dove-sono_c6at-33q9_final.csv', sep = ';')



@app.route('/')
def home():
   

    return render_template("home.html")

@app.route('/esercizio1', methods = ["GET"])
def esercizio():
   
    areagb = aree.groupby('MUNICIPIO').count().reset_index()[['MUNICIPIO','NIL']].sort_values(by='NIL',ascending = False)
    ascisse = areagb['MUNICIPIO'].map(str)
    ordinate = areagb['NIL']


    fig, ax = plt.subplots(figsize=(20,15))
    ax.bar(ascisse, ordinate, label='AREE PER MUNICIPI',color = ["red", "blue", "green", "yellow", "black"])
    ax.set_title('Titolo')
    ax.set_xlabel('Municipio')
    ax.set_ylabel('Aree')
    ax.legend()
        
    dir = "static/images"
    file_name = "es1.png"
    save_path = os.path.join(dir, file_name)
    plt.savefig(save_path, dpi = 150)
    return render_template("esercizio1.html")



if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3246, debug=True)