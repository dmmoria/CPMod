# CPMod (Consequence Potential Model in Python)

## Introduction and Purpose
This tool was designed to stochastically calculate the summation of independent and dependent random variables. Although this tool can be applied to variety of problems it was initially designed to estimate consequence potentials of well designs in natural gas storage operations. This tool relies on Microsoft Excel to store inputs and Python to perform calculations.

At its core, the computational element was designed to model various iterations of a system that relies on the summation of random variables. This is done by performing a simple Monte Carlo simulation and adding each outcome to generate a total. The process is repeated multiple times to generate a range of possible outcomes and is meant to inform the end user of expected ranges.

The design of the workflow is tailored for entry-level programmers yet flexible enough to model user defined complex systems. Users will spend most of their time in excel setting up distributions for the system. They will only need to transition to Python to run the script. Outputs include figure generation, however, future versions will include additional methods for interrogating data. 

## Design
The design of this model was meant to add the capabilities stated above while creating a familiar, yet streamlined, workflow. There are two main components of this workflow: 1) The Microsoft Excel Spreadsheet where users will spend most of their time defining inputs and 2) the Python code which is used to run a Monte Carlo simulation based on the inputs from Excel.

### Microsoft Excel
All of the defined variables are stored in Microsoft Excel. This is due to the availability and familiarity of Excel in the industry. There are no calculations performed in Excel, only storage of inputs and outputs. The workbook will have a single sheet for inputs and another for outputs. The input spreadsheet stores information that will be used to create distributions in Excel. There are several categories that are needed to define a distribution. 

**consqeuence_name** - This category represents the name of the consequence potential. It can be any type of alphanumerical name including spaces. This quality is currently used for bookkeeping only.

**category** - This is a category the given consequence falls into. It is used to group consequence potentials together in the output visuals. Any alphanumeric name (including spaces) can be used. For example, the JITC model uses four categories: surface safety, subsurface safety, environmental, and service reliability.
 
 **dependence** - This parameter will be covered in detail later, but essentially it allows the user to create a dependence between variables. For example, if one dependent variable is high, then all the other dependent variables will be high (or vice versa).

**dist_type** - This parameter is used to define the type of distribution for a given consequence potential.

**distribution_parameters** - This set of parameters is used to define the distribution defined in the dist_type column.

Information from the Excel Spreadsheet is then imported to Python for calculations.

***Note:*** *Names of column headers can be changed but those changes must be reflected in the Python parameter file.*

***Note:*** *Input filetype can be changed to fit the user's need (i.e. CSV or similar file) but slight changes to the tool files will need to be made.*

### Python
Python is used to import all the input parameters, perform all calculations, plot results, and write inputs. The code was designed to be used with little to no programming experience. Any changes to the code will require some knowledge of programming.

**cp_main.py** - This is the main file that will users will work with. There are several user defined inputs that determine the number of scenarios used in the Monte Carlo simulations (more runs = more compute time/resources needed) and the outputs.

**cp_param.py** - Used for housing the parameter name information (i.e. the names of the columns in the excel worksheet). Users will need to modify this file if any of the column headers are changed in the Excel Spreadsheet.

**cp_calcs.py** - Location of all the functions needed for performing the Monte Carlo simulation. This includes parsing the data, separating the data into dependent and independent groups, random sampling for Monte Carlo simulation, and summing all consequence potentials.

**cp_tools.py** File that contains global functions not specifically associated with the Monte Carlo simulation functions found in cp_calcs.py

**cp_plot.py** Functions used to plot results.

***Note:*** *It is possible to add additional distributions to use in the Monte Carlo Simulation. Users with programming knowledge would need to modify the cp_param.py and cp_calcs.py files.*

## Code Workflow
Users will need to download a Python 3.8 or newer distribution. The scripts also rely on Pandas, SciPy and NumPy. All of these can be installed individually or by using an Anaconda Python distribution.

Users will also need all the files in the CPMod distribution to the same directory (as the Python script looks for an Excel spreadsheet in the same directory).

Once user download the files, they can test the code by running the cp_main.py script. This should automatically run through the code using the sample parameters in the example Excel spreadsheet. Assuming the user gets outputs they are free to manipulate the inputs in the spreadsheet to match their system. If the user wishes to change the spreadsheet name, they will need to change the definitions in the cp_param.py file to reflect the correct filename.
