import rospy
from python_package_starter.sub_package.sub_package_code import bar_fn
# You can either run your code completely inside the script file, eg ExampleClass
# or you can import from a python module in the src folder, eg bar_fn()
class ExampleClass():
    def __init__(self):
        rospy.init_node("~", anonymous=True)
        print("Executing init for ExampleClass")
        self.message = "Executing function in ExampleClass"

        self.example_fn()


    def example_fn(self):
        print(self.message)
        

if __name__ == '__main__':
    try:
        ExampleClass()
        bar_fn()
    except rospy.ROSInterruptException:
        pass