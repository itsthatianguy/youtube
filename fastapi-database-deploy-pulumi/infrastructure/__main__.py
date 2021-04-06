"""An AWS Python Pulumi program"""

import pulumi
import json
import pulumi_aws as aws


config = pulumi.Config()
db_username = config.require('db_username')
db_password = config.require_secret('db_password')

default_vpc = aws.ec2.DefaultVpc("default-vpc", tags={
    "Name": "Default VPC",
})

default_az1 = aws.ec2.DefaultSubnet("default-az-1",
    availability_zone="eu-west-2a",
    tags={
        "Name": "Default subnet for eu-west-2a",
    }
)

default_az2 = aws.ec2.DefaultSubnet("default-az-2",
    availability_zone="eu-west-2b",
    tags={
        "Name": "Default subnet for eu-west-2b",
    }
)

default_az3 = aws.ec2.DefaultSubnet("default-az-3",
    availability_zone="eu-west-2c",
    tags={
        "Name": "Default subnet for eu-west-2c",
    }
)

subnet_ids = pulumi.Output.all(default_az1.id, default_az2.id, default_az3.id).apply(lambda az: f"{az[0]},{az[1]},{az[2]}")

vpc_to_rds = aws.ec2.SecurityGroup("vpc-to-rds",
    description="Allow the resources inside the VPC to communicate with postgres RDS instance",
    vpc_id=default_vpc.id,
    ingress=[aws.ec2.SecurityGroupIngressArgs(
        from_port=5432,
        to_port=5432,
        protocol="tcp",
        cidr_blocks=[default_vpc.cidr_block],
    )])

rds = aws.rds.Instance("rds-instance",
    allocated_storage=10,
    engine="postgres",
    engine_version="13.1",
    instance_class="db.t3.micro",
    name="fastdb",
    password=db_password,
    skip_final_snapshot=True,
    username=db_username,
    vpc_security_group_ids=[vpc_to_rds.id])

instance_profile_role = aws.iam.Role("eb-ec2-role",
    assume_role_policy=json.dumps({
        "Version": "2012-10-17",
        "Statement": [{
            "Action": "sts:AssumeRole",
            "Effect": "Allow",
            "Sid": "",
            "Principal": {
                "Service": "ec2.amazonaws.com",
            },
        }],
    }))

eb_policy_attach = aws.iam.RolePolicyAttachment("eb-policy-attach",
    role=instance_profile_role.name,
    policy_arn="arn:aws:iam::aws:policy/AWSElasticBeanstalkWebTier")

instance_profile = aws.iam.InstanceProfile("eb-ec2-instance-profile", role=instance_profile_role.name)

conn = pulumi.Output.all(rds.address, db_password).apply(lambda out: f"postgresql://{db_username}:{out[1]}@{out[0]}/fastdb")

eb_app = aws.elasticbeanstalk.Application("fastapi-app", description="Testing FastAPI app deployment")

eb_env = aws.elasticbeanstalk.Environment("fastapi-env",
    application=eb_app.name,
    solution_stack_name="64bit Amazon Linux 2 v3.2.1 running Python 3.8",
    settings=[
        aws.elasticbeanstalk.EnvironmentSettingArgs(
            namespace="aws:elasticbeanstalk:environment:proxy",
            name="ProxyServer",
            value="apache"
        ),
        aws.elasticbeanstalk.EnvironmentSettingArgs(
            namespace="aws:autoscaling:launchconfiguration",
            name="IamInstanceProfile",
            value=instance_profile.name
        ),
        aws.elasticbeanstalk.EnvironmentSettingArgs(
            namespace="aws:ec2:vpc",
            name="VPCId",
            value=default_vpc.id,
        ),
        aws.elasticbeanstalk.EnvironmentSettingArgs(
            namespace="aws:ec2:vpc",
            name="Subnets",
            value=subnet_ids,
        ),
        aws.elasticbeanstalk.EnvironmentSettingArgs(
            namespace="aws:elasticbeanstalk:application:environment",
            name="CONNECTION_STRING",
            value=conn,
        ),
    ])

pulumi.export('connection_string', conn)
