from .models import Article
from .serializers import ArticleSerializer
from rest_framework import generics
from rest_framework.response import Response


class ArticleList(generics.ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

    def list(self, request):
        print("heyehey")
        queryset = self.get_queryset()
        serializer = ArticleSerializer(queryset, many=True)
        return Response(serializer.data)
