from django.shortcuts import render
from posting.serializer import TaskSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.


@api_view(["GET"])
def getTaskList(request):
    TaskSetQuery = Task.objects.all() #데이터베이스에서 가져오고자 하는 문장
    serializer = TaskSerializer(TaskSetQuery, many=True) #many=True : 데이터가 많을 수도 있다. 1개가 아니다
    print(serializer.data)
    return Response(serializer.data, status=200)
    #query문 SELECT * FROM TASK
    #migrate은 데이터를 변경했을 때만 하는 것

@api_view(['POST'])
def addTask(request):
    if request.method == 'POST' : 
        serializers = TaskSerializer(data=request.data)
        if serializers.is_vaild():
            serializers.save()
            return Response(serializers.data, status=200)
        else :
            print(serializers.errors)
        return Response(serializers.errors, status=400) 