from django.shortcuts import render, redirect
from .models import Drug  # Drug 모델을 임포트
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json  # JSON 파싱을 위해 임포트

@csrf_exempt  # CSRF 토큰 검사를 비활성화합니다. 보안적으로 안전하지 않으니, 실제 운영 환경에서는 신중히 사용하세요.
def analyze(request):
    if request.method == 'POST':
        return JsonResponse({'status': 'waiting'}, status=200)
    else:
        return JsonResponse({'error': 'Invalid method'}, status=405)

@csrf_exempt
def analyze_results(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            drug_name = data.get('drug_name')

            if not drug_name:
                return JsonResponse({'error': 'Missing data fields'}, status=400)

            # 실제 데이터베이스에서 데이터를 가져옵니다.
            try:
                drug = Drug.objects.get(drug_name=drug_name)
                response_data = {
                    "drug_image_url": drug.drug_img_key,
                    "drug_name": drug.drug_name,
                    "drug_illness": drug.drug_illness
                }
                return JsonResponse(response_data, status=200)
            except Drug.DoesNotExist:
                return JsonResponse({'error': 'Drug not found'}, status=404)

        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)
        except KeyError:
            return JsonResponse({'error': 'Missing required keys'}, status=400)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    else:
        return JsonResponse({'error': 'Invalid method'}, status=405)

def results(request):
    drugs = Drug.objects.all()  # Drug 모델을 사용
    return render(request, 'results.html', {'drugs': drugs})

def delete_pills(request):
    return render(request, 'delete_pills.html')

# def submit_deletions(request):
#     # 삭제 처리 로직 추가
#     return render(request, 'submit_deletions.html')

def aianalyzelist(request):
    drugs = Drug.objects.all()  # Drug 모델을 사용하여 모든 약물 데이터를 가져옴
    return render(request, 'aianalyzelist.html', {'drugs': drugs})

# def go_to_analyzeList(request):
#     return redirect('analyzelist')
