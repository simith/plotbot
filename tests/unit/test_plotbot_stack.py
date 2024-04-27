import aws_cdk as core
import aws_cdk.assertions as assertions

from plotbot.plotbot_stack import PlotbotStack

# example tests. To run these tests, uncomment this file along with the example
# resource in plotbot/plotbot_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = PlotbotStack(app, "plotbot")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
