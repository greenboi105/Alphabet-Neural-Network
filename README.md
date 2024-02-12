# Alphabet Soup

The nonprofit foundation Alphabet Soup wants a tool that can help select the applicants for funding with the best chance of success in their ventures.

We want to use the features in the provided dataset to create a binary classifier that can predict whether applicants will be successful if funded by Alphabet Soup.

## Step 1: Preprocess the Data

Using pandas and scikit-learn, we need to preprocess the data for the later stage where we compile, train and evaluate the neural network model.

## Step 2: Compile, Train and Evaluate a Model

We design a neural network, or deep learning model, to create a binary classification model that can predict if an Alphabet Soup-funded organization will be successful based on the features in the dataset.

## Step 3: Optimize the Model

Using knowledge of TensorFlow, optimize the model to achieve a target predictive accuracy high than 75%.

## Step 4: Write a Report on the Neural Network Model

1. Overview of the analysis: Explain the purpose of the analysis.

    - The purpose of the analysis and the neural network model is to utilize the features (columns) in the dataset that are not `IS_SUCCESSFUL` to predict the outcome of that particular column.

2. Result - Using bulleted lists and images to support the answers, address the questions:

    - Data Preprocessing

        - What variables are the targets for you model?

            - `IS_SUCCESSFUL` is the target for the model.

        - What variables are the features for your model?

            - Features for the model are the traits for a given application, such as the `INCOME_AMT` or the `ASK_AMT`.

        - What variables should be removed from the input data because they are neither targets not features?

            - The variables that should be removed are the identifying aspects for a given application, such as the ID number and the name of the organization.

    - Compiling, Training, and Evaluating the Model

        - How many neurons, layers, and activation functions did you select for your neural network model, and why?

            - The number of neurons should match the number of input features after preprocessing. For the initial setup, we should begin with one or two hidden layers. A common approach is to use a number of neurons in between the size of the input layer and the output layer. For the output layer, we should have a single neuron and use a sigmoid activation function since it produces a value either 0 or 1, representing whether the task is successful or not.

        - Were you able to achieve the target model performance?

            - No, the model did not reach the threshold of 0.75.

        - What steps did you take in your attempts to increase model performance?

            - I attempted to add more layers and neurons, along with experimenting with the type of activation function. It is likely the case that some more sophisticated methods will be needed such as searching for optimal hyperparameters.

3. Summary: Summarize the overall results of the deep learning model. Include a recommendation for how a different model could solve the classification problem, and explain your recommendation.

    - It would also be possible to use conventional machine learning methods instead of deep learning, which could possibly suit this task better.
