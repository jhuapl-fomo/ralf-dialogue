# RALF

A general framework for building applications -- including conversational AIs -- that rely on a mix of prompted large language models (LLMs) and conventional Python code and services. This can be considered a powerful form of neuro-symbolic AI.

## Introduction

RALF itself is a kind of ecosystems of libraries and frameworks for doing useful things with large language models (LLMs). At its core is `ralf` proper -- the library that contains the primitives necessary for easily stringing together LLM-based "actions" into pipelines that can be used to process data in real-world applications. For even greater power and expressivity, `ralf` offers the `lang_graph` module, which contains control flow primitives along with an expanded implementation of "actions" that can be composed into declarative computational graphs.

Other frameworks, such as `ralf-dialogue`, build on the core `ralf` library, adding primatives and components for building conversational agents (or "chatbots") that can interact with users in natural language, leveraging context and accessing external knowledge stores or reasoning engines. Many of these components are still under active construction, and we're always looking for talented contributors.

## Getting started

Create a new Conda environment (or equivalent) containing Python 3.9 and switch to it:
```bash
conda create -n [ralf-env-name] python=3.9
conda activate [ralf-env-name]
```

`pip`-install the `requirements.txt` file:
```bash
pip install -r requirements.txt
```

Finally, build and install RALF:
```bash
flit build
pip install -e .
```

Now, to use, simply import the RALF module(s) you need at the top of your application; e.g.:
```python
from ralf import dispatcher
```


## Tutorial
The best way to get started with RALF is to do the tutorial. In it, you'll learn how to use the two most basic tools RALF offers -- the action dispatcher and the zero-shot classifier. If you're eager to get started and want to skip the tutorial, you might instead consider checking out the `dispatcher_demo.py` and `classifier_demo.py` files in the `demo/` directory.

### Setting up the configuration
[**TODO**: explain]

[**TODO**: models.yml]

[**TODO**: prompts.yml]

### Actions Pipelines and The Action Dispatcher
[**TODO**]

### Zero-shot Classifier
[**TODO**]

## Read the Docs
[**TODO**]

## Further Reading
[**TODO**]
