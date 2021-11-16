import * as cdk from '@aws-cdk/core';
import * as lambda from '@aws-cdk/aws-lambda';
import * as aws_s3 from '@aws-cdk/aws-s3';
import * as path from 'path';

export class LunaV2Stack extends cdk.Stack {
    constructor(scope: cdk.Construct, id: string, props?: cdk.StackProps) {
        super(scope, id, props);

        const bucket = new aws_s3.Bucket(this, 'Bucket', {
            versioned: true
        })

        const createEvent = new lambda.Function(this, "createEventCalendar", {
            runtime: lambda.Runtime.PYTHON_3_8,
            handler: "main.create_event",
            code: lambda.Code.fromAsset(
                path.join('lambdas/create_event'),
                {
                    bundling: {
                        image: lambda.Runtime.PYTHON_3_8.bundlingImage,
                        command: [
                            'bash',
                            '-c',
                            [
                                'pip install -r requirements.txt -t /asset-output',
                                'cp -au *.py /asset-output',
                                'cp -au *.json /asset-output'
                            ].join(' && '),
                        ],
                    },
                }
            ),
            environment: {
                "BUCKET": bucket.bucketName
            }
        })

        bucket.grantReadWrite(createEvent)
    }
}
