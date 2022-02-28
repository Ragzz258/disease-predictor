
Preparation of the data in a suitable format:

we convert the given data set to a new suitable format which has 
row names as diseases and columns as all the symptoms and we give 1 if
the symptom is present in that disease else we give 0


Training a decision tree:

using train_test_split function we split trainning data and testing data
then using DecisionTreeClassifier function and setting criterion = "entropy" and
then we fit our data into the desiciontree i.e we are training our model here.

we use predict function and predict the disease from symptoms compare it with actual disease
and calculate accuracy score.

then plot the tree using plot_tree function.

finally we use pickle.dump functom to store our decisiontree model in a seperate file
which will be used in our webapp.


Web app: 

first we load our pickle file with pickle.load

we make user select their symptoms from the list we created
then predict the disease accordingly from our decision tree

to show our predicted disease, its description and precautions
we use put_html from pywebio and use style for adding color, setting font size, etc...

then we make a return button to go back and enter symptoms instead of running the code everytime,
href to previous symptom page and again we use style to make the button

after running the code we get the webapp adress which leads us to the webapp





