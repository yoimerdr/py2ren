from src.py2ren import cli

args = cli.Args("../src/py2ren", "./generated",
                force_config=True, init_level=-1)
cli.main(args)
