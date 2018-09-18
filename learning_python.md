# Issues Learning Python

Some notes on my experience learning Python.

## Background

I have programmed in several languages, C, C++, Matlab, SAS, VBA. When I started learning Python I had not programmed in R. I found Python quite intimidating and there were several (easy) things that confused me. We should consider incorporating some of these lessons into our plan.

## Issues and Confusions

1. Distinguish Python from core packages from commonly used packages from lesser used packages from quirky packages. For example, I'd categorize:

| Core    | Common     | Lesser        | Quirky |
|:--------|:-----------|:--------------|:-------|
| sys     | numpy      | beautifulsoup | vispy  |
| os      | matplotlib | requests      | base58 |
| re      | pandas     |               |        |
| hashlib | scipy      |               |        |
| etc.    |            |               |        |

2. Understand arguments and exactly what **kwargs means (and hence almost all Matplotlib documentation!)
3. Basics of attribtutes vs. items
4. Built in magic: dir(), .__dict__, just what are all those __functions__?
5. iPython/Jupyter/JupyterLab
6. Review the (relatively few) built in language commands. E.g. iter
7. f strings, worth the upgrade to 3.6
8. On which topic: 2.x vs. 3.x ==> 3.x
9. Unicode conniptions and (brilliant) 3.x support; UTF-8, open( with encoding)
10. Byte arrays vs. numbers vs. strings vs. hex (I really got into this when I was understanding Bitcoin)

## Items To Cover

My idiosyncratic list

* strings: built in string support in Python is absolutely fantastic
* regular expressions and hence to text manipulation
* Pandas: read_csv, read_excel, read_fwf, .plot, groupby(), agg, apply, applymap, map, pivot. Pandas is my Excel. Creating on-the-fly dataframes to display information in Jupyter.
* Seaborn with Pandas for easy plotting (Seaborn makes the routine easy, Matplotlib makes the hard possible)
* How probability distributions work in scipy.stat, which is very well thought out IMO (shape vs. scale and location parameters, uniform interface, frozen distributions)
* R like regressions, i.e. specify model as 'y ~ a + b + c'
* Web APIs and requests, web scraping, BS4, FRED data server
