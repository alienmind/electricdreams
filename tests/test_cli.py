from electricdreams.cli import cli


def test_cli():
    cli.main(interactive=False, prompt="Hello")
    # ... there's no actually a way to assert anything about this output, being an AI Chat...
    pass
