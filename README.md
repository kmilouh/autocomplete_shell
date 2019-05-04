# Readme.


## Install.

- You must have install npm & node [install](http://nodejs.org)
  
- Open a terminal and install angular : `npm install -g @angular/cli`

- Change the file `app\src\app\app.component.ts` and  put your name and email in the lines 19 and 21.

- Open a terminal in the folder `app\` and run the command : `npm install`

- Then you must type in the terminal: `npm run prod`
  This build the angular app.

- You must install the python package from requirements.txt typing  `pip install -r requirements.txt`


## File main.py

In the line 22 you have a list of model class that define your autocomplete model. You can have more that one model defined. You can define models from multiple language, multiple corpus etc. Here you MUST change this and add your models.

The model class must have the function `def predict(self, words, top=1)`. This function must receive as parameter a list of words and the number return words. This function must return a tuple of the words sorted by relevance.

In the line 30 you have a list for the description of your autocomplete models.

You can load your trained models. Is better that you use a trained model here for better performance(you can use  [pickle](https://docs.python.org/3/library/pickle.html) )

The webapi is serve using `bottle` and contains four endpoints.

- `/` : serve the `index.html`
- `/<filename:path>` : serve the js, css files used by the angular app.
- `/models`: return a JSON with the description of your autocomplete models.
- `/complete/<modelbase>/<length>/<words>` : this request is the main endpoint. The `modelbase` is the model number in the list models, `length` is the size of the response word list and `words` is the list of the words typed in the frontend app.


The number of the modelbase use to retrieve the auto complete word list is set in the frontend angular app and also the number of words to retrieve.

After change the angular app, change the python files, added your models etc. you can execute the app typing in a terminal `python main.py`

Any questions write to [kmilouh@gmail.com](mailto:kmilouh@gmail.com) 

