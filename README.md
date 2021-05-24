# CPMod 

## Summary
This tool was designed to stochastically calculate the summation of independent and dependent random variables. Although this tool can be applied to variety of problems it was initially designed to estimate consequence potentials of well designs in natural gas storage operations. This tool relies on Microsoft Excel to store inputs and Python to perform calculations. The design of the workflow is tailored for entry-level programmers yet flexible enough to model user defined complex systems. Users will spend most of their time in excel setting up distributions for the system. They will only need to transition to Python to run the script. Outputs include figure generation, however, future versions will include additional methods for interrogating data.

## Introduction and Purpose
This tool was designed to stochastically calculate the summation of independent and dependent random variables. Although this tool can be applied to variety of problems it was initially designed to estimate consequence potentials of well designs in natural gas storage operations. This tool relies on Microsoft Excel to store inputs and Python to perform calculations.

At its core, the computational element was designed to model various iterations of a system that relies on the summation of random variables. This is done by performing a simple Monte Carlo simulation and adding each outcome to generate a total. The process is repeated multiple times to generate a range of possible outcomes and is meant to inform the end user of expected ranges.

The design of the workflow is tailored for entry-level programmers yet flexible enough to model user defined complex systems. Users will spend most of their time in excel setting up distributions for the system. They will only need to transition to Python to run the script. Outputs include figure generation, however, future versions will include additional methods for interrogating data. 

## Code Workflow
### Design
The design of this model was meant to add the capabilities stated above while creating a familiar, yet streamlined, workflow. There are two main components of this workflow: 1) The Microsoft Excel Spreadsheet where users will spend most of their time defining inputs and 2) the Python code which is used to run a Monte Carlo simulation based on the inputs from Excel.

### Microsoft Excel
All of the defined variables are stored in Microsoft Excel. This is due to the availability and familiarity of Excel in the industry. There are no calculations performed in Excel, only storage of inputs and outputs. The workbook will have a single sheet for inputs and another for outputs. The input spreadsheet stores information that will be used to create distributions in Excel. There are several categories that are needed to define a distribution. 
