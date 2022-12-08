# electricdreams

[![Release](https://img.shields.io/github/v/release/alienmind/electricdreams)](https://img.shields.io/github/v/release/alienmind/electricdreams)
[![Build status](https://img.shields.io/github/workflow/status/fpgmaas/electricdreams/Main/main)](https://github.com/fpgmaas/electricdreams/actions/workflows/main.yml?query=branch%3Amain)
[![codecov](https://codecov.io/gh/alienmind/electricdreams/branch/main/graph/badge.svg)](https://codecov.io/gh/alienmind/electricdreams)
[![Commit activity](https://img.shields.io/github/commit-activity/m/alienmind/electricdreams)](https://img.shields.io/github/commit-activity/m/alienmind/electricdreams)
[![License](https://img.shields.io/github/license/alienmind/electricdreams)](https://img.shields.io/github/license/alienmind/electricdreams)

Helper module to interact with ChatGPT and Stable Diffusion. Just for DIY small projects.

Current features:
- Exposing StableDiffusion via API for image generation based on a prompt.
- Generating a 100% original text adventure in CLI (without images) - based in OpenAI
- Running a text adventure in a notebook (with contextual images)

You need to alocate your own API keys and put them under ~/.config/electricdreams/electric.env
See config/electric.env.template for an example

This is pre-alpha. Expect bugs. Test coverage is zero.

- **Github repository**: <https://github.com/alienmind/electricdreams/>
- **Documentation** <https://alienmind.github.io/electricdreams/>

## Building and local testing

This project uses poetry for dependency management, building and testing.
Poetry can be installed with:

```bash
curl -sSL https://install.python-poetry.org | python3 -
```

Some commands:
```bash
poetry run electricdreams-cli   # Run a text adventure from the command line
poetry run electricdreams-api   # Expose an API
```

## Running from a Notebook in Google Colab
One possible setup is to expose an API in Google Colab, taking advantage of the GPU for image generation.
There are examples for this under notebooks/electricdreams-jupyter-colab.ipynb

## Running from the terminal
Another option is to run entirely in the terminal, but for now it will rely on a local GPU

## TODO
A web frontend is WIP and will allow decoupling both
---

Repository initiated with [fpgmaas/cookiecutter-poetry](https://github.com/fpgmaas/cookiecutter-poetry).