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
        drug_names = request.GET.getlist('drug_name')

        if not drug_names:
            return JsonResponse({'error': 'Missing drug_name'}, status=400)

        drugs = Drug.objects.filter(drug_name__in=drug_names)
        if drugs.exists():
            drug_list = []
            for drug in drugs:
                drug_list.append({
                    'status_code': 200,
                    'drug_img_path': drug.drug_img_path,
                    'drug_name': drug.drug_name,
                    'drug_illness': drug.drug_illness,
                    'drug_price': drug.drug_price
                })
            return JsonResponse(drug_list, safe=False)
        else:
            return JsonResponse({'error': 'No drugs found'}, status=404)
    else:
        return JsonResponse({'error': 'Invalid HTTP method'}, status=405)
    
@csrf_exempt
def aianalyzelist(request):
    if request.method == 'GET':
        drug_names = request.GET.getlist('drug_name')
        drug_img_paths = request.GET.getlist('drug_img_path')
        drug_illnesses = request.GET.getlist('drug_illness')

        if not (drug_names and drug_img_paths and drug_illnesses):
            return JsonResponse({'error': 'Missing required parameters'}, status=400)

        if len(drug_names) != len(drug_img_paths) or len(drug_names) != len(drug_illnesses):
            return JsonResponse({'error': 'Parameter lists are not of the same length'}, status=400)

        drugs = []
        for drug_name, drug_img_path, drug_illness in zip(drug_names, drug_img_paths, drug_illnesses):
            drug = Drug.objects.filter(drug_name=drug_name, drug_img_path=drug_img_path, drug_illness=drug_illness).first()
            if drug:
                drugs.append({
                    'status_code': 200,
                    'drug_illness': drug.drug_illness,
                    'drug_name': drug.drug_name,
                    'drug_price': drug.drug_price,
                    'drug_img_path': drug.drug_img_path
                })
            else:
                drugs.append({
                    'status_code': 404,
                    'error': 'Drug not found',
                    'drug_name': drug_name,
                    'drug_img_path': drug_img_path,
                    'drug_illness': drug_illness
                })

        return JsonResponse(drugs, safe=False)
    else:
        return JsonResponse({"error": "Invalid HTTP method"}, status=405)