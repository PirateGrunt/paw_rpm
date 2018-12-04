# Python for Actuaries Workshop

## Session Description

A one day introduction to Python. The workshop will feed you some tasty cakes baked in Python and then give you the recipes. You will get ideas for new deserts you can bake in your own kitchen.

The session will not attempt to convert you to Python and does not claim its cakes couldn't be baked in R.

### Intended Audience

* You love programming and just want to learn about Python because it is a cool language. You will learn just how cool it is.
* You know R, have heard about Python and are curious what it is all about. You are unlikely to change religion. You will learn how to read Python code and how to converse with a Pythoner. You might also get a few ideas about how to improve your R code.
* You know you need to learn something beyond Excel/VBA and are trying to figure out what, so you are looking at Python. You will learn that were you are not an actuary you probably should learn Python. But, full disclosure: for actuaries we recommend you learn R because of its strong actuarial network.

### Prerequisites

You can already program in **some language** (R, VBA, ...; sorry HTML/CSS is **not** a programming language)

## Possible Mini-Projects

* Download a web page and list the common words in descending order of frequency (use wikipedia or sec.gov)
* Analysis of the CAS Loss Reserve Database
* Create a basic frequency / severity simulation model or work with simulation modeling output
* Find sentences common between two text files using exact matching and fuzzy matching

## Learning Objectives

After attending the session participants will:

* Be able to recognize Python code
* Be able to read Python code to get a general understanding of what it is doing (or how to find out if not obvious=access online help); recognize functions, classes, iterator constructions, lambda functions etc.
* Be able to explain the difference between pure Python language and imported libraries
* Be aware of, and appreciate, the Zen of Python
* Be aware of the functionality contained in basic built-in Python libraries such as os, sys, pathlib, re
* Be aware of the functionality contained in the common and relevant add-on libraries such as numpy, pandas, matplotlib, seaborn, scipy, scikit-learn, requests, bs4
* Be able to install Python (Anaconda or Canopy) and know what to ask for (Python 3.6+, Jupyter, JupyterLab)
* Be able to write basic Python code, including functions, flow control, use of iterators, basic string manipulation
* Be able to perform classic "Pythoneque" scripting such as downloading a web page and scraping out text content
* Be able to manipulate data with Pandas dataframes (discussed in the context of R dataframes)
* Be able to create basic graphical visualizations
* Be able to list some differences and similarities between R and Python
* Be able to explain that using either Python or R for data science is fine and that there is no clear **best** tool

## General Points

* We will use colab as the environment, which means folks only need a Google account and a web connection.
* **Will we have a web connection?**
* No software to install. Means using Jupyter rather than raw Python.
* If you have Jupyter installed on your own machine you can use it
* We will use Python 3.6 or later (**not 2.xx**)

## Draft Schedule (derived from schedule.md file)

| Item                     | Start |  End  | Duration   |
|:-------------------------|:-----:|:-----:|:-----------|
| Introductions            | 9:00  | 9:15  | 15 minutes |
| Environment, first steps | 9:15  | 9:45  | 30 minutes |
| Flow control, data types | 9:45  | 10:30 | 45 minutes |
| AM break                 | 10:30 | 10:45 | 15 minutes |
| Intro to numpy           | 10:45 | 11:30 | 45 minutes |
| Pandas                   | 11:30 | 12:30 | 45 minutes |
| Lunch                    | 12:30 | 1:30  | 60 minutes |
| Intro scikit-learn       | 1:30  | 2:30  | 60 minutes |
| Something else           | 2:30  | 3:30  | 60 minutes |
| PM break                 | 3:30  | 3:45  | 15 minutes |
| File system?             | 3:45  | 4:30  | 45 minutes |
| Wrap-up, Q&A             | 4:30  | 5:00  | 30 minutes |

## Intro to numpy (suggest less time)
* Arrays and array functions
* Broadcasting
* Roll your own data types
* Generally not as nice as you might hope...hence...

