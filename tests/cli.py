import src as py2ren

args = py2ren.cli.Args("../src", "./generated",
                       force_config=True, name="py2ren", init_level=-1)
py2ren.cli.main(args)
