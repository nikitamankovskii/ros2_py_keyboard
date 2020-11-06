import rclpy
import keyboard
from rclpy.node import Node
from geometry_msgs.msg import Twist


class MinimalPublisher(Node):

    def __init__(self):
        super().__init__('minimal_publisher')
        self.publisher_ = self.create_publisher(Twist, '/demo/cmd_demo', 10)
        timer_period = 0.5  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 0

    def timer_callback(self):
        msg = Twist()

        msg.linear.x = 0.0
        msg.linear.y = 0.0
        msg.linear.z = 0.0
        msg.angular.x = 0.0
        msg.angular.y = 0.0
        msg.angular.z = 0.0
        
        x_trig = False
        y_trig = False

        log = False
        if keyboard.is_pressed("l"):
            log = not log
         

        if keyboard.is_pressed("W"):
            x_trig = True
            msg.linear.x = 1.0
            print("UP")
        if keyboard.is_pressed("s"):
            x_trig = True
            msg.linear.x = -1.0
            print("down")
        if x_trig == False:
            # msg.linear.x = 0.0
            print("Nothing pressed x-axis")

        if keyboard.is_pressed("a"):
            y_trig = True
            msg.angular.z = 1.0
            print("UP")
        if keyboard.is_pressed("d"):
            y_trig = True
            msg.angular.z = -1.0
            print("down")
        if y_trig == False:
            # msg.angular.z = 0.0
            print("Nothing pressed  y-axis")
        

        if log:
            self.get_logger().info('Publishing: "%s"' % msg)
        
        self.publisher_.publish(msg)
        self.i += 1


def main(args=None):
    rclpy.init(args=args)

    minimal_publisher = MinimalPublisher()

    rclpy.spin(minimal_publisher)

    minimal_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()