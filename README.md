# electricdreams

[![Release](https://img.shields.io/github/v/release/alienmind/electricdreams)](https://img.shields.io/github/v/release/alienmind/electricdreams)
[![Build status](https://img.shields.io/github/workflow/status/fpgmaas/electricdreams/Main/main)](https://github.com/fpgmaas/electricdreams/actions/workflows/main.yml?query=branch%3Amain)
[![codecov](https://codecov.io/gh/alienmind/electricdreams/branch/main/graph/badge.svg)](https://codecov.io/gh/alienmind/electricdreams)
[![Commit activity](https://img.shields.io/github/commit-activity/m/alienmind/electricdreams)](https://img.shields.io/github/commit-activity/m/alienmind/electricdreams)
[![License](https://img.shields.io/github/license/alienmind/electricdreams)](https://img.shields.io/github/license/alienmind/electricdreams)

![image info](./img/default.jpg)

Helper module and demo CLI to interact with ChatGPT and Stable Diffusion. Just for DIY small projects.

Current features:
- Running queries against GPT from the command line
- Exposing an API for text and image generation based on prompts
- Demo: Generating an original text adventure - both from the command line or a notebook

This is pre-alpha. Expect bugs. Test coverage is zero.

- **Github repository**: <https://github.com/alienmind/electricdreams/>
- **Documentation** <https://alienmind.github.io/electricdreams/>

## Installation
You need to alocate your own API keys (OPENAI / Stable Diffusion) and put them under ~/.config/electricdreams/electric.env
See config/electric.env.template for an example

## Running from a Notebook in Google Colab
One possible setup is to expose an API in Google Colab, taking advantage of the GPU for image generation.
There are examples for this under notebooks/electricdreams-jupyter-colab.ipynb

## Running from the terminal
Another option is to run entirely in the terminal, but for now it will rely on a local GPU

## API
Check http://localhost:8000 for a swagger

## Building and local testing
This project uses poetry for dependency management, building and testing.
Poetry can be installed with:

```bash
curl -sSL https://install.python-poetry.org | python3 -
```

Some commands:
```bash
poetry run electricdreams-cli         # Query from the command line (-h for help)
poetry run electricdreams-adventure   # Run a text adventure
poetry run electricdreams-api         # Expose an API - WIP
```

### TODO
Create a web app that interacts with the API to create an adventure

---

Repository initiated with [fpgmaas/cookiecutter-poetry](https://github.com/fpgmaas/cookiecutter-poetry).