def is_notebook() -> bool:
  """
  Tries to detect if cli.py is running in a notebook
  This will disallow using argparse
  """
  try:
    shell = get_ipython().__class__.__name__
    return True
  except NameError:
    return False

