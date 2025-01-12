from py2ren import cli, create_config

path = "../py2ren"

cfg = create_config(path, level='-1')

args = cli.Args(path, "./generated",
                config=cfg, init_level=0)
cli.main(args)
