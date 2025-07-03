# Transitioning from OneTick to KX products: A Series of Use Cases

While migrating tick data from OneTick to kdb+, one of the more straightforward aspects is handling raw trade and quote
data. This is because such data can often be re-sourced from market data providers. Therefore, the main focus during
migration lies in rethinking the architecture of the data analytics platform itself.

By shifting from OneTick Query Language to the q programming language, teams can take full advantage of kdb+’s
performance and expressiveness, among other powerful features. This transition also enables seamless integration with
existing Python-based analytics platforms through PyKX, resulting in a more flexible and scalable architecture.

**Environment Setup**

Create Virtual Environment: `python -m venv .venv`

Activate Virtual Environment: `source .venv/bin/activate`

Install Libraries: `pip install requests pykx matplotlib seaborn`  