import sys



arguments=sys.argv[1:]

#print("The arguments are",arguments)
print("Choose your operation\n 1.Type installdir \n 2.Type app\n 3.recursive")
for i in arguments:
    match i:
        case [installdir, app]:
            print("installing")
        case ["-r",installdir,app]:
            recursive=True
        case _:
            print("Error message :")
            print("\t python install.py [-r] installdir app")
            sys.exit(0)
    print(f"Will install <{app}> in {installdir}> (recursive mode:{recursive})")


