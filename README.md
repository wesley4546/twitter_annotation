# Twitter Annotations

## Introduction 

The purpose of this program is so that anyone can rapidly go through a list of twitter user URLs and answer questions about them; in other words a very simple data-entry program.

If you stop in the middle, it does have a mechanism that will roughly save your progress (As long as you enter things in correctly).

## Tutorial

It's relativley simple to setup but it is important to have specific things:

### Step 1

  * Your `input.csv` must contain the following 2 columns:
    * `ScreenName` which is the twitter username (The @ one)
    * `URL` the URL to the user
    

For Example:

![Example of Column naming in Input CSV](tutorial/example_input_csv_column_names.PNG)

### Step 2

Make sure that in you `main.py` that you have the correct file names for both:
 * `input_file_name`
 
 * ` output_file_name`
 
For Example:
![Example of variable naming for the files](tutorial/example_file_variable_naming.PNG)

