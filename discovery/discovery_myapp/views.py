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


@csrf_exempt  # CSRF 토큰 검사를 비활성화합니다. 보안적으로 안전하지 않으니, 실제 운영 환경에서는 신중히 사용하세요.
def analyze(request):
    if request.method == 'POST':
        return JsonResponse({'status': 'waiting'}, status=200)
    elif request.method == 'GET':
        return render(request, 'analyze.html')  # GET 요청에 대해 템플릿 렌더링
    else:
        return JsonResponse({'error': 'Invalid method'}, status=405)

@csrf_exempt
def analyze_results(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)  # JSON 데이터를 파싱합니다.
            drug_name = data.get('drug_name')

            if not drug_name:
                return JsonResponse({'error': 'Missing drug_name'}, status=400)

            try:
                drug = Drug.objects.get(drug_name=drug_name)
                response_data = {
                    'drug_image_path': drug.drug_img_path,
                    'drug_name': drug.drug_name,
                    'drug_illness': drug.drug_illness,
                }
                return JsonResponse(response_data, status=200)
            except Drug.DoesNotExist:
                return JsonResponse({'error': 'Drug not found'}, status=404)

        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)

    elif request.method == 'GET':
        return render(request, 'results.html')

    else:
        return JsonResponse({'error': 'Invalid method'}, status=405)            

def delete_pills(request):
    return render(request, 'delete_pills.html')

def aianalyzelist(request):
    if request.method == 'GET':
        drugs = Drug.objects.all()
        return render(request, 'aianalyzelist.html', {'drugs': drugs})
    else:
        return JsonResponse({"error": "Invalid HTTP method"}, status=405)