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
        return render(request, 'analyze.html')  # analyze.html 템플릿을 렌더링
    else:
        return JsonResponse({'error': 'Invalid method'}, status=405)

@csrf_exempt
def analyze_results(request):
    if request.method == 'GET': # GET 요청을 처리
        drug_names = request.GET.getlist('drug_name') # drug_name 파라미터를 리스트로 가져옴

        if not drug_names: # drug_name 파라미터가 없는 경우
            return JsonResponse({'error': 'Missing drug_name'}, status=400) # 400 에러 반환

        drugs = Drug.objects.filter(drug_name__in=drug_names) # drug_name 파라미터에 해당하는 Drug 객체들을 가져옴
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
    if request.method == 'GET': # GET 요청을 처리
        drug_names = request.GET.getlist('drug_name') # drug_name 파라미터를 리스트로 가져옴
        drug_img_paths = request.GET.getlist('drug_img_path') # drug_img_path 파라미터를 리스트로 가져옴
        drug_illnesses = request.GET.getlist('drug_illness')  # drug_illness 파라미터를 리스트로 가져옴

        if not (drug_names and drug_img_paths and drug_illnesses): # drug_name, drug_img_path, drug_illness 파라미터 중 하나라도 없는 경우
            return JsonResponse({'error': 'Missing required parameters'}, status=400) # 400 에러 반환

        if len(drug_names) != len(drug_img_paths) or len(drug_names) != len(drug_illnesses): # drug_name, drug_img_path, drug_illness 리스트의 길이가 다른 경우
            return JsonResponse({'error': 'Parameter lists are not of the same length'}, status=400) # 400 에러 반환
 
        drugs = [] 
        for drug_name, drug_img_path, drug_illness in zip(drug_names, drug_img_paths, drug_illnesses): # drug_name, drug_img_path, drug_illness 리스트를 동시에 순회
            drug = Drug.objects.filter(drug_name=drug_name, drug_img_path=drug_img_path, drug_illness=drug_illness).first() # drug_name, drug_img_path, drug_illness에 해당하는 Drug 객체를 가져옴
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