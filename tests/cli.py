from py2ren import cli

path = "../py2ren"


args = cli.Args(path, "./generated/py2ren", init_level=0, analyze_dependencies=True)
cli.main(args)
