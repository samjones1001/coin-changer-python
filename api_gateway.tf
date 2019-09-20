resource "aws_api_gateway_rest_api" "coin-changer-api" {
    name = "CoinChanger"
    description = "Coin Changer API"
}

resource "aws_api_gateway_resource" "changer" {
    rest_api_id = "${aws_api_gateway_rest_api.coin-changer-api.id}"
    parent_id = "${aws_api_gateway_rest_api.coin-changer-api.root_resource_id}"
    path_part = "changer"
}

resource "aws_api_gateway_method" "changer" {
    rest_api_id = "${aws_api_gateway_rest_api.coin-changer-api.id}"
    resource_id = "${aws_api_gateway_resource.changer.id}"
    http_method = "POST"
    authorization = "NONE"
}

resource "aws_api_gateway_integration" "changer" {
    rest_api_id = "${aws_api_gateway_rest_api.coin-changer-api.id}"
    resource_id = "${aws_api_gateway_resource.changer.id}"
    http_method = "${aws_api_gateway_method.changer.http_method}"
    type = "AWS_PROXY"
    uri = "${aws_lambda_function.coin_changer.invoke_arn}"
    integration_http_method = "POST"
}

resource "aws_api_gateway_deployment" "coin-changer-api" {
    depends_on = [
        "aws_api_gateway_integration.changer"
    ]

    rest_api_id = "${aws_api_gateway_rest_api.coin-changer-api.id}"
    stage_name = "test"
}

output "base_url" {
    value = "${aws_api_gateway_deployment.coin-changer-api.invoke_url}"
}