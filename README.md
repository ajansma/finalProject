## Taking Netflix by Storm
This project looks at the relationship between my Netflix watch history and the weather through a number of aggregation and exploratory data analysis techniques. In addition to this, 3 different machine learning classifiers were used on the weather data to try to predict the average viewing time. First, I compute a kNN classifier on the dataset. Using the temperature, precipitation, and category columns, the kNN classifier attempts to classify the Viewing Time category. The kNN classifier is compared to a Decision Tree and a Neural Network (MLP) classifier. The kNN classifier is tied with the Neural Network classifier as the best model for this dataset. However, those models are still not great. As this data is explored and analyzed, I found that there was not a significant relationship between the weather and the amount of viewing I did on a given day. This made it difficult to classify the results.

### Running the Project
This project was completed in a Jupyter Notebook with a .py file containing the utility code. To run this project, the repository can be cloned into Jupyter Lab, Jupyter Notebook, Google Collab, or VS Code. To do this you can copy the URL and use `git clone (URL HERE)` in the command line. Once the repository has been cloned, the Run all Cells button in Jupyter Lab can be used to run and render all of the cells in the Jupyter Notebook. 

### Layout
The project is organized in a fairly self-explanatory way with headers in the notebook to introduce each section. The Notebook begins with an Introduction that describes the project, my hypothesis, and a brief description of the results that I found. I then move into the Data Analysis section which describes the dataset, where it came from, and the attributes that I will be using. After this, I move into the Data Preparation section. In this section, the data is loaded into the pandas objects and then cleaned into a usable form. Once in a usable form, the Exploratory Data Analysis begins. A number of data aggregation techniques are used along with some visual representations of the dataset in order to better understand the dataset and the relationships it has. A few hypothesis tests are created in this section as well. Finally, the Classification portion can begin. In this portion, the Viewing Time column is the class attribute and I try to predict it using the weather columns. A number of different classifiers are attempted as mentioned above. Finally, the project draws its close with a Conclusion that summarizes the results, the data, and its implications.  

### Sources
I used a few different sources for this project, the first being the MeteoStat API for the weather data.
The documentation for this source can be found here: https://dev.meteostat.net/docs/

Secondly, I was not familiar with the Neural Network Classifier, also known as the MLP Classifier, I used the scikit learn website to learn more about this classifier works and how to use it in python.
Those sources can be found here:  https://scikit-learn.org/stable/modules/generated/sklearn.neural_network.MLPClassifier.html  
https://scikit-learn.org/stable/modules/neural_networks_supervised.html

