from mymodule import my_func
from MyMainPackage import some_main_script
from MyMainPackage.SubPackage import my_sub_script

my_func()
some_main_script.main_report()
my_sub_script.sub_report()

if __name__ == "__main__":
    print("MyProgram Run Directly")
else:
    print("Imported")


