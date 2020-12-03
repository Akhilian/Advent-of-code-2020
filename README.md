# Advent-of-code-2020

[![Build Status](https://travis-ci.org/Akhilian/Advent-of-code-2020.svg?branch=main)](https://travis-ci.org/Akhilian/Advent-of-code-2020)

## I have learned

Before 3.7, you cant refer to the self.class definition.
You have to wrap the class name with single quotes.
```
class Policy(object):
    def __enter__(self) -> 'Policy':
        pass
```

This is fixed in python 3.7
```
from __future__ import annotations

class Policy(object):
    def __enter__(self) -> Policy:
        pass
```
