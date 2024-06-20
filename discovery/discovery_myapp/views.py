from django.shortcuts import render, redirect
from .models import Drug  # Drug 모델을 임포트
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json  # JSON 파싱을 위해 임포트
from django.shortcuts import render
import logging

# 로깅 설정
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)


@csrf_exempt  # CSRF 토큰 검사를 비활성화
def analyze(request):
    if request.method == 'POST':
        return JsonResponse({'status': 'waiting'}, status=200)
    elif request.method == 'GET':
        return render(request, 'analyze.html')  # GET 요청에 대해 템플릿 렌더링
    else:
        return JsonResponse({'error': 'Invalid method'}, status=405)

@csrf_exempt
def analyze_results(request):
    if request.method == 'GET':
        drug_name = request.GET.get('drug_name')

        if not drug_name:
            return JsonResponse({'error': 'Missing drug_name'}, status=400)

        drug = Drug.objects.filter(drug_name=drug_name).first()
        if drug:
            response_data = {
                'status_code': 200,
                'drug_img_path': drug.drug_img_path,
                'drug_name': drug.drug_name,
                'drug_illness': drug.drug_illness,
            }
            return JsonResponse(response_data, status=200)
        else:
            return JsonResponse({'error': 'Drug not found'}, status=404)

    # GET 요청 시 results.html을 렌더링합니다.
    drugs = Drug.objects.all()
    return render(request, 'results.html', {'drugs': drugs})   

def aianalyzelist(request):
    if request.method == 'GET':
        drug_name = request.GET.get('drug_name')
        drug_img_path = request.GET.get('drug_img_path')
        drug_illness = request.GET.get('drug_illness')

        if not drug_name or not drug_img_path or not drug_illness:
            return JsonResponse({'error': 'Missing required parameters'}, status=400)

        drug = Drug.objects.filter(drug_name=drug_name, drug_img_path=drug_img_path, drug_illness=drug_illness).first()
        if drug:
            response_data = {
                'status_code': 200,
                'drug_illness': drug.drug_illness,
                'drug_name': drug.drug_name,
                'drug_price': drug.drug_price,
                'drug_img_path': drug.drug_img_path
            }
            return JsonResponse(response_data, status=200)
        else:
            return JsonResponse({'error': 'Drug not found'}, status=404)
    else:
        return JsonResponse({"error": "Invalid HTTP method"}, status=405)