# FIND-S ALGORITHM

Developer  :Praahas Amin<br />
Contact:praahas@gmail.com<br />
Contact:praahas1234@gmail.com<br />
License: GPL<br />
Maintainer: Praahas Amin<br />
Credits: Tom M.Mitchell<br />
# Machine-Learning-Lab-VTU
Python Codes for the machine learning lab course of vtu 7th semester 

## DESCRIPTION
This algorithm is the first program in the Machine Learning Laboratory Course 15CSL76 under VTU.
The theory behind the algorithm is based on the description given by Tom M. Mitchell in his book titled "Machine Learning"
The algorithm used to find a Maximally Specific Hypothesis.
We start off with a Most Specific Hypothesis and based on the Training Examples, we end up with a Maximally Specific Hypothesis for the Target Concept.
The description for teh algorithm is given below.

## Algorithm:
Initialize h to the most specific hypothesis in H<br />
For each positive training instance x<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;For each attribute constraint a in h<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;If the constraint a is satisfied by x<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Then do nothing<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Else<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Replace a in h by the next more general constraint that is satisfied by x<br />
Output hypothesis h<br />

## INSTALLATION
Ensure that Python 3 is installed. The .csv file to be used with the python code should be located in the same folder as the python code.
According to the code, the csv file should be named enjoysport.csv. That may be changed by the developer and appropriate changes should
be done in the python code.
Pandas must be installed. This is because in the python code, Pandas is used to open and read the data from the .csv file.

## USAGE
Once python is installed and has been added to path, then python can be directly invoked from the command line interface.
(Users may also use Spyder,IDLE or any other IDE). Type "python finds.py" (without quotes"") this should execute the code.
and the output will be displayed on the screen. The output will show the Table, Hypotheses corresponding to Positive Training Examples,
Hypotheses corresponding to Negative Training Examples and the Maximally Specific Hypothesis for teh Target Concept.

## CREDITS
I am grateful to the author of "Machine Learning",Professor Tom M. Mitchell who has given a really simple explanation for the algorithm 
in his book which is the Text book for the Course.