## Pandas (suggest more time)
* All of numpy plus more
* Creating dataframes
* Row and column indexes
* Concat
* Merging, pivot, stack and unstack
* query
* plot

## Cake-Oriented Draft Schedule

| Item                      | Start |  End  | Duration    | Cake Version                                       |
|:--------------------------|:-----:|:-----:|:------------|:---------------------------------------------------|
| Introductions             | 9:00  | 9:15  | 15 minutes  |                                                    |
| Environment, first steps  | 9:15  | 9:45  | 30 minutes  |                                                    |
| Flow control, data types  | 9:45  | 10:30 | 45 minutes  | Download webpage                                   |
| AM break                  | 10:30 | 10:45 | 15 minutes  |                                                    |
| Intro to pandas and numpy | 10:45 | 12:30 | 105 minutes | CAS Loss Reserve Database example                  |
| Lunch                     | 12:30 | 1:30  | 60 minutes  | ...obviously serving real cake                     |
| Intro scikit-learn        | 1:30  | 2:30  | 60 minutes  | Clustering and other using LRD                     |
| Simulation Modeling       | 2:30  | 3:30  | 60 minutes  | Reinsurance evaluation using Cat Model output      |
| PM break                  | 3:30  | 3:45  | 15 minutes  |                                                    |
| File system?              | 3:45  | 4:30  | 45 minutes  | by now don't need cake: JSON, fuzzy matching, APIs |
| Wrap-up, Q&A              | 4:30  | 5:00  | 30 minutes  |                                                    |

## Introductions
* BF, SM, JB
* The dreaded R vs. Python debate
	- Not here to convert you to Python
	- Not here to convince you one or other is "better"
	- Not here to compare and contrast every feature
	- Similarities
	- Differences: general purpose language vs. statistical
	- What Python is used for: SublimeText, Atom, Google, Spotify, websites
	- Who uses Python: #1 language in IEEE Spectrum survey
* What to expect

## Environment, first steps (getting to the cake store)
* Open colab notebook
* Hello world
* Variables
* Integer arithmetic (2**256)
* f'Hello {var}'
* Functions

## First Taste: Flow Control, Data Types
* Cake = function to download a webpage and find frequent words
* Illustrates leveraging existing Python libraries
* Apply to sec.gov (10Ks, search for risk, reinsurance...); conference call reports, wikipedia pages...
* Start with the function (it is only a few lines long); try on other pages; show how it works
* Strings and basic string functions, strings as arrays, slices and indexing
* Lists...lo all the slices work here too
* Dictionaries - the biggest miss of R IMO
* Tuples - don't worry too much about these
* Functions as data (should be familiar to R users)

## AM break

## Powerful Pandas: A Real Gateaux
* Cake = CAS Loss Reserve Database (LRD) analysis
* Read in CSV...produce some beautiful plots...and useful summaries...
* plot
* Arrays and array functions
* Accessing data: loc, iloc, slices, multi-indexes, filter
* Merging, pivot, stack and unstack
* query
* groupby, apply, map

## Lunch

## Intro scikit-learn
* Brian... could we do something to "learn" development patterns from the LRD?
* Cluster by development patterns using k-means

## More Pandas: Python Fast Enough for Simulation Modeling
* The Re-arrangement algorithm and maximum Value At Risk problem (https://ar.casact.org/the-re-arrangement-algorithm/)
* Iman-Conover by hand
* Evaluating reinsurance
* Plotting confidence ellipses and looking for evidence of extreme correlation

## PM break

## You Are Sick of Cake and Want Some Protein
* File system
* pathlib library and file manipulation and io
* file I/O open, unicode
* JSON - have to cover this!
* using a not-SQL database, e.g. MongoDB
* using an API, e.g. Twitter or Reddit?
* duplicate sentences and fuzzy matching example
* parsing xml/HTML with bs4, lxml
* writing your own library and using import

## Wrap-up, Q&A
