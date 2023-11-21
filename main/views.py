from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from main.servises import check_format, search_form


class FormAPIView(APIView):

    def post(self, request):
        query_params = request.query_params
        validated_data = check_format(query_params)
        response = search_form(validated_data)

        if response:
            return Response(status=status.HTTP_200_OK, data={"template_name": response.name})

        return Response(status=status.HTTP_200_OK, data=validated_data)
