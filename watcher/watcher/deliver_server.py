import cv2
import json

from solar_interfaces.srv import DeliverImg

import rclpy
from rclpy.node import Node

from .redis_store import get_bytes


class DeliverService(Node):

    def __init__(self):
        super().__init__('deliver_service')
        self.srv = self.create_service(DeliverImg, 'deliver_server', self.deliver_photo)

    def deliver_photo(self, request, response):
        # response.sum = request.a + request.b

        self.get_logger().info(f'Incoming request photo with id {request.photo_id}')
        ret, image = get_bytes(str(request.photo_id))

        data  = {'id' : request.photo_id, 'image' : image}
        if not ret:
            data['error'] = 'foto  no disponible en el cache, id incorrecto'
            
        response.photo_str = json.dumps(data, default=str)
        return response


def main():
    rclpy.init()

    deliver_service = DeliverService()

    rclpy.spin(deliver_service)

    rclpy.shutdown()


if __name__ == '__main__':
    main()