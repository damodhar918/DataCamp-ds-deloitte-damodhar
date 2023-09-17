import cdk = require("@aws-cdk/core");
import fs = require("fs");
import apigw = require("@aws-cdk/aws-apigateway");
import lambda = require("@aws-cdk/aws-lambda");
import { AwsLambdaApigatewayStack } from "./apigateway-stack";

export class LambdaAuthorizerConstruct extends cdk.Construct {
  public readonly id: string;

  constructor(scope: AwsLambdaApigatewayStack, id: string) {
    super(scope, id);

    let uid: string = "";
    if (fs.existsSync("tmp/cache/uid-authorizer")) {
      uid = fs
        .readFileSync("tmp/cache/uid-authorizer")
        .toString()
        .replace(/^.+?:(.+?)\n$/, "$1");
    }

    const fn = new lambda.Function(scope, "authorizerLambda", {
      functionName: `${scope.stackName}-Authorizer`,
      runtime: lambda.Runtime.GO_1_X,
      code: lambda.Code.fromBucket(scope.lambdaBucket, `authorizer/_build/authorizer-${uid}.zip`),
      handler: `_build/authorizer-${uid}`,
      memorySize: 128,
      timeout: cdk.Duration.seconds(30),
      environment: {}
    });
    fn.addPermission(`${scope.stackName}-Authorizer`, scope.apiLambdaPermission);

    const authorizer = new apigw.CfnAuthorizer(scope, "lambdaAuthorizer", {
      name: "lambdaAuthorizer",
      restApiId: scope.api.restApiId,
      type: "REQUEST",
      authorizerUri: `arn:aws:apigateway:${scope.region}:lambda:path/2015-03-31/functions/${fn.functionArn}/invocations`,
      authorizerResultTtlInSeconds: 300,
      identitySource: `method.request.header.${scope.envAuthorizationHeaderName}`
    });

    this.id = authorizer.ref;
  }
}
