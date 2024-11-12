from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from .models import Article  # 导入你在 models.py 中定义的模型
from .serializers import ArticleSerializer  # 使用序列化来格式化输出数据
import json

# 定义接口：根据文章主键ID返回文章标题和内容
@api_view(['GET'])
def get_article_by_id(request, id):
    try:
        article = Article.objects.get(id=id)  # 根据 ID 获取文章
        response_data = {
            'title': article.title,
            'content': article.content,  # 返回原始的 Markdown 内容
        }
        return JsonResponse(response_data)
    except Article.DoesNotExist:
        return JsonResponse({'error': 'Article not found'}, status=404)

def add_article(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            title = data.get('title')
            content = data.get('content')
            print(f"Received title: {title}, content: {content}")  # 打印输出
            
            if not title or not content:
                return JsonResponse({'error': '缺少标题或内容'}, status=400)

            article = Article.objects.create(title=title, content=content)
            return JsonResponse({'message': '文章已成功添加', 'article_id': article.id})
        except json.JSONDecodeError:
            return JsonResponse({'error': '请求数据格式错误'}, status=400)
    
    return JsonResponse({'error': '仅支持 POST 请求'}, status=400)