# PerplexityIPYNB

PerplexityIPYNB is a Python module that allows you to interact with the Perplexity AI.\
*New in 1.1: magic commands support for cell and row*\
*New in 1.1.1: fixed websocket problem*
## Installation

You can install PerplexityIPYNB using pip. Run the following command in your terminal:

```bash
pip install PerplexityIPYNB
```


## Usage
### Functional
```python
from PerplexityIPYNB import Perplexity

ai = Perplexity()
prompt = input()

print(ai.RUN(prompt))
```
### Magic commands
```python
%%perplexity
prompt
```
or 
```python
%perplexity prompt
```
