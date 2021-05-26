import rospy
from python_package_starter import main


if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass