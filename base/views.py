from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import OperationSerializer
# Create your views here.



operations = ["addition","subtraction","multiplication"]
addition_listener = ["add","sum","addition","summation","plus","adding","+","together","togetheness"]
substraction_listener = ["difference","minus","deduct","remove","less","deduction","subtraction","subtract","-"]
multiplication_listener = ["product","multiply","multiplication","x","X","*"]

@api_view(['POST'])
def arithmetic(request): 
    if request.method == "POST":
        data_query = request.data
        serializer = OperationSerializer(data=data_query)
        if serializer.is_valid():
            serializer.save()
            received_data = serializer.data
            # print(received_data["operation_type"])
            words = received_data["operation_type"].lower().split()


            

            for keyword in words:
                if keyword in addition_listener:
                    x = received_data["x"]
                    y = received_data["y"]
                    result = x + y
                    operation_type = operations[0]

                elif keyword in substraction_listener:
                    x = received_data["x"]
                    y = received_data["y"]
                    result = x - y
                    operation_type = operations[1]
                
                elif keyword in multiplication_listener:
                    x = received_data["x"]
                    y = received_data["y"]
                    result = x * y
                    operation_type = operations[2]

                else:
                    x = received_data["x"]
                    y = received_data["y"]
                    operation_type = received_data["operation_type"]
                    result = 0






            
            # print(words)
            # print(received_data["x"])
            # return Response(received_data)



            context = {
                "slackUsername":"bhen",   
                "result":result,         
                "operation_type":operation_type
                
            }

            return Response(context)
        

