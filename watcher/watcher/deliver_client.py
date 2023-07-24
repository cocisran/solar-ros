import sys
from solar_interfaces.srv import DeliverImg 
import rclpy
from rclpy.node import Node


class DeliverImgClient(Node):

    def __init__(self):
        super().__init__('deliver_client_async')
        self.cli = self.create_client(DeliverImg , 'deliver_server')
        while not self.cli.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('service not available, waiting again...')
        self.req = DeliverImg .Request()

    def send_request(self, id):
        self.req.photo_id = id
        self.future = self.cli.call_async(self.req)
        rclpy.spin_until_future_complete(self, self.future)
        return self.future.result()


def main():
    rclpy.init()

    minimal_client = DeliverImgClient()
    response = minimal_client.send_request(int(sys.argv[1]))
    minimal_client.get_logger().info(
       f'respuesta { response.photo_str}')

    minimal_client.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()