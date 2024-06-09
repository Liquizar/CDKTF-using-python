#!/usr/bin/env python
from constructs import Construct
from cdktf import App, NamedRemoteWorkspace, TerraformStack, TerraformOutput
from cdktf_cdktf_provider_aws.provider import AwsProvider
from cdktf_cdktf_provider_aws.instance import Instance


class MyStack(TerraformStack):
    def __init__(self, scope: Construct, ns: str):
        super().__init__(scope, ns)

        AwsProvider(self, "AWS", region="ap-south-1")

        instance = Instance(self, "Instance",
                            ami="ami-0f58b397bc5c1f2e8",
                            instance_type="t2.micro",
                            tags={"Name": "example-cdktf"})

        TerraformOutput(self, "public_ip",
                        value=instance.public_ip,
                        )


app = App()
stack = MyStack(app, "aws_instance")

app.synth()
