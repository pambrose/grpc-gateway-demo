from gen.echo_service_pb2 import  StringMessage
from gen.echo_service_pb2 import EchoServiceServicer
from gen.echo_service_pb2 import add_EchoServiceServicer_to_server
from grpc_support import GenericServer
from utils import current_time_millis
from utils import setup_logging
import logging
import time
import grpc
from concurrent import futures

logger = logging.getLogger(__name__)

class EchoServer(EchoServiceServicer, GenericServer):
    def __init__(self, port=None):
        super(EchoServer, self).__init__(port=port, desc="echo server")
        self._start_time = current_time_millis()
        self.grpc_server = None

    def Echo(self, request, context):
        value = request.value
        return StringMessage(value=value)

    def _init_values_on_start(self):
        pass

    def _start_server(self):
        logger.info("Starting gRPC {0} listening on {1}".format(self.desc, self.hostname))
        self.grpc_server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
        add_EchoServiceServicer_to_server(self, self.grpc_server)
        self.grpc_server.add_insecure_port(self.hostname)
        self.grpc_server.start()
        try:
            while not self.stopped:
                time.sleep(1)
        except KeyboardInterrupt:
            pass
        finally:
            self.stop()

if __name__ == "__main__":
    setup_logging()

    EchoServer().start()
