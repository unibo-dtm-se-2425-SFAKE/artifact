import sfake

# this is the main module of your app
# it is only required if your project must be runnable
# this is the script to be executed whenever some users writes `python -m sfake` on the command line, eg.
x = sfake.MyClass().my_method()
print(x)
