from django.http import JsonResponse, HttpResponseBadRequest
import json
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def echo_view_add(request, *args, **kwargs):
    return api_calculator(request, 'add')


@csrf_exempt
def echo_view_subtract(request, *args, **kwargs):
    return api_calculator(request, 'subtract')


@csrf_exempt
def echo_view_multiply(request, *args, **kwargs):
    return api_calculator(request, 'multiply')


@csrf_exempt
def echo_view_divide(request, *args, **kwargs):
    return api_calculator(request, 'divide')


def api_calculator(request, method_calculator):
    data = {
        "A": 1234,
        "B": 4567
    }

    a = data["A"]
    b = data["B"]

    if isinstance(a, (int, float)) or isinstance(b, (int, float)):
        if method_calculator == 'add':
            result = a + b
            return JsonResponse({"answer": result})
        elif method_calculator == 'subtract':
            result = a - b
            return JsonResponse({"answer": result})
        elif method_calculator == 'multiply':
            result = a * b
            return JsonResponse({"answer": result})
        elif method_calculator == 'divide':
            if b == 0:
                return HttpResponseBadRequest(json.dumps({"error": "Делить на ноль сегодня нельзя :("}),
                                              content_type="application/json")
            else:
                result = a / b
                return JsonResponse({"answer": result})
    else:
        return JsonResponse({"error": "A and B must be numbers"}, status=400)
