from py2ren import cli

path = "../py2ren"


args = cli.Args(path, "./generated/py2ren",
                config="./py2ren.config.json", init_level=0)
cli.main(args)
