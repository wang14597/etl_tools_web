import grpc
from google.protobuf import empty_pb2
from proto_py.ApplicationManagerService_pb2 import GetDependenciesRequest


class EtlToolsWebClient:

    def __enter__(self):
        self._channel = grpc.insecure_channel(self.address)
        self._stub = self.service(self._channel)

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._channel.close()

    def __init__(self, address, service):
        self.address = address
        self.service = service


class ApplicationManagerClient(EtlToolsWebClient):

    def get_jobs(self):
        jobs = self._stub.getJobs(empty_pb2.Empty())
        return jobs.jobId

    def get_dependencies(self, **kwargs):
        dependencies = self._stub.getDependencies(
            GetDependenciesRequest(jobId=kwargs["job_id"], taskId=kwargs["task_id"]))
        return dependencies.stages
