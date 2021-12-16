from fastapi_utils.cbv import cbv
from fastapi_utils.inferring_router import InferringRouter
from fastapi import FastAPI
from model import *
from proto_py.etl_tool_client import ApplicationManagerClient
from proto_py.ApplicationManagerService_pb2_grpc import ApplicationManagerServiceStub
from google.protobuf.json_format import MessageToDict
from fastapi.middleware.cors import CORSMiddleware
from list.util_list import UtilsList

app = FastAPI()
router = InferringRouter()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@cbv(router)
class WebServer:
    application_manager_client = ApplicationManagerClient("10.208.20.16:7777", ApplicationManagerServiceStub)

    @router.get("/")
    def read_root(self):
        h = HelloWorld(content="hello")
        return h

    @router.get("/jobs")
    def get_jobs(self):
        jobs = self.application_manager_client.get_jobs()
        return list(jobs)

    @router.get("/jobs/{job_id}")
    def get_dependency(self, job_id):
        dependencies = self.application_manager_client.get_dependencies(job_id=int(job_id))
        list_d = UtilsList(dependencies)
        result = UtilsList()
        list_d.foreach(lambda x: result.append(MessageToDict(x)))
        return result


app.include_router(router)
